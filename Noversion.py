import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit
from googletrans import Translator
from qt_material import apply_stylesheet
from PySide6.QtCore import QTimer

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.timer = QTimer()
        self.timer.timeout.connect(self.translate_text)

    def init_ui(self):
        self.setWindowTitle('Переводчик')

        self.input_label = QLabel('Введите текст для перевода:')
        self.input_text = QLineEdit()
        self.input_text.textChanged.connect(self.start_timer)
        self.output_label = QLabel('Перевод:')

        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def start_timer(self):
        self.timer.stop()
        self.timer.start(100)

    def translate_text(self):
        text_to_translate = self.input_text.text()
        translator = Translator()
        translation = translator.translate(text_to_translate, dest='en')
        self.output_label.setText(f"Перевод: {translation.text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator_app = TranslatorApp()
    apply_stylesheet(app, theme='dark_custom_theme.xml')
    translator_app.show()
    sys.exit(app.exec())
