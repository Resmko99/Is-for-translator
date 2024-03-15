import sys
import os
from functools import partial
from PySide6.QtCore import Qt, QPoint, QPropertyAnimation, QEasingCurve, QEvent, QDate, QTimer
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea, QHBoxLayout,
                               QGridLayout, QPushButton, QHeaderView, QLabel, QLineEdit)
from PySide6.QtGui import QPixmap, QPainter, QCursor, QStandardItemModel, QStandardItem
from googletrans import Translator
from datetime import datetime
import itertools
import psycopg2

from ui import Ui_MainWindow

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

        image_paths = [
            r"Photo\AA1kTdiJ.jpg",
            r"Photo\EyX_7safWuU.jpg",
            r"Photo\x_89c4262c.jpg",
            r"Photo\3G3tOpNoHPQ.jpg",
            r"Photo\ee855f4a-8d70-4c03-b56e-f7a5059bbbec.jpg",
            r"Photo\1bbb92772c6c2826a41f6f43dddb515d.jpg",
            r"Photo\e1d2c368-d1eb-43f3-9dd6-c33c8ac680d2.jpg",
            r"Photo\0a1a1fd8-f38f-4ce2-84a8-74a83c63203c.jpg",
        ]

        repeated_paths = itertools.cycle(image_paths)

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

        self.images_per_row = 5

        for i in range(56):
            if i % self.images_per_row == 0:
                self.row_layout = QHBoxLayout()
                self.scrollLayout.addLayout(self.row_layout)

            self.image_text_container = QWidget()
            self.image_text_container.setStyleSheet("background-color: #3D434B;"
                                                    "border: none;"
                                                    "border-radius: 10px;"
                                                    "border: 2px solid #FFCC33;"
                                                    "margin: 15px;")

            self.image_text_layout = QVBoxLayout(self.image_text_container)

            image_path = next(repeated_paths)
            label = RoundedImageLabel()
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(250, 380, Qt.IgnoreAspectRatio)
            if not pixmap.isNull():
                label.setPixmap(pixmap)
            else:
                label.setText("Image not found")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("border: none")
            self.image_text_layout.addWidget(label)

            text_label = QLabel(f"Text for Image {i + 1}")
            self.image_text_layout.addWidget(text_label)
            text_label.setStyleSheet("color: #fff; border: none; margin-top: 2px;")
            text_label.setAlignment(Qt.AlignCenter)

            self.row_layout.addWidget(self.image_text_container)

        self.scrollLayout.addStretch()
        self.scroll.setWidget(self.scrollContent)
        self.scroll_area_contents_layout.addWidget(self.scroll)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize_direction = None
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
        self.ui.widget_4.hide()
        self.ui.titleBtn_2.setChecked(True)

        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

        self.normal_geometry = None

        self.model_table_task = QStandardItemModel()
        self.ui.tableListTask.setModel(self.model_table_task)
        self.database_connection()

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
            (self.ui.backTaskBtn, self.ui.pageListTask)
        ]

        for button, page in move_buttons:
            button.clicked.connect(partial(self.ui.stackedWidget_2.setCurrentWidget, page))

        self.ui.closeBtn.clicked.connect(self.closeApp)
        self.ui.expandBtn.clicked.connect(self.toggle_screen_state)
        self.ui.minimazeBtn.clicked.connect(self.minimizeApp)
        self.ui.taskAddBtn.clicked.connect(self.apply_task)
        self.screen_expanded = False

        # Установка фильтра событий для главного окна
        self.open_hand_px = QPixmap(directory + f'/Photo/free-icon-cursor-5340828.png')
        self.scaled_open_hand_px = self.open_hand_px.scaled(16, 16)
        self.scaled_open_hand_px.setMask(self.scaled_open_hand_px.mask())
        self.open_hand_cursor = QCursor(self.scaled_open_hand_px, 0, 0)
        self.setCursor(self.open_hand_cursor)
        self.current_cursor = self.open_hand_cursor

        self.installEventFilter(self)
        self.setup_scroll_area()
        self.setup_calender_widget()
        self.get_data_orders()

        self.translation_delay = 100
        self.translation_timer = QTimer()
        self.translation_timer.setSingleShot(True)
        self.translation_timer.timeout.connect(self.translate_text)
        self.init_translator_ui()
        self.ui.textEdit.textChanged.connect(self.on_text_edit_changed)

    def database_connection(self):
        try:
            self.connection = psycopg2.connect(
                dbname="task",
                user="postgres",
                password="user",
                host="localhost",
            )
            self.cursor = self.connection.cursor()
            print("Успешное подключение к базе данных PostgreSQL!")
        except (Exception, psycopg2.Error) as error:
            print("Ошибка при подключении к базе данных PostgreSQL:", error)
            QMessageBox.critical(self, "Ошибка", "Ошибка при подключении к базе данных PostgreSQL.")
            sys.exit(1)

        self.load_users()
        self.get_data_orders()

    def load_users(self):
        self.ui.employeeAddTask.clear()
        self.cursor.execute("SELECT user_id, login, password FROM public.user")
        users = self.cursor.fetchall()
        for user in users:
            self.ui.employeeAddTask.addItem(f"{user[1]}", userData=user[0])

    def apply_task(self):
        user_id = self.ui.employeeAddTask.currentData()
        task_text = self.ui.taskEditAdd.toPlainText()
        date = self.ui.dateEdit.date().toString("yyyy-MM-dd")

        if user_id is None or not task_text:
            return

        self.cursor.execute("INSERT INTO task (date, task_text) VALUES (%s, %s) RETURNING id_task", (date, task_text))
        id_task = self.cursor.fetchone()[0]

        self.cursor.execute("INSERT INTO user_task (id_user, id_task) VALUES (%s, %s) RETURNING id_user_task", (user_id, id_task))
        self.connection.commit()


        self.ui.employeeAddTask.clear()
        self.ui.taskEditAdd.clear()
        self.load_users()
        self.get_data_orders()
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageListTask)

    def get_data_orders(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute('''
                    SELECT "user".login, task.task_text, task.date
                    FROM user_task
                    INNER JOIN "user" ON user_task.id_user = "user".user_id
                    INNER JOIN task ON user_task.id_task = task.id_task
                    ORDER BY user_task.id_user_task;
                ''')
                records = cursor.fetchall()

                self.model_table_task.clear()
                self.model_table_task.setColumnCount(3)
                self.model_table_task.setHorizontalHeaderLabels(['Пользователь', 'Задача', 'Дата'])

                for record in records:
                    row = [QStandardItem(str(value)) for value in record]

                    self.model_table_task.appendRow(row)
                self.ui.tableListTask.resizeColumnsToContents()

                header = self.ui.tableListTask.horizontalHeader()
                header.setSectionResizeMode(QHeaderView.Stretch)

        except Exception as e:
            print(f'Ошибка: {e}')


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

        if not text_to_translate:
            return

        if selected_src_lang == "Выберите язык" or selected_dest_lang == "Выберите язык":
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
                translated_text = translation.text if translation else ""
                self.ui.textEdit_2.setPlainText(translated_text)
            except Exception as e:
                print("Ошибка при переводе текста:", e)
        else:
            print("Ошибка: Один из выбранных языков не распознается.")

    def open_desc_page(self, event, widget):
        if event.button() == Qt.LeftButton:
            self.clicked_widget = widget
            self.update_photo_desc()
            self.change_page_with_animation(self.ui.pageDesc)

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

    def setup_scroll_area(self):
        self.image_scroll_area = ImageScrollArea()
        self.ui.titleGrid.addWidget(self.image_scroll_area, 0, 0)

        for child_widget in self.image_scroll_area.findChildren(RoundedImageLabel):
            child_widget.mousePressEvent = lambda event, widget=child_widget: self.open_desc_page(event, widget)

    def open_desc_page(self, event, widget):
        if event.button() == Qt.LeftButton:
            self.clicked_widget = widget
            self.update_photo_desc()
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.pageDesc)

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
    sys.exit(app.exec())

