from PyQt5.QtWidgets import QStackedWidget, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QMenuBar, QToolBar, QApplication
from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox, QTextEdit
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtSvg import QSvgWidget as qsvg
from PyQt5.QtCore import Qt, QRectF

class home(QWidget):
    def __init__(self, switch_func, save_func=None, history_func=None):
        super().__init__()
        self.save_func = save_func
        self.history_func = history_func

        self.setLayout(QVBoxLayout())

        # text
        hom_caption1 = QLabel("Get starting...")
        hom_caption1.setStyleSheet("font-size: 50px; color: white;")
        self.layout().addWidget(hom_caption1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 
        hom_content_widget = QWidget()
        hom_content_widget.setLayout(QHBoxLayout())
        self.layout().addWidget(hom_content_widget, 8)

        # place for users to put notes

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Your can make your notes here...")
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background: rgba(255,255,255,0.1);
                color: white;
                border-radius: 8px;
                padding: 6px;
                font-size: 16px;
            }
        """)
        hom_content_widget.layout().addWidget(self.text_edit, 5)

        btn_row = QWidget()
        btn_row.setLayout(QHBoxLayout())
        hom_content_widget.layout().addWidget(btn_row, 1)

        save_button = QPushButton("Save")
        save_button.setStyleSheet("font-size: 16px; padding: 6px;")
        save_button.clicked.connect(self.save_note)
        btn_row.layout().addWidget(save_button)

        history_button = QPushButton("History")
        history_button.setStyleSheet("font-size: 16px; padding: 6px;")
        history_button.clicked.connect(self.show_history)
        btn_row.layout().addWidget(history_button)

    def save_note(self):
        content = self.text_edit.toPlainText()
        if self.save_func:
            success, msg = self.save_func(content)
            if success:
                QMessageBox.information(self, "Success", f"Saved successfully! Time:{msg}")
                self.text_edit.clear()
            else:
                QMessageBox.warning(self, "Failure", msg)

    def show_history(self):
        if not self.history_func:
            QMessageBox.warning(self, "History", "You are not logged in!")
            return

        history_text = self.history_func()  # Only fetch now
        if not history_text.strip():
            history_text = "Empty here"
        QMessageBox.information(self, "History", history_text)