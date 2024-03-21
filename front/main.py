import sys
import os

from PySide6.QtCore import (Qt, QPoint, QPropertyAnimation, QEasingCurve, QEvent, QDate, QByteArray, QBuffer, QIODevice,
                            QTimer)
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea, QHBoxLayout,
                               QGridLayout, QPushButton, QFileDialog, QHeaderView)
from PySide6.QtGui import QPixmap, QPainter, QCursor, QPalette, QColor, QStandardItemModel, QStandardItem

from googletrans import Translator
from datetime import datetime
from functools import partial
from ui import Ui_MainWindow
from database import connect, close_db_connect

import psycopg2
import itertools

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
    def __init__(self, parent=None):
        super().__init__(parent)
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

        self.load_images_from_database()

        self.scrollLayout.addStretch()
        self.scroll.setWidget(self.scrollContent)
        self.scroll_area_contents_layout.addWidget(self.scroll)

    def load_images_from_database(self):
        # Удаляем все дочерние виджеты из scrollLayout
        while self.scrollLayout.count():
            widget = self.scrollLayout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        connection = connect()
        cursor = connection.cursor()
        cursor.execute('SELECT "title_name", "icon_title", "title_id" FROM "Title" ORDER BY "title_id" ASC')
        rows = cursor.fetchall()

        images_per_row = 5
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
            pixmap = pixmap.scaled(250, 380, Qt.IgnoreAspectRatio)

            if not pixmap.isNull():
                label.setPixmap(pixmap)
            else:
                label.setText("Image not found")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("border: none")
            image_text_layout.addWidget(label)

            text_label = QLabel(row[0])  # Используем текст из базы данных
            image_text_layout.addWidget(text_label)
            text_label.setStyleSheet('color: #fff; border: none; margin-top: 2px; font: 14pt "Inter";')
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
        self.ui.stackedWidget.setCurrentIndex(4)
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
        self.ui.socialNetworksBtn_1.setToolTip("Соц. сети")
        self.ui.fileSharingBtn_1.setToolTip("Обмен файлами")
        self.ui.acceptFileBtn_1.setToolTip("Принять файлы")
        self.ui.accountBtn_1.setToolTip("Аккаунт")
        self.ui.translateBtn_1.setToolTip("Переводчик")
        self.ui.aboutUs_1.setToolTip("О нас")

        self.normal_geometry = None

        page_buttons = [
            (self.ui.incomeBtn_1, self.ui.incomeBtn_2, self.ui.pageIncome),
            (self.ui.titleBtn_1, self.ui.titleBtn_2, self.ui.pageTitle),
            (self.ui.scheduleBtn_1, self.ui.scheduleBtn_2, self.ui.pageSchedule),
            (self.ui.socialNetworksBtn_1, self.ui.socialNetworksBtn_2, self.ui.pageSocialNetwork),
            (self.ui.fileSharingBtn_1, self.ui.fileSharingBtn_2, self.ui.pageFileSharing),
            (self.ui.accountBtn_1, self.ui.accountBtn_2, self.ui.pageAccount),
            (self.ui.aboutUs_1, self.ui.aboutUs_2, self.ui.pageAboutUs),
            (self.ui.acceptFileBtn_1, self.ui.acceptFileBtn_2, self.ui.pageReceiveFile),
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
            (self.ui.editListTask, self.ui.pageEditTask),
            (self.ui.backApplyTaskBtn, self.ui.pageListTask)
        ]

        for button, page in move_buttons:
            button.clicked.connect(partial(self.ui.stackedWidget_2.setCurrentWidget, page))

        self.ui.closeBtn.clicked.connect(self.closeApp)
        self.ui.expandBtn.clicked.connect(self.toggle_screen_state)
        self.ui.minimazeBtn.clicked.connect(self.minimizeApp)
        self.ui.taskAddBtn.clicked.connect(self.apply_task)
        self.screen_expanded = False

        # Установка фильтра событий для главного окна
        open_hand_px_path = os.path.join(directory, 'Photo', 'free-icon-cursor-5340828.png')
        self.open_hand_px = QPixmap(open_hand_px_path)
        self.scaled_open_hand_px = self.open_hand_px.scaled(16, 16)
        self.scaled_open_hand_px.setMask(self.scaled_open_hand_px.mask())
        self.open_hand_cursor = QCursor(self.scaled_open_hand_px, 0, 0)
        self.setCursor(self.open_hand_cursor)
        self.current_cursor = self.open_hand_cursor

        self.installEventFilter(self)
        self.setup_scroll_area()
        self.setup_calender_widget()
        self.get_data()

        self.translation_delay = 1000
        self.translation_timer = QTimer()
        self.translation_timer.setSingleShot(True)
        self.translation_timer.timeout.connect(self.translate_text)
        self.init_translator_ui()
        self.ui.textEdit.textChanged.connect(self.on_text_edit_changed)
        self.ui.deleteListTask.clicked.connect(self.delete_selected_task)
        self.ui.editListTask.clicked.connect(self.edit_task)
        self.ui.taskApplyBtn.clicked.connect(self.update_task)

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

        self.load_users()
        self.get_data()
        self.load_edit_users()

    def load_users(self):
        self.ui.employeeAddTask.clear()
        connection = connect()
        cursor = connection.cursor()
        cursor.execute('SELECT user_id, login, password FROM "User"')
        users = cursor.fetchall()
        for user in users:
            self.ui.employeeAddTask.addItem(f"{user[1]}", userData=user[0])

    def load_edit_users(self):
        self.ui.employeeEditTask.clear()
        try:
            connection = connect()
            cursor = connection.cursor()
            cursor.execute('SELECT user_id, login, password FROM "User"')
            users = cursor.fetchall()
            for user in users:
                self.ui.employeeEditTask.addItem(f"{user[1]}", userData=user[0])
            if users:
                first_user_id = users[0][0]
                index = self.ui.employeeEditTask.findData(first_user_id)
                if index != -1:
                    self.ui.employeeEditTask.setCurrentIndex(index)

        except Exception as e:
            print(f'Ошибка при загрузке пользователей для редактирования: {e}')

    def apply_task(self):
        user_id = self.ui.employeeAddTask.currentData()
        task_text = self.ui.taskEditAdd.toPlainText()
        date = self.ui.dateEdit.date().toString("yyyy-MM-dd")

        if user_id is None or not task_text:
            return

        connection = connect()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO "Task" (date, task_text) VALUES (%s, %s) RETURNING task_id', (date, task_text))
        task_id = cursor.fetchone()[0]

        cursor.execute('INSERT INTO "User_task" (user_id, task_id) OVERRIDING SYSTEM VALUE VALUES (%s, %s) RETURNING user_task_id', (user_id, task_id))
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

    def edit_task(self):
        selected_index = self.ui.tableListTask.currentIndex()
        if not selected_index.isValid():
            return

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

        except Exception as e:
            print(f'Ошибка2: {e}')

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
            print(f'Ошибка1: {e}')

    def delete_selected_task(self):
        selected_indexes = self.ui.tableListTask.selectionModel().selectedRows()
        if not selected_indexes:
            return
        try:
            for index in selected_indexes:
                task_id = int(index.siblingAtColumn(3).data(Qt.UserRole))
                connection = connect()
                with self.connection.cursor() as cursor:
                    cursor.execute('DELETE FROM "Task" WHERE task_id = %s', (task_id,))
            connection.commit()
            self.get_data()
        except Exception as e:
            print(f'Ошибка3: {e}')

    def on_text_edit_changed(self):
        text = self.ui.textEdit.toPlainText()
        selected_text = self.ui.textEdit.textCursor().selectedText()
        if selected_text == text:
            self.ui.textEdit_2.clear()

    def init_translator_ui(self):
        self.ui.textEdit.textChanged.connect(self.start_timer)
        self.ui.comboBox.currentIndexChanged.connect(self.translate_text)
        self.ui.comboBox_2.currentIndexChanged.connect(self.translate_text)
        self.ui.comboBox.setStyleSheet("background-color: #3D434B; color: white;")
        self.ui.comboBox_2.setStyleSheet("background-color: #3D434B; color: white;")

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

    def setup_scroll_area(self):
        self.image_scroll_area = ImageScrollArea()
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
        self.setup_scroll_area()

    def open_edit_title_page(self):
        connection = connect()
        cursor = connection.cursor()
        cursor.execute('SELECT "title_name", "description" FROM "Title" WHERE title_id = %s', (self.title_id,))
        row = cursor.fetchone()
        close_db_connect(connection, cursor)

        if row:
            title_name, title_description = row
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageEditTitle)
            self.ui.nameEditTitle.setText(title_name)
            self.ui.descriptionEdit_2.setText(title_description)

    def switch_to_page_desc(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageDesc)

    def apply_title_changes(self):
        new_title_name = self.ui.nameEditTitle.text()
        new_description = self.ui.descriptionEdit_2.toPlainText()

        # Получаем путь к изображению из ImageAreaEdit
        image_path = self.ui.imageAreaEdit.toPlainText()

        # Загружаем изображение по указанному пути
        pixmap = QPixmap(image_path)
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.WriteOnly)
        pixmap.save(buffer, "PNG")  # Сохраняем изображение в байтовый массив в формате PNG
        byte_array = buffer.data()
        image_data = bytes(byte_array)

        connection = connect()
        cursor = connection.cursor()
        cursor.execute('UPDATE "Title" SET "title_name" = %s, "description" = %s, "icon_title" = %s WHERE title_id = %s',
                       (new_title_name, new_description, image_data, self.title_id))
        connection.commit()
        close_db_connect(connection, cursor)

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageTitle)
        self.ui.imageAreaEdit.clear()
        self.setup_scroll_area()

    def open_image_dialog(self, event):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images (*.png *.jpg *.jpeg)", options=options)
        if file_path:
            self.ui.imageAreaEdit.setText(file_path)

    def open_image_dialog_add_title(self, event):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images (*.png *.jpg *.jpeg)",
                                                   options=options)
        if file_path:
            self.ui.imageArea.setText(file_path)

    def add_title_to_database(self):
        title_name = self.ui.nameAddTitle.text()
        title_description = self.ui.descriptionEdit.toPlainText()
        image_path = self.ui.imageArea.toPlainText()

        # Загружаем изображение по указанному пути
        pixmap = QPixmap(image_path)
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.WriteOnly)
        pixmap.save(buffer, "PNG")  # Сохраняем изображение в байтовый массив в формате PNG
        byte_array = buffer.data()
        image_data = bytes(byte_array)

        connection = connect()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO "Title" ("title_name", "description", "icon_title") VALUES (%s, %s, %s)',
                       (title_name, title_description, image_data))
        connection.commit()
        cursor.close()
        connection.close()

        self.ui.nameAddTitle.clear()
        self.ui.descriptionEdit.clear()
        self.ui.imageArea.clear()
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageTitle)
        self.setup_scroll_area()

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

    current_dir = os.path.dirname(os.path.abspath(__file__))
    style_file_path = os.path.join(current_dir, "style.qss")

    if not os.path.exists(style_file_path):
        print("Файл стиля QSS не найден:", style_file_path)
        sys.exit(1)

    with open(style_file_path, "r") as style_file:
        style_str = style_file.read()

    app.setStyleSheet(style_str)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

