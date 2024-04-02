import sys
import os
from PySide6.QtWidgets import QApplication
from Interface.main_window import MainWindow
from Interface.main_window import MainWindow
from Interface.ui import Ui_MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    style_file_path = os.path.join(current_dir, "Interface", "style.qss")

    if not os.path.exists(style_file_path):
        print("Файл стиля QSS не найден:", style_file_path)
        sys.exit(1)

    with open(style_file_path, "r") as style_file:
        style_str = style_file.read()

    app.setStyleSheet(style_str)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())