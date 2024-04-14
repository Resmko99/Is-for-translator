import configparser
import sys
import os
from io import BytesIO

import cv2
import time

import numpy as np
from PIL import Image
from PySide6.QtCore import (Qt, QPoint, QPropertyAnimation, QEasingCurve, QEvent, QDate,
                            QTimer, QRegularExpression, QStandardPaths)
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea, QHBoxLayout,
                               QGridLayout, QPushButton, QFileDialog, QHeaderView, QMessageBox, QInputDialog)
from PySide6.QtGui import QPixmap, QPainter, QCursor, QPalette, QColor, QStandardItemModel, QStandardItem, \
    QRegularExpressionValidator
from cryptography.fernet import Fernet

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials


from googletrans import Translator
from functools import partial
from ui import Ui_MainWindow
from database import connect, close_db_connect

import psycopg2

directory = os.path.abspath(os.curdir)


class Calender(QWidget):
    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.ui = ui
        self.init_ui()

    def init_ui(self):
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

        # Заменяем создание выпадающего списка month_combo на использование comboBoxMonth
        self.month_combo = self.ui.comboBoxMonth
        self.month_combo.addItems([
            "Январь", "Февраль", "Март", "Апрель",
            "Май", "Июнь", "Июль", "Август",
            "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
        ])
        self.month_combo.setCurrentIndex(QDate.currentDate().month() - 1)
        self.month_combo.currentIndexChanged.connect(self.update_calendar)

        # Заменяем создание выпадающего списка year_combo на использование comboBoxYear
        self.year_combo = self.ui.comboBoxYear
        self.year_combo.addItems([str(year) for year in range(1900, 2101)])
        self.year_combo.setCurrentText(str(QDate.currentDate().year()))
        self.year_combo.currentIndexChanged.connect(self.update_calendar)

        # Создаем сетку для дней недели и чисел месяца
        self.grid_layout = QGridLayout()
        self.grid_layout.setHorizontalSpacing(0)
        self.grid_layout.setVerticalSpacing(0)
        self.layout.addLayout(self.grid_layout, 0, 0)

        # Добавляем дни месяца
        self.update_calendar()

    def update_calendar(self):
        month_index = self.month_combo.currentIndex() + 1
        year = int(self.year_combo.currentText())
        days_in_month = QDate(year, month_index, 1).daysInMonth()

        # Очищаем текущие дни месяца
        for i in reversed(range(1, self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # Определяем начальную позицию для первого числа месяца
        row = 1  # Начинаем с второй строки (первая строка занята заголовками дней недели)
        col = 0  # Первый столбец

        for day in range(1, days_in_month + 1):
            button = QPushButton(str(day))
            button.setMaximumSize(330, 330)
            button.setStyleSheet(
                '''
                QPushButton {
                    background-color: #010409;
                    border: 1px solid #FFCC33;
                    border-radius: 10px;
                    font: 20px "Inter";
                    color: #FFFFFF;
                }

                QPushButton:pressed {
                    background-color: #BEA14B;
                }
                '''
            )
            self.grid_layout.addWidget(button, row, col)
            col = (col + 1) % 7
            if col == 0:
                row += 1
            button.clicked.connect(partial(self.set_date_in_date_edit, day, month_index, year))
            button.clicked.connect(partial(self.ui.stackedWidget_2.setCurrentWidget, self.ui.pageListTask))

    def set_date_in_date_edit(self, day, month, year):
        date = QDate(year, month, day)
        self.ui.dateEdit.setDate(date)


class RoundedImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(10, 10, 10, 10)
        self.setStyleSheet("border-radius: 10px; border: 1px solid #FFCC33;")

    def setPixmap(self, pixmap):
        rounded_pixmap = self.rounded_pixmap(pixmap)
        super().setPixmap(rounded_pixmap)

    def rounded_pixmap(self, pixmap):
        rounded_pixmap = QPixmap(pixmap.size())
        rounded_pixmap.fill(Qt.transparent)
        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.white)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(pixmap.rect(), 10, 10)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        return rounded_pixmap


class ImageScrollArea(QWidget):
    def __init__(self, team_id=None, search_text=None, parent=None):
        super().__init__(parent)
        self.team_id = team_id
        self.search_text = search_text
        self.loaded = False
        self.setup_ui()

    def setup_ui(self):
        self.scroll_area_contents_layout = QVBoxLayout(self)
        self.scroll_area_contents_layout.setAlignment(Qt.AlignTop)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scrollContent = QWidget()
        self.scrollLayout = QVBoxLayout(self.scrollContent)

        self.scroll.setStyleSheet(
            """
            QScrollArea {
                background-color: #24282E;
                border: none;
            }

            QScrollBar:vertical, QScrollBar:horizontal {
                background-color: transparent;
                border: none;
                border-radius: 5px;
                width: 10px;
                height: 10px;
            }

            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
                background-color: #FFFFFF;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                background-color: #2E333A;
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                background: none;
            }

            QScrollArea QWidget {
                background-color: transparent;
            }
            """
        )

        if self.team_id is not None:
            self.load_images_from_database(team_id=self.team_id, search_text=self.search_text)
        else:
            self.load_images_from_database(search_text=self.search_text)  # Иначе загружаем все тайтлы

        self.scrollLayout.addStretch()
        self.scroll.setWidget(self.scrollContent)
        self.scroll_area_contents_layout.addWidget(self.scroll)

    def clear_titles(self):
        while self.scrollLayout.count():
            widget = self.scrollLayout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

    def load_images_from_database(self, team_id=None, search_text=None):
        # Очищаем существующие тайтлы перед загрузкой новых
        self.clear_titles()

        connection = connect()
        cursor = connection.cursor()

        if team_id is not None and search_text is not None:
            cursor.execute(
                'SELECT "title_name", "icon_title", "title_id" FROM "Title" WHERE "team_id" = %s AND "title_name" ILIKE %s ORDER BY "title_id" ASC',
                (team_id, f'%{search_text}%'))
        elif team_id is not None:
            cursor.execute(
                'SELECT "title_name", "icon_title", "title_id" FROM "Title" WHERE "team_id" = %s ORDER BY "title_id" ASC',
                (team_id,))
        elif search_text is not None:
            cursor.execute(
                'SELECT "title_name", "icon_title", "title_id" FROM "Title" WHERE "title_name" ILIKE %s ORDER BY "title_id" ASC',
                (f'%{search_text}%',))
        else:
            cursor.execute('SELECT "title_name", "icon_title", "title_id" FROM "Title" ORDER BY "title_id" ASC')

        rows = cursor.fetchall()

        self.loaded = True

        images_per_row = 4
        current_row_layout = None

        for i, row in enumerate(rows):
            if i % images_per_row == 0:
                current_row_layout = QHBoxLayout()
                self.scrollLayout.addLayout(current_row_layout)

            image_text_container = QWidget()
            image_text_container.setStyleSheet("background-color: #3D434B;"
                                               "border: none;"
                                               "border-radius: 10px;"
                                               "border: 2px solid #FFCC33;"
                                               "margin: 15px;")

            image_text_layout = QVBoxLayout(image_text_container)

            label = RoundedImageLabel()
            label.title_id = row[2]

            # Преобразование байтов изображения в QPixmap
            pixmap = QPixmap()
            pixmap.loadFromData(bytes(row[1]))
            pixmap = pixmap.scaled(370, 500, Qt.IgnoreAspectRatio)

            if not pixmap.isNull():
                label.setPixmap(pixmap)
            else:
                label.setText("Image not found")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("border: none; color: #FFFFFF;")
            image_text_layout.addWidget(label)

            text_label = QLabel(row[0])  # Используем текст из базы данных
            image_text_layout.addWidget(text_label)
            text_label.setStyleSheet('color: #fff; border: none; margin-top: 2px; font: 18px "Inter";')
            text_label.setAlignment(Qt.AlignCenter)

            current_row_layout.addWidget(image_text_container)

        close_db_connect(connection, cursor)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize_direction = None
        self.connection = connect()
        self.resize_offset = QPoint()
        self.drag_position = None
        self.mouse_press_position = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.icon.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.openMenuBtn.clicked.connect(self.toggle_full_menu)
        self.ui.fullMenu.hide()
        self.ui.icon.show()
        self.ui.titleBtn_2.setChecked(True)
        self.ui.dateEdit.dateChanged.connect(self.get_data)

        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

        self.normal_geometry = None

        self.model_table_task = QStandardItemModel()
        self.ui.tableListTask.setModel(self.model_table_task)

        self.model_table_income = QStandardItemModel()
        self.ui.tableIncome.setModel(self.model_table_income)

        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

        # Выделение рамки подсказки
        app_palette = QApplication.palette()
        app_palette.setColor(QPalette.ToolTipBase, QColor("#3D434B"))
        app_palette.setColor(QPalette.ToolTipText, Qt.white)
        QApplication.setPalette(app_palette)
        self.setStyleSheet(
            "QToolTip { background-color: #3D434B; color: white; border: 1px solid #FFCC33; }")

        # Подсказки
        self.ui.incomeBtn_1.setToolTip("Доходы")
        self.ui.titleBtn_1.setToolTip("Тайтлы")
        self.ui.scheduleBtn_1.setToolTip("Расписание")
        self.ui.socialNetworksBtn_1.setToolTip("Соц. сеть")
        self.ui.fileSharingBtn_1.setToolTip("Обмен файлами")
        self.ui.accountBtn_1.setToolTip("Аккаунт")
        self.ui.translateBtn_1.setToolTip("Переводчик")
        self.ui.aboutUs_1.setToolTip("О нас")

        validator = QRegularExpressionValidator(QRegularExpression("[0-9.]*"))
        self.ui.salaryAddIncome.setValidator(validator)

        self.normal_geometry = None

        page_buttons = [
            (self.ui.incomeBtn_1, self.ui.incomeBtn_2, self.ui.pageIncome),
            (self.ui.titleBtn_1, self.ui.titleBtn_2, self.ui.pageTitle),
            (self.ui.scheduleBtn_1, self.ui.scheduleBtn_2, self.ui.pageSchedule),
            (self.ui.socialNetworksBtn_1, self.ui.socialNetworksBtn_2, self.ui.pageSocialNetwork),
            (self.ui.fileSharingBtn_1, self.ui.fileSharingBtn_2, self.ui.pageFileSharing),
            (self.ui.accountBtn_1, self.ui.accountBtn_2, self.ui.pageAccount),
            (self.ui.aboutUs_1, self.ui.aboutUs_2, self.ui.pageAboutUs),
            (self.ui.translateBtn_1, self.ui.translateBtn_2, self.ui.pageTranslator)
        ]
        for button, button_2, page in page_buttons:
            for btn in [button, button_2]:
                btn.clicked.connect(partial(self.ui.stackedWidget_2.setCurrentWidget, page))

        move_buttons = [
            (self.ui.backAddTitleBtn, self.ui.pageTitle),
            (self.ui.backBtnDesc, self.ui.pageTitle),
            (self.ui.pushOpenAdd, self.ui.pageAddTitle),
            (self.ui.cancelPageList, self.ui.pageSchedule),
            (self.ui.addListTask, self.ui.pageAddTask),
            (self.ui.backTaskBtn, self.ui.pageListTask),
            (self.ui.backApplyTaskBtn, self.ui.pageListTask),
            (self.ui.backTaskViewBtn, self.ui.pageListTask),
            (self.ui.incomeAddBtn, self.ui.pageAddIncome),
            (self.ui.backAddIncome, self.ui.pageIncome),
            (self.ui.backEditIncome, self.ui.pageIncome)
        ]

        for button, page in move_buttons:
            button.clicked.connect(partial(self.ui.stackedWidget_2.setCurrentWidget, page))

        self.ui.tableListTask.doubleClicked.connect(self.view_task)
        self.ui.closeBtn.clicked.connect(self.closeApp)
        self.ui.expandBtn.clicked.connect(self.toggle_screen_state)
        self.ui.minimazeBtn.clicked.connect(self.minimizeApp)
        self.ui.taskAddBtn.clicked.connect(self.apply_task)
        self.ui.addIncomeBtn.clicked.connect(self.apply_income)
        self.screen_expanded = False

        # Установка фильтра событий для главного окна
        self.open_hand_px = QPixmap(directory + f'/Photo/free-icon-cursor-5340828.png')
        self.scaled_open_hand_px = self.open_hand_px.scaled(16, 16)
        self.scaled_open_hand_px.setMask(self.scaled_open_hand_px.mask())
        self.open_hand_cursor = QCursor(self.scaled_open_hand_px, 0, 0)
        self.setCursor(self.open_hand_cursor)
        self.current_cursor = self.open_hand_cursor

        self.installEventFilter(self)

        self.load_title_teams()
        self.ui.comboboxTitle.currentIndexChanged.connect(self.load_titles_by_team)
        self.load_titles_by_team()

        self.setup_calender_widget()
        self.get_data()

        self.translation_delay = 1000
        self.translation_timer = QTimer()
        self.translation_timer.setSingleShot(True)
        self.translation_timer.timeout.connect(self.translate_text)
        self.init_translator_ui()
        self.ui.textEdit.textChanged.connect(self.on_text_edit_changed)
        self.ui.deleteListTask.clicked.connect(self.delete_selected_task)
        self.ui.tableListTask.clicked.connect(self.state_edit_button)
        self.ui.taskApplyBtn.clicked.connect(self.update_task)
        self.ui.crewComboBox.currentIndexChanged.connect(self.get_income)
        self.ui.incomeEditBtn.clicked.connect(self.edit_income)
        self.ui.editIncomeBtn.clicked.connect(self.update_income)
        self.ui.incomeDeleteBtn.clicked.connect(self.delete_selected_income)
        self.ui.addLogo.clicked.connect(self.add_logo_button_clicked)

        self.ui.stackedWidget_2.currentChanged.connect(self.load_description)
        self.ui.deleteTitleBtn.clicked.connect(self.delete_title)
        self.ui.editTitleBtn.clicked.connect(self.open_edit_title_page)
        self.ui.backEditTitleBtn.clicked.connect(self.switch_to_page_desc)
        self.ui.applyEditBtn.clicked.connect(self.apply_title_changes)
        self.ui.imageAreaEdit.mouseDoubleClickEvent = self.open_image_dialog
        self.ui.imageArea.mouseDoubleClickEvent = self.open_image_dialog_add_title
        self.ui.addTitleBtn.clicked.connect(self.add_title_to_database)
        self.ui.descriptionEdit_2.verticalScrollBar().setStyleSheet("""
                            QScrollBar:vertical {
                                background-color: transparent;
                                border: none;
                                border-radius: 5px;
                                width: 15px;
                                margin-right: 5px; 
                                margin-top: 2px;
                                margin-bottom: 2px;
                            }

                            QScrollBar::handle:vertical {
                                background-color: #FFFFFF;
                                border-radius: 5px;
                                min-height: 20px;
                            }

                            QScrollBar::add-line:vertical,
                            QScrollBar::sub-line:vertical {
                                background-color: #2E333A;
                                height: 0px;
                                subcontrol-position: bottom;
                                subcontrol-origin: margin;
                            }

                            QScrollBar::add-page:vertical,
                            QScrollBar::sub-page:vertical {
                                background: none;
                            }
                        """)
        self.ui.descriptionEdit.verticalScrollBar().setStyleSheet("""
                            QScrollBar:vertical {
                                background-color: transparent;
                                border: none;
                                border-radius: 5px;
                                width: 15px;
                                margin-right: 5px;
                                margin-top: 2px;
                                margin-bottom: 2px;
                            }

                            QScrollBar::handle:vertical {
                                background-color: #FFFFFF;
                                border-radius: 5px;
                                min-height: 20px;
                            }

                            QScrollBar::add-line:vertical,
                            QScrollBar::sub-line:vertical {
                                background-color: #2E333A;
                                height: 0px;
                                subcontrol-position: bottom;
                                subcontrol-origin: margin;
                            }

                            QScrollBar::add-page:vertical,
                            QScrollBar::sub-page:vertical {
                                background: none;
                            }
                        """)

        self.ui.textEditDesc.verticalScrollBar().setStyleSheet("""
                                 QScrollBar:vertical {
                                     background-color: transparent;
                                     border: none;
                                     border-radius: 5px;
                                     width: 15px;
                                     margin-right: 5px;
                                     margin-top: 2px;
                                     margin-bottom: 2px;
                                 }

                                 QScrollBar::handle:vertical {
                                     background-color: #FFFFFF;
                                     border-radius: 5px;
                                     min-height: 20px;
                                 }

                                 QScrollBar::add-line:vertical,
                                 QScrollBar::sub-line:vertical {
                                     background-color: #2E333A;
                                     height: 0px;
                                     subcontrol-position: bottom;
                                     subcontrol-origin: margin;
                                 }

                                 QScrollBar::add-page:vertical,
                                 QScrollBar::sub-page:vertical {
                                     background: none;
                                 }
                             """)
        self.ui.SearchBtn.clicked.connect(self.load_titles_by_team)
        self.ui.inLogBtn.clicked.connect(self.login_button_clicked)

        self.ui.titleBtn_1.clicked.connect(self.load_titles_by_team)
        self.ui.titleBtn_2.clicked.connect(self.load_titles_by_team)
        self.ui.incomeBtn_1.clicked.connect(self.get_income)
        self.ui.incomeBtn_2.clicked.connect(self.get_income)

        self.autentificate = False
        self.ui.fileSharingBtn_1.clicked.connect(self.post_init)
        self.ui.fileSharingBtn_2.clicked.connect(self.post_init)

        self.generate_key()
        self.load_saved_credentials()

        self.load_team()
        self.load_title_income()
        self.load_users()
        self.get_data()
        self.get_income()
        self.load_edit_users()
        self.load_edit_team_income()
        self.load_edit_title_income()
        self.load_account_teams()
        self.load_edit_teams()

        self.file_path = None
        self.folder_id = None

        self.ui.dateReleaseAddTitle.setDate(QDate.currentDate())
        self.ui.sendFile.clicked.connect(self.upload_to_drive)  # Выбор папки
        self.ui.fileAdd.mouseDoubleClickEvent = self.file_add_double_click

    def post_init(self):
        if not self.autentificate:

            self.drive_service = self.authenticate()  # Переместить сюда
            self.get_folders()
            self.autentificate = True
        else:
            return
    def file_add_double_click(self, event):
        if event.button() == Qt.LeftButton:
            self.browse_file()

    def browse_file(self):
        desktop_path = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", desktop_path)

        if self.file_path:
            self.ui.fileAdd.setText(f"Выбран файл: {self.file_path}")

    def get_folders(self):
        self.ui.recipientFile.clear()
        if not self.drive_service:
            self.drive_service = self.authenticate()

        if not self.drive_service:
            self.drive_service = self.authenticate()

        try:
            results = self.drive_service.files().list(
                q="mimeType='application/vnd.google-apps.folder'",
                spaces='drive',
                fields='nextPageToken, files(id, name)'
            ).execute()
        except Exception as e:
            print(f"An error occurred: {e}")
            return

        items = results.get('files', [])
        if not items:
            print('No folders found.')
        else:
            print('Folders:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
                self.ui.recipientFile.addItem(item['name'], item['id'])

    def upload_to_drive(self):
        if not self.drive_service:
            self.drive_service = self.authenticate()
        if not self.file_path:
            QMessageBox.warning(self, 'Внимание', 'Вы не выбрали файл')
            return

        folder_id = self.ui.recipientFile.currentData()
        if not folder_id:
            QMessageBox.warning(self, 'Внимание', 'Вы не выбрали папку')
            return

        media = MediaFileUpload(self.file_path)
        request = self.drive_service.files().create(
            media_body=media,
            body={
                'name': os.path.basename(self.file_path),  # Используйте имя файла, а не статическое имя
                'parents': [folder_id]
            }
        )
        request.execute()
        print(f"Файл успешно загружен в папку: {self.ui.recipientFile.currentText()}")
        self.ui.fileAdd.clear()

    def authenticate(self):
        SCOPES = ['https://www.googleapis.com/auth/drive']

        # Получаем абсолютный путь к текущему файлу
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Формируем путь к файлу credentials.json в другой подпапке
        credentials_path = os.path.join(current_dir, '..', 'Source', 'credentials.json')

        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
        creds = flow.run_local_server(port=0)

        return build('drive', 'v3', credentials=creds)

    def load_title_teams(self):
        self.ui.comboboxTitle.clear()
        connection = connect()
        cursor = connection.cursor()
        cursor.execute('SELECT team_id, name_team FROM "Teams"')
        teams = cursor.fetchall()
        for team in teams:
            self.ui.comboboxTitle.addItem(f"{team[1]}", userData=team[0])

    def load_titles_by_team(self):
        team_id = self.ui.comboboxTitle.currentData()
        search_text = self.ui.SearchEdit.text().strip()
        self.setup_scroll_area(team_id, search_text)

    def state_edit_button(self):
        selected_index = self.ui.tableListTask.currentIndex()
        if selected_index.isValid():
            self.ui.editListTask.clicked.connect(self.edit_task)
        else:
            self.ui.editListTask.setEnabled(False)


    def login_button_clicked(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        encrypted_login = self.encrypt_data(login)
        encrypted_password = self.encrypt_data(password)

        self.save_credentials(encrypted_login, encrypted_password)

        if self.check_credentials(login, password):
            self.ui.stackedWidget.setCurrentIndex(4)
        else:
            self.show_error_message("Неправильный логин/email или пароль")

    def check_credentials(self, login, password):
        connection = connect()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM "User" WHERE (login = %s OR email = %s) AND password = %s',
                       (login, login, password))
        user_exists = cursor.fetchone() is not None
        close_db_connect(connection, cursor)
        return user_exists

    def load_saved_credentials(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        if 'Account' in config:
            encrypted_login = config['Account']['username']
            encrypted_password = config['Account']['password']
            login = self.decrypt_data(encrypted_login)
            password = self.decrypt_data(encrypted_password)

            if self.check_credentials(login, password):
                self.ui.stackedWidget.setCurrentIndex(4)

    def save_credentials(self, encrypted_login, encrypted_password):
        config = configparser.ConfigParser()
        config['Account'] = {'username': encrypted_login, 'password': encrypted_password}

        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def generate_key(self):
        key_file = 'secret.key'
        if not os.path.exists(key_file):
            key = Fernet.generate_key()
            with open(key_file, 'wb') as keyfile:
                keyfile.write(key)

    def encrypt_data(self, data):
        with open('secret.key', 'rb') as keyfile:
            key = keyfile.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data.decode()

    def decrypt_data(self, encrypted_data):
        with open('secret.key', 'rb') as keyfile:
            key = keyfile.read()
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data.encode())
        return decrypted_data.decode()

    def load_edit_teams(self):
        self.ui.nameCrewTranslatorEditTitle.clear()
        try:
            connection = connect()
            cursor = connection.cursor()
            cursor.execute('SELECT team_id, name_team FROM "Teams"')
            teams = cursor.fetchall()
            for team in teams:
                self.ui.nameCrewTranslatorEditTitle.addItem(f"{team[1]}", userData=team[0])
            if teams:
                first_team_id = teams[0][0]
                index = self.ui.nameCrewTranslatorEditTitle.findData(first_team_id)
                if index != -1:
                    self.ui.nameCrewTranslatorEditTitle.setCurrentIndex(index)
        except Exception as e:
            print(f'Ошибка при загрузке пользователей для редактирования: {e}')

    def load_account_teams(self):
        self.ui.nameCrewAccComboBox.clear()
        self.ui.nameCrewAccComboBox.clear()
        connection = connect()
        cursor = connection.cursor()
        cursor.execute('SELECT team_id, name_team, bot_id, icon_team FROM "Teams"')
        teams = cursor.fetchall()
        for team in teams:
            self.ui.crewAddComboBox.addItem(f"{team[1]}", userData=team[0])
            self.ui.nameCrewAccComboBox.addItem(f"{team[1]}", userData=team[0])

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Сообщение об ошибке")
        msg.exec()

    def load_users(self):
        self.ui.employeeAddTask.clear()
        self.ui.userAddComboBox.clear()
        connection = connect()
        cursor = connection.cursor()
        cursor.execute('SELECT user_id, login, password FROM "User"')
        users = cursor.fetchall()
        for user in users:
            self.ui.userAddComboBox.addItem(f"{user[1]}", userData=user[0])
            self.ui.employeeAddTask.addItem(f"{user[1]}", userData=user[0])

    def load_edit_users(self):
        self.ui.employeeEditTask.clear()
        self.ui.userEditComboBox.clear()
        try:
            connection = connect()
            cursor = connection.cursor()
            cursor.execute('SELECT user_id, login, password FROM "User"')
            users = cursor.fetchall()
            for user in users:
                self.ui.employeeEditTask.addItem(f"{user[1]}", userData=user[0])
                self.ui.userEditComboBox.addItem(f"{user[1]}", userData=user[0])
            if users:
                first_user_id = users[0][0]
                index = self.ui.employeeEditTask.findData(first_user_id)
                index_new = self.ui.userEditComboBox.findData(first_user_id)
                if index != -1:
                    self.ui.employeeEditTask.setCurrentIndex(index)
                if index_new != -1:
                    self.ui.userEditComboBox.setCurrentIndex(index_new)

        except Exception as e:
            print(f'Ошибка при загрузке пользователей для редактирования: {e}')

    def apply_task(self):
        user_id = self.ui.employeeAddTask.currentData()
        task_text = self.ui.taskEditAdd.toPlainText()
        date = self.ui.dateEdit.date().toString("yyyy-MM-dd")

        if not task_text:
            self.show_error_message("Вы не заполнили задачу! Пожалуйста повторите попытку!")
            return

        connection = connect()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO "Task" (date, task_text) VALUES (%s, %s) RETURNING task_id', (date, task_text))
        task_id = cursor.fetchone()[0]

        cursor.execute(
            'INSERT INTO "User_task" (user_id, task_id) OVERRIDING SYSTEM VALUE VALUES (%s, %s) RETURNING user_task_id',
            (user_id, task_id))
        connection.commit()

        self.ui.employeeAddTask.clear()
        self.ui.taskEditAdd.clear()
        self.load_users()
        self.get_data()
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageListTask)

    def update_task(self):
        selected_index = self.ui.tableListTask.currentIndex()
        if not selected_index.isValid():
            return

        task_id = int(self.model_table_task.item(selected_index.row(), 3).data(Qt.UserRole))
        updated_task_text = self.ui.taskEditChange.toPlainText()
        updated_date = self.ui.dateEditEditTask.date().toString("yyyy-MM-dd")
        updated_user_id = self.ui.employeeEditTask.currentData()

        if not updated_task_text:
            self.show_error_message("Вы не заполнили задачу! Пожалуйста повторите попытку!")
            return

        try:
            with self.connection.cursor() as cursor:
                connection = connect()
                cursor = connection.cursor()
                cursor.execute('UPDATE "Task" SET task_text = %s, date = %s WHERE task_id = %s',
                               (updated_task_text, updated_date, task_id))

                cursor.execute('UPDATE "User_task" SET user_id = %s WHERE task_id = %s',
                               (updated_user_id, task_id))

            connection.commit()
            self.get_data()
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageListTask)

        except Exception as e:
            print(f'Ошибка при обновлении задачи: {e}')

    def view_task(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageUserView)
        selected_index = self.ui.tableListTask.currentIndex()
        if not selected_index.isValid():
            return

        task_id = int(self.model_table_task.item(selected_index.row(), 3).data(Qt.UserRole))

        try:
            connection = connect()
            with self.connection.cursor() as cursor:
                cursor.execute('''
                    SELECT t.task_text, t.date
                    FROM "Task" t
                    WHERE t.task_id = %s
                ''', (task_id,))
                task_details = cursor.fetchone()

                if task_details:
                    task_text = task_details[0]
                    date = task_details[1].strftime("%Y-%m-%d")

                    self.ui.taskEditView.setPlainText(task_text)
                    self.ui.dateEditView.setDate(QDate.fromString(date, "yyyy-MM-dd"))

        except Exception as e:
            print(f'Ошибка при выводе задач: {e}')

    def edit_task(self):
        self.ui.tableListTask.clearSelection()
        selected_index = self.ui.tableListTask.currentIndex()
        if not selected_index.isValid():
            return

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageEditTask)
        task_id = int(self.model_table_task.item(selected_index.row(), 3).data(Qt.UserRole))

        try:
            connection = connect()
            with self.connection.cursor() as cursor:
                cursor.execute('''
                    SELECT t.task_text, t.date, ut.user_id
                    FROM "Task" t
                    INNER JOIN "User_task" ut ON t.task_id = ut.task_id
                    WHERE t.task_id = %s
                ''', (task_id,))
                task_details = cursor.fetchone()

                if task_details:
                    task_text = task_details[0]
                    date = task_details[1].strftime("%Y-%m-%d")
                    user_id = task_details[2]

                    self.ui.taskEditChange.setPlainText(task_text)
                    self.ui.dateEditEditTask.setDate(QDate.fromString(date, "yyyy-MM-dd"))

                    index = self.ui.employeeEditTask.findData(user_id)
                    if index != -1:
                        self.ui.employeeEditTask.setCurrentIndex(index)
                    self.ui.tableListTask.clearSelection()

        except Exception as e:
            print(f'Ошибка при заполнении задач: {e}')

    def get_data(self):
        try:
            selected_date = self.ui.dateEdit.date().toString("yyyy-MM-dd")
            connection = connect()
            with self.connection.cursor() as cursor:
                cursor.execute('''
                    SELECT u.login, t.task_text, t.date, t.task_id
                    FROM "User_task" ut
                    INNER JOIN "User" u ON ut.user_id = u.user_id
                    INNER JOIN "Task" t ON ut.task_id = t.task_id
                    WHERE t.date = %s
                    ORDER BY ut.user_task_id;
                ''', (selected_date,))
                records = cursor.fetchall()

                self.model_table_task.clear()
                self.model_table_task.setColumnCount(3)
                self.model_table_task.setHorizontalHeaderLabels(['Пользователь', 'Задача', 'Дата'])

                for record in records:
                    row = [QStandardItem(str(value)) for value in record[:3]]
                    task_id_item = QStandardItem()
                    task_id_item.setData(record[3], Qt.UserRole)
                    row.append(task_id_item)

                    self.model_table_task.appendRow(row)
                self.ui.tableListTask.resizeColumnsToContents()

                header = self.ui.tableListTask.horizontalHeader()
                header.setSectionResizeMode(QHeaderView.Stretch)

                self.ui.tableListTask.setColumnHidden(3, True)

        except Exception as e:
            print(f'Ошибка при выводе: {e}')

    def delete_selected_task(self):
        selected_index = self.ui.tableListTask.currentIndex()
        if not selected_index.isValid():
            return
        try:
            task_id = int(self.model_table_task.item(selected_index.row(), 3).data(Qt.UserRole))
            connection = connect()
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM "Task" WHERE task_id = %s', (task_id,))
            connection.commit()
            self.get_data()
        except Exception as e:
            print(f'Ошибка при удалении задач: {e}')

    def load_team(self):
        self.ui.crewAddComboBox.clear()
        self.ui.crewComboBox.clear()
        self.ui.nameCrewTranslatorAddTitle.clear()
        connection = connect()
        cursor = connection.cursor()
        cursor.execute('SELECT team_id, name_team, bot_id, icon_team FROM "Teams"')
        teams = cursor.fetchall()
        for team in teams:
            self.ui.crewAddComboBox.addItem(f"{team[1]}", userData=team[0])
            self.ui.crewComboBox.addItem(f"{team[1]}", userData=team[0])
            self.ui.nameCrewTranslatorAddTitle.addItem(f"{team[1]}", userData=team[0])


    def load_title_income(self):
        self.ui.titleAddComboBox.clear()
        connection = connect()
        cursor = connection.cursor()
        cursor.execute('SELECT title_id, title_name FROM "Title"')
        titles = cursor.fetchall()
        for title in titles:
            self.ui.titleAddComboBox.addItem(f"{title[1]}", userData=title[0])

    def load_edit_team_income(self):
        self.ui.crewEditComboBox.clear()
        try:
            connection = connect()
            cursor = connection.cursor()
            cursor.execute('SELECT team_id, name_team, bot_id, icon_team FROM "Teams"')
            teams = cursor.fetchall()
            for team in teams:
                self.ui.crewEditComboBox.addItem(f"{team[1]}", userData=team[0])
            if teams:
                first_team_id = teams[0][0]
                index = self.ui.crewEditComboBox.findData(first_team_id)
                if index != -1:
                    self.ui.crewEditComboBox.setCurrentIndex(index)

        except Exception as e:
            print(f'Ошибка при загрузке команд для редактирования: {e}')

    def load_edit_title_income(self):
        self.ui.titleEditcomboBox.clear()
        try:
            connection = connect()
            cursor = connection.cursor()
            cursor.execute('SELECT title_id, title_name FROM "Title"')
            titles = cursor.fetchall()
            for title in titles:
                self.ui.titleEditcomboBox.addItem(f"{title[1]}", userData=title[0])
            if titles:
                first_title_id = titles[0][0]
                index = self.ui.titleEditcomboBox.findData(first_title_id)
                if index != -1:
                    self.ui.titleEditcomboBox.setCurrentIndex(index)

        except Exception as e:
            print(f'Ошибка при загрузке команд для редактирования: {e}')

    def apply_income(self):
        team_id = self.ui.crewAddComboBox.currentData()
        user_id = self.ui.userAddComboBox.currentData()
        title_id = self.ui.titleAddComboBox.currentData()
        chapter = self.ui.nameChapterAddIncome.text()
        money = self.ui.salaryAddIncome.text()

        if not money or not chapter:
            self.show_error_message("Вы не заполнили поля! Пожалуйста повторите попытку!")
            return

        connection = connect()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO "Income" (user_id, team_id, money, chapter, title_id) VALUES (%s, %s, %s, %s, %s) '
                       'RETURNING income_id', (user_id, team_id, money, chapter, title_id))
        income_id = cursor.fetchone()[0]
        connection.commit()

        self.ui.nameChapterAddIncome.clear()
        self.ui.salaryAddIncome.clear()
        self.load_users()
        self.load_title_income()
        self.load_team()
        self.get_income()
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageIncome)

    def get_income(self):
        try:
            total_income = 0
            selected_team = self.ui.crewComboBox.currentData()
            connection = connect()
            with self.connection.cursor() as cursor:
                cursor.execute('''
                    SELECT t.name_team, u.login, tl.title_name, ic.chapter, ic.money, ic.income_id
                    FROM "Income" ic
                    INNER JOIN "User" u ON ic.user_id = u.user_id
                    INNER JOIN "Teams" t ON ic.team_id = t.team_id
                    INNER JOIN "Title" tl ON ic.title_id = tl.title_id
                    WHERE ic.team_id = %s
                    ORDER BY ic.income_id;
                ''', (selected_team,))
                records = cursor.fetchall()

                self.model_table_income.clear()
                self.model_table_income.setColumnCount(5)
                self.model_table_income.setHorizontalHeaderLabels(
                    ['Команда', 'Пользователь', 'Наименование тайтла', 'Наименование главы', 'Заработок'])

                for record in records:
                    row = [QStandardItem(str(value)) for value in record[:5]]
                    income_id_item = QStandardItem()
                    income_id_item.setData(record[5], Qt.UserRole)
                    row.append(income_id_item)
                    total_income += record[4]

                    self.model_table_income.appendRow(row)
                self.ui.tableIncome.resizeColumnsToContents()

                header = self.ui.tableIncome.horizontalHeader()
                header.setSectionResizeMode(QHeaderView.Stretch)

                self.ui.tableIncome.setColumnHidden(5, True)
                self.ui.totalIncomeEdit.setText(str(total_income))

        except Exception as e:
            print(f'Ошибка: {e}')

    def edit_income(self):

        selected_index = self.ui.tableIncome.currentIndex()
        if not selected_index.isValid():
            return


        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageEditIncome)
        income_id = int(self.model_table_income.item(selected_index.row(), 5).data(Qt.UserRole))

        try:
            connection = connect()
            with self.connection.cursor() as cursor:
                cursor.execute('''
                    SELECT t.team_id, u.user_id, tl.title_id, ic.chapter, ic.money, ic.income_id
                    FROM "Income" ic
                    INNER JOIN "User" u ON ic.user_id = u.user_id
                    INNER JOIN "Teams" t ON ic.team_id = t.team_id
                    INNER JOIN "Title" tl ON ic.title_id = tl.title_id
                    WHERE ic.income_id = %s
                    ORDER BY ic.income_id;
                ''', (income_id,))
                income_details = cursor.fetchone()

                if income_details:
                    team_id = income_details[0]
                    user_id = income_details[1]
                    title_id = income_details[2]
                    chapter = income_details[3]
                    money = income_details[4]

                    self.ui.crewEditComboBox.currentData(team_id)
                    self.ui.userEditComboBox.currentData(user_id)
                    self.ui.titleEditcomboBox.currentData(title_id)
                    self.ui.nameChapterEditIncome.setText(chapter)
                    self.ui.salaryEditIncome.setText(str(money))

                    index_one = self.ui.crewEditComboBox.findData(team_id)
                    if index_one != -1:
                        self.ui.crewEditComboBox.setCurrentIndex(index_one)

                    index_two = self.ui.userEditComboBox.findData(user_id)
                    if index_two != -1:
                        self.ui.userEditComboBox.setCurrentIndex(index_two)

                    index_three = self.ui.titleEditcomboBox.findData(title_id)
                    if index_three != -1:
                        self.ui.titleEditcomboBox.setCurrentIndex(index_three)


        except Exception as e:
            print(f'Ошибка при заполнении задач3: {e}')

    def update_income(self):
        selected_index = self.ui.tableIncome.currentIndex()
        if not selected_index.isValid():
            return

        income_id = int(self.model_table_income.item(selected_index.row(), 5).data(Qt.UserRole))

        edit_team_id = self.ui.crewEditComboBox.currentData()
        edit_user_id = self.ui.userEditComboBox.currentData()
        edit_title_id = self.ui.titleEditcomboBox.currentData()
        edit_chapter = self.ui.nameChapterEditIncome.text()
        edit_money = self.ui.salaryEditIncome.text()

        if not edit_chapter or not edit_money:
            self.show_error_message("Вы не заполнили поля! Пожалуйста повторите попытку!")
            return

        try:
            with self.connection.cursor() as cursor:
                connection = connect()
                cursor = connection.cursor()
                cursor.execute(
                    'UPDATE "Income" SET user_id = %s, team_id = %s, money = %s, chapter = %s, title_id = %s '
                    'WHERE income_id = %s',
                    (edit_user_id, edit_team_id, edit_money, edit_chapter, edit_title_id, income_id))
                connection.commit()

            self.get_income()
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageIncome)

        except Exception as e:
            print(f'Ошибка4: {e}')

    def delete_selected_income(self):
        selected_index = self.ui.tableIncome.currentIndex()
        if not selected_index.isValid():
            return
        try:
            income_id = int(self.model_table_income.item(selected_index.row(), 5).data(Qt.UserRole))
            connection = connect()
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM "Income" WHERE income_id = %s', (income_id,))
            connection.commit()
            self.get_income()
        except Exception as e:
            print(f'Ошибка при удалении задач: {e}')

    def on_text_edit_changed(self):
        text = self.ui.textEdit.toPlainText()
        selected_text = self.ui.textEdit.textCursor().selectedText()
        if selected_text == text:
            self.ui.textEdit_2.clear()

    def init_translator_ui(self):
        self.ui.textEdit.textChanged.connect(self.start_timer)
        self.ui.comboBox.currentIndexChanged.connect(self.translate_text)
        self.ui.comboBox_2.currentIndexChanged.connect(self.translate_text)

    def start_timer(self):
        self.translation_timer.stop()
        self.translation_timer.start(self.translation_delay)

    def translate_text(self):
        text_to_translate = self.ui.textEdit.toPlainText().strip()
        selected_src_lang = self.ui.comboBox.currentText()
        selected_dest_lang = self.ui.comboBox_2.currentText()

        if not text_to_translate or selected_src_lang == "Выберите язык" or selected_dest_lang == "Выберите язык":
            return

        lang_dict = {
            "Английский": "en",
            "Русский": "ru",
            "Корейский": "ko",
            "Японский": "ja",
        }

        src_lang = lang_dict.get(selected_src_lang)
        dest_lang = lang_dict.get(selected_dest_lang)

        if src_lang and dest_lang:
            try:
                translator = Translator()
                translation = translator.translate(text_to_translate, src=src_lang, dest=dest_lang)
                translated_text = translation.text
                self.ui.textEdit_2.setPlainText(translated_text)
            except Exception as e:
                print("Ошибка при переводе текста:", e)
        else:
            print("Ошибка: Один из выбранных языков не распознается.")

    def setup_scroll_area(self, team_id=None, search_text=None):
        # Убедитесь, что image_scroll_area является атрибутом вашего класса
        self.image_scroll_area = ImageScrollArea(team_id=team_id, search_text=search_text)
        self.ui.titleGrid.addWidget(self.image_scroll_area, 0, 0)

        for child_widget in self.image_scroll_area.findChildren(RoundedImageLabel):
            child_widget.mousePressEvent = lambda event, widget=child_widget: self.open_desc_page(event, widget)

    def open_desc_page(self, event, widget):
        if event.button() == Qt.LeftButton:
            self.clicked_widget = widget
            self.update_photo_desc()
            self.title_id = widget.title_id
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageDesc)

    def load_description(self, index):
        if index == self.ui.stackedWidget_2.indexOf(self.ui.pageDesc):
            connection = connect()
            cursor = connection.cursor()
            cursor.execute('SELECT description FROM "Title" WHERE title_id = %s', (self.title_id,))
            row = cursor.fetchone()
            close_db_connect(connection, cursor)

            if row:
                description = row[0]
                self.ui.textEditDesc.setPlainText(description)
            else:
                self.ui.textEditDesc.clear()

    def delete_title(self):
        title_id = self.title_id

        connection = connect()
        cursor = connection.cursor()

        try:
            cursor.execute('DELETE FROM "Title" WHERE title_id = %s', (title_id,))
            connection.commit()
        except psycopg2.Error as e:
            connection.rollback()
            print("Ошибка при удалении тайтла:", e)
        finally:
            close_db_connect(connection, cursor)

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageTitle)
        self.load_titles_by_team()

    def open_edit_title_page(self):
        connection = connect()
        cursor = connection.cursor()
        cursor.execute('SELECT title_name, description, team_id, title_date FROM "Title" WHERE title_id = %s', (self.title_id,))
        row = cursor.fetchone()
        close_db_connect(connection, cursor)

        if row:
            title_name, title_description, team_id, title_date  = row
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageEditTitle)
            self.ui.nameEditTitle.setText(title_name)
            self.ui.descriptionEdit_2.setText(title_description)
            self.ui.dateReleaseEditTitle.setDate(title_date)

            index = self.ui.nameCrewTranslatorEditTitle.findData(team_id)
            if index != -1:
                self.ui.nameCrewTranslatorEditTitle.setCurrentIndex(index)


    def switch_to_page_desc(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageDesc)

    def fractal_compress(self, image, scale=2):
        height, width = image.shape[:2]
        compressed_height = height // scale if height % scale == 0 else height // scale + 1
        compressed_width = width // scale if width % scale == 0 else width // scale + 1
        compressed_image = cv2.resize(image, (compressed_width, compressed_height), interpolation=cv2.INTER_AREA)

        start_time = time.time()  # Засекаем начало сжатия

        for y in range(0, height, scale):
            for x in range(0, width, scale):
                block = image[y:min(y + scale, height), x:min(x + scale, width)]

                # Применяем интерполяцию INTER_AREA
                block = cv2.resize(block, (1, 1), interpolation=cv2.INTER_AREA)
                compressed_image[y // scale, x // scale] = block[0, 0]

        end_time = time.time()  # Засекаем окончание сжатия
        compression_time = end_time - start_time  # Вычисляем время сжатия

        return compressed_image, compression_time

    def load_image(self, path):
        try:
            with Image.open(path) as img:
                # Преобразуем изображение в RGB, если оно не в этом формате
                img = img.convert('RGB')
                img_np = np.array(img)
                # Преобразуем цветовое пространство из RGB в BGR для OpenCV
                img_np_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
            return img_np_bgr
        except Exception as e:
            print(f"Error loading image from '{path}': {e}")
            return None

    def apply_title_changes(self):
        team_id = self.ui.nameCrewTranslatorEditTitle.currentData()
        new_title_name = self.ui.nameEditTitle.text()
        new_description = self.ui.descriptionEdit_2.toPlainText()
        selected_date = self.ui.dateReleaseEditTitle.date()
        release_date = selected_date.toPython()

        # Получаем путь к изображению
        image_path = self.ui.imageAreaEdit.toPlainText()

        if not new_title_name:
            self.ui.nameEditTitle.setPlaceholderText('Вы не написали название тайтла.')
            self.ui.nameEditTitle.setStyleSheet("placeholder-text-color: red;")
        else:
            self.ui.nameEditTitle.setPlaceholderText('')

        if not new_description:
            self.ui.descriptionEdit_2.setPlaceholderText('Вы не написали описание.')
            self.ui.descriptionEdit_2.setStyleSheet("placeholder-text-color: red;")
        else:
            self.ui.descriptionEdit_2.setPlaceholderText('')

        # Установка таймера на 5 секунд для сброса стилей и текстовых подсказок
        timer = QTimer(self)
        timer.singleShot(5000, self.reset_input_edit_fields)

        if image_path:
            # Загружаем изображение
            original_image = self.load_image(image_path)

            if original_image is not None and new_title_name and new_description:
                # Сжимаем изображение
                compressed_image, _ = self.fractal_compress(original_image)

                # Преобразуем сжатое изображение в байтовый массив
                buffer = BytesIO()
                buffer.write(cv2.imencode('.jpg', compressed_image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])[1])
                image_data = buffer.getvalue()
            else:
                print("Ошибка загрузки изображения.")
                return
        else:
            image_data = None

        connection = connect()
        cursor = connection.cursor()
        if new_title_name and new_description is not None:
            if image_data is not None:
                cursor.execute(
                    'UPDATE "Title" SET title_name = %s, description = %s, icon_title = %s, team_id = %s, title_date = %s WHERE title_id = %s',
                    (new_title_name, new_description, psycopg2.Binary(image_data), team_id, release_date, self.title_id))
            else:
                cursor.execute(
                    'UPDATE "Title" SET title_name = %s, description = %s, team_id = %s, title_date = %s WHERE title_id = %s',
                    (new_title_name, new_description, team_id, release_date, self.title_id))
        else:
            return
        connection.commit()
        close_db_connect(connection, cursor)

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageTitle)
        self.ui.imageAreaEdit.clear()
        self.load_titles_by_team()

    def reset_input_edit_fields(self):
        # Сброс стилей и текстовых подсказок полей ввода
        self.ui.imageAreaEdit.setPlaceholderText('Нажмите два раза для добавления изображения')
        self.ui.imageAreaEdit.setStyleSheet("placeholder-text-color: #FFFFFF")  # Сброс стилей
        self.ui.nameEditTitle.setPlaceholderText('')
        self.ui.descriptionEdit_2.setPlaceholderText('')

    def open_image_dialog(self, event):
        # Получаем путь к рабочему столу
        desktop_path = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)

        # Открываем диалог выбора файла, начиная с рабочего стола
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", desktop_path,
                                                   "Images (*.png *.jpg *.jpeg)", options=options)
        if file_path:
            self.ui.imageAreaEdit.setText(file_path)

    def open_image_dialog_add_title(self, event):
        # Получаем путь к рабочему столу
        desktop_path = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)

        # Открываем диалог выбора файла, начиная с рабочего стола
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", desktop_path,
                                                   "Images (*.png *.jpg *.jpeg)", options=options)
        if file_path:
            self.ui.imageArea.setText(file_path)


    def open_file_explorer(self):
        # Получаем путь к рабочему столу
        desktop_path = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)

        # Открываем диалог выбора файла, начиная с рабочего стола
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", desktop_path,
                                                   "Images (*.png *.jpg *.jpeg)", options=options)
        if file_path:
            self.ui.imageAreaEdit.setText(file_path)
            self.set_image_to_label(file_path)

    def rounded_pixmap(self, pixmap):
        rounded_pixmap = QPixmap(pixmap.size())
        rounded_pixmap.fill(Qt.transparent)
        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.white)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(pixmap.rect(), 10, 10)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.drawPixmap(10, 10, pixmap)
        painter.end()
        return rounded_pixmap

    def set_image_to_label(self, image_path):
        # Загрузка изображения
        pixmap = QPixmap(image_path)

        # Применение стилей к QLabel (self.ui.label_37)
        self.ui.label_37.setContentsMargins(10, 10, 10, 10)  # Установка отступов

        # Установка изображения с закругленными углами
        rounded_pixmap = self.rounded_pixmap(pixmap)
        self.ui.label_37.setPixmap(rounded_pixmap)
        self.ui.label_37.setScaledContents(True)  # Разрешение масштабирования содержимого QLabel

    def add_logo_button_clicked(self):
        self.open_file_explorer()

    def add_title_to_database(self):
        comboBox_team = self.ui.nameCrewTranslatorAddTitle.currentData()
        title_name = self.ui.nameAddTitle.text()
        title_description = self.ui.descriptionEdit.toPlainText()
        image_path = self.ui.imageArea.toPlainText()
        selected_date = self.ui.dateReleaseAddTitle.date()
        release_date = selected_date.toPython()

        if not image_path:
            self.ui.imageArea.setPlaceholderText('Вы не выбрали изображение.')
            self.ui.imageArea.setStyleSheet("placeholder-text-color: red;")
        if not title_name:
            self.ui.nameAddTitle.setPlaceholderText('Вы не написали название тайтла.')
            self.ui.nameAddTitle.setStyleSheet("placeholder-text-color: red;")
        if not title_description:
            self.ui.descriptionEdit.setPlaceholderText('Вы не написали описание.')
            self.ui.descriptionEdit.setStyleSheet("placeholder-text-color: red;")

        # Установка таймера на 5 секунд для сброса стилей и текстовых подсказок
        timer = QTimer(self)
        timer.singleShot(5000, self.reset_input_fields)


        # Загружаем и сжимаем изображение
        original_image = self.load_image(image_path)
        # Check if original_image is valid
        if original_image is not None and title_name and title_description is not None:
            # Continue with image processing and database insertion
            compressed_image, _ = self.fractal_compress(original_image)
            buffer = BytesIO()
            buffer.write(cv2.imencode('.jpg', compressed_image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])[1])
            image_data = buffer.getvalue()
        else:
            print("Ошибка загрузки изображения или отсутствует название/описание.")
            return

        connection = connect()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO "Title" (title_name, description, icon_title, team_id, title_date) '
                       'VALUES (%s, %s, %s, %s, %s)',
                       (title_name, title_description, psycopg2.Binary(image_data), comboBox_team, release_date))
        connection.commit()
        cursor.close()
        connection.close()

        # Очистка полей ввода после вставки
        self.ui.dateReleaseAddTitle.setDate(QDate.currentDate())
        self.ui.nameAddTitle.clear()
        self.ui.descriptionEdit.clear()
        self.ui.imageArea.clear()
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageTitle)
        self.load_titles_by_team()
        self.load_team()

    def reset_input_fields(self):
        # Сброс стилей и текстовых подсказок полей ввода
        self.ui.imageArea.setPlaceholderText('Нажмите два раза для добавления изображения')
        self.ui.imageArea.setStyleSheet("placeholder-text-color: #FFFFFF")  # Сброс стилей
        self.ui.nameAddTitle.setPlaceholderText('')
        self.ui.descriptionEdit.setPlaceholderText('')

    def setup_calender_widget(self):
        calender = Calender(self.ui)
        self.ui.widgetCalender.setLayout(QVBoxLayout())
        self.ui.widgetCalender.layout().addWidget(calender)

    def toggle_full_menu(self):
        if self.ui.fullMenu.isHidden():
            self.ui.fullMenu.show()
            self.ui.icon.hide()
        else:
            self.ui.fullMenu.hide()
            self.ui.icon.show()

    def update_photo_desc(self):
        if hasattr(self, 'clicked_widget'):
            pixmap = self.clicked_widget.pixmap()
            rounded_pixmap = self.clicked_widget.rounded_pixmap(pixmap)
            self.ui.photoDesc.setPixmap(rounded_pixmap)

    def mouseDoubleClickEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            pos = event.globalPosition().toPoint()
            if self.ui.widget_2.rect().contains(self.ui.widget_2.mapFromGlobal(pos)):
                self.toggle_screen_state()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.HoverMove:
            pos = event.globalPosition().toPoint()
            frame_geometry = self.frameGeometry()
            left_edge = abs(pos.x() - frame_geometry.left()) <= 5
            right_edge = abs(pos.x() - frame_geometry.right()) <= 5
            top_edge = abs(pos.y() - frame_geometry.top()) <= 5
            bottom_edge = abs(pos.y() - frame_geometry.bottom()) <= 5

            if left_edge or right_edge or top_edge or bottom_edge:
                if left_edge:
                    if top_edge:
                        self.current_cursor = Qt.SizeFDiagCursor
                    elif bottom_edge:
                        self.current_cursor = Qt.SizeBDiagCursor
                    else:
                        self.current_cursor = Qt.SizeHorCursor
                elif right_edge:
                    if top_edge:
                        self.current_cursor = Qt.SizeBDiagCursor
                    elif bottom_edge:
                        self.current_cursor = Qt.SizeFDiagCursor
                    else:
                        self.current_cursor = Qt.SizeHorCursor
                elif top_edge or bottom_edge:
                    self.current_cursor = Qt.SizeVerCursor
            else:
                # Если не на боковых сторонах, оставляем курсор Open Hand
                self.current_cursor = self.open_hand_cursor

            # Устанавливаем текущий курсор
            self.setCursor(self.current_cursor)

        return super().eventFilter(obj, event)

    def closeApp(self):
        self.close()

    def minimizeApp(self):
        self.showMinimized()

    def toggle_screen_state(self):
        start_geometry = self.geometry()
        if not self.screen_expanded:
            end_geometry = QApplication.primaryScreen().availableGeometry()
            self.normal_geometry = start_geometry  # Обновляем сохраненную геометрию
        else:
            end_geometry = self.normal_geometry  # Восстанавливаем начальную геометрию
        if start_geometry == end_geometry:
            start_geometry, end_geometry = end_geometry, self.normal_geometry

        self.animation.setStartValue(start_geometry)
        self.animation.setEndValue(end_geometry)
        self.animation.finished.connect(self.on_animation_finished)  # Связываем обработчик события завершения анимации
        self.animation.start()

        self.screen_expanded = not self.screen_expanded

    def on_animation_finished(self):
        if not self.screen_expanded:
            self.setGeometry(self.normal_geometry)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            pos = event.globalPosition().toPoint()
            frame_geometry = self.frameGeometry()
            left_edge = abs(pos.x() - frame_geometry.left()) <= 5
            right_edge = abs(pos.x() - frame_geometry.right()) <= 5
            top_edge = abs(pos.y() - frame_geometry.top()) <= 5
            bottom_edge = abs(pos.y() - frame_geometry.bottom()) <= 5

            if left_edge or right_edge or top_edge or bottom_edge:
                self.mouse_press_position = pos
                self.resize_offset = pos

                if left_edge:
                    if top_edge:
                        self.resize_direction = "top_left"
                    elif bottom_edge:
                        self.resize_direction = "bottom_left"
                    else:
                        self.resize_direction = "left"
                elif right_edge:
                    if top_edge:
                        self.resize_direction = "top_right"
                    elif bottom_edge:
                        self.resize_direction = "bottom_right"
                    else:
                        self.resize_direction = "right"
                elif top_edge:
                    self.resize_direction = "top"
                elif bottom_edge:
                    self.resize_direction = "bottom"

            elif self.ui.widget_2.rect().contains(self.ui.widget_2.mapFromGlobal(pos)):
                self.drag_position = pos - frame_geometry.topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            pos = event.globalPosition().toPoint()
            if self.drag_position is not None:
                self.move(pos - self.drag_position)
            elif self.resize_direction is not None:
                frame_geometry = self.frameGeometry()
                new_geometry = frame_geometry

                if "left" in self.resize_direction:
                    new_geometry.setLeft(pos.x())
                    if new_geometry.width() < self.minimumWidth():
                        new_geometry.setLeft(frame_geometry.right() - self.minimumWidth())
                elif "right" in self.resize_direction:
                    new_geometry.setRight(pos.x())
                    if new_geometry.width() < self.minimumWidth():
                        new_geometry.setRight(frame_geometry.left() + self.minimumWidth())
                if "top" in self.resize_direction:
                    new_geometry.setTop(pos.y())
                    if new_geometry.height() < self.minimumHeight():
                        new_geometry.setTop(frame_geometry.bottom() - self.minimumHeight())
                elif "bottom" in self.resize_direction:
                    new_geometry.setBottom(pos.y())
                    if new_geometry.height() < self.minimumHeight():
                        new_geometry.setBottom(frame_geometry.top() + self.minimumHeight())

                self.setGeometry(new_geometry)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = None
            self.resize_direction = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    window = MainWindow()
    window.show()
    # window.post_init()
    sys.exit(app.exec())
