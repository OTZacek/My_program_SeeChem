from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QMenuBar, QToolBar, QApplication
from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtSvg import QSvgWidget as qsvg
from PyQt5.QtCore import Qt, QRectF

class n_home(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.setLayout(QVBoxLayout())

        # text
        txt1 = QLabel("Looking forward for your joining!")
        txt1.setStyleSheet("font-size: 50px; color: white;")
        self.layout().addWidget(txt1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

        # buttons
        btn_widget = QWidget()
        btn_widget.setLayout()
        self.layout().addWidget(btn_widget)

        

        back_btn = QPushButton("Back to Welcome Page")
        back_btn.setStyleSheet("""
                        font-size: 13px; text-align: center; color: black; 
                        background-color: white; border-radius: 5px;
                        """)
        self.layout().addWidget(back_btn)
        back_btn.clicked.connect(lambda: switch_func(0))