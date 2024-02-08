import sys
from functools import partial
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize_direction = None
        self.resize_position = None
        self.drag_position = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.icon.hide()
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.titleBtn_2.setChecked(True)

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

        self.ui.closeBtn.clicked.connect(self.closeApp)
        self.ui.expandBtn.clicked.connect(self.toggle_screen_state)
        self.ui.minimazeBtn.clicked.connect(self.minimizeApp)
        self.screen_expanded = False

    def enterEvent(self, event):
        if not self.screen_expanded:
            pos = event.globalPosition().toPoint()
            frame_geometry = self.frameGeometry()
            left_edge = abs(pos.x() - frame_geometry.left()) <= 5
            right_edge = abs(pos.x() - frame_geometry.right()) <= 5
            top_edge = abs(pos.y() - frame_geometry.top()) <= 5
            bottom_edge = abs(pos.y() - frame_geometry.bottom()) <= 5

            if left_edge or right_edge or top_edge or bottom_edge:
                if left_edge:
                    if top_edge:
                        self.setCursor(Qt.SizeFDiagCursor)
                    elif bottom_edge:
                        self.setCursor(Qt.SizeBDiagCursor)
                    else:
                        self.setCursor(Qt.SizeHorCursor)
                elif right_edge:
                    if top_edge:
                        self.setCursor(Qt.SizeBDiagCursor)
                    elif bottom_edge:
                        self.setCursor(Qt.SizeFDiagCursor)
                    else:
                        self.setCursor(Qt.SizeHorCursor)
                elif top_edge or bottom_edge:
                    self.setCursor(Qt.SizeVerCursor)
                elif self.ui.widget_2.rect().contains(self.ui.widget_2.mapFromGlobal(pos)):
                    self.setCursor(Qt.OpenHandCursor)

    def leaveEvent(self, event):
        if not self.screen_expanded:
            self.setCursor(Qt.ArrowCursor)

    def closeApp(self):
        self.close()

    def minimizeApp(self):
        self.showMinimized()

    def toggle_screen_state(self):
        if self.screen_expanded:
            self.showNormal()
        else:
            self.showMaximized()
        self.screen_expanded = not self.screen_expanded

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            pos = event.globalPosition().toPoint()
            frame_geometry = self.frameGeometry()

            if (
                    abs(pos.x() - frame_geometry.left()) <= 5
                    or abs(pos.x() - frame_geometry.right()) <= 5
                    or abs(pos.y() - frame_geometry.top()) <= 5
                    or abs(pos.y() - frame_geometry.bottom()) <= 5
            ):
                self.resize_position = pos
                if abs(pos.x() - frame_geometry.left()) <= 5:
                    if abs(pos.y() - frame_geometry.top()) <= 5:
                        self.resize_direction = "top_left"
                        self.setCursor(Qt.SizeFDiagCursor)
                    elif abs(pos.y() - frame_geometry.bottom()) <= 5:
                        self.resize_direction = "bottom_left"
                        self.setCursor(Qt.SizeBDiagCursor)
                    else:
                        self.resize_direction = "left"
                        self.setCursor(Qt.SizeHorCursor)
                elif abs(pos.x() - frame_geometry.right()) <= 5:
                    if abs(pos.y() - frame_geometry.top()) <= 5:
                        self.resize_direction = "top_right"
                        self.setCursor(Qt.SizeBDiagCursor)
                    elif abs(pos.y() - frame_geometry.bottom()) <= 5:
                        self.resize_direction = "bottom_right"
                        self.setCursor(Qt.SizeFDiagCursor)
                    else:
                        self.resize_direction = "right"
                        self.setCursor(Qt.SizeHorCursor)
                elif abs(pos.y() - frame_geometry.top()) <= 5:
                    self.resize_direction = "top"
                    self.setCursor(Qt.SizeVerCursor)
                elif abs(pos.y() - frame_geometry.bottom()) <= 5:
                    self.resize_direction = "bottom"
                    self.setCursor(Qt.SizeVerCursor)
                event.accept()

            elif (
                    abs(pos.y() - frame_geometry.top()) <= 5
                    and frame_geometry.left() <= pos.x() <= frame_geometry.right()
            ):
                self.drag_position = pos - frame_geometry.topLeft()
                event.accept()

            elif self.ui.widget_2.rect().contains(self.ui.widget_2.mapFromGlobal(pos)):
                self.drag_position = pos - frame_geometry.topLeft()
                event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.drag_position is not None:
                self.move(event.globalPosition().toPoint() - self.drag_position)
                event.accept()
            elif self.resize_position is not None:
                delta = event.globalPosition().toPoint() - self.resize_position
                frame_geometry = self.frameGeometry()

                if "left" in self.resize_direction:
                    new_left = frame_geometry.left() + delta.x()
                    if new_left < frame_geometry.right() - self.minimumWidth():
                        frame_geometry.setLeft(new_left)
                elif "right" in self.resize_direction:
                    new_right = frame_geometry.right() + delta.x()
                    if new_right > frame_geometry.left() + self.minimumWidth():
                        frame_geometry.setRight(new_right)
                if "top" in self.resize_direction:
                    new_top = frame_geometry.top() + delta.y()
                    if new_top < frame_geometry.bottom() - self.minimumHeight():
                        frame_geometry.setTop(new_top)
                elif "bottom" in self.resize_direction:
                    new_bottom = frame_geometry.bottom() + delta.y()
                    if new_bottom > frame_geometry.top() + self.minimumHeight():
                        frame_geometry.setBottom(new_bottom)

                self.setGeometry(frame_geometry)
                self.resize_position = event.globalPosition().toPoint()
                event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = None
            self.resize_position = None
            self.setCursor(Qt.ArrowCursor)
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
