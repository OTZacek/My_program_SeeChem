from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPainter
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtSvg import QSvgWidget as qsvg
from PyQt5.QtCore import Qt, QRectF

class welcome(QWidget):
    def __init__(self, switch_func):
        super().__init__()

        self.setLayout(QHBoxLayout())
        self.welcome_bg = QSvgRenderer("imagesource/welcome_page_bg.svg")

        # content and image
        wel_1_widget = QWidget()
        wel_1_widget.setLayout(QVBoxLayout())
        self.layout().addWidget(wel_1_widget, 6)

        # text
        wel_title_widget = QWidget()
        wel_title_widget.setLayout(QVBoxLayout())
        wel_1_widget.layout().addWidget(wel_title_widget, 4, alignment=Qt.AlignmentFlag.AlignLeft)

        wel_title1 = QLabel("Welcome to SeeChem")
        wel_title_widget.layout().addWidget(wel_title1)
        wel_title1.setStyleSheet("font-family: 'poppins'; font-size: 80px; font-weight: bold; color: #DFF2EC;")


        wel_title2 = QLabel("where you start your chemistry")
        wel_title_widget.layout().addWidget(wel_title2)
        wel_title2.setStyleSheet("font-family: 'poppins'; font-size: 50px; color: #DFF2EC")

        # button

        wel_button_widget = QWidget()
        wel_button_widget.setLayout(QVBoxLayout())
        wel_1_widget.layout().addWidget(wel_button_widget, 3, alignment=Qt.AlignmentFlag.AlignLeft)


        wel_button1 = QPushButton("➔ Log in")
        wel_button1.setStyleSheet("""
        font-size: 30px; text-align: left; color: white; 
        border: none; background-color: transparent;
        """)
        wel_button_widget.layout().addWidget(wel_button1)
        wel_button1.clicked.connect(lambda: switch_func(1, "log in"))

        wel_button2 = QPushButton("➔ Create account")
        wel_button2.setStyleSheet("""
        font-size: 30px; text-align: left; color: white; 
        border: none; background-color: transparent;
        """)
        wel_button_widget.layout().addWidget(wel_button2)
        wel_button2.clicked.connect(lambda: switch_func(1, "create acc"))

        wel_button3 = QPushButton("➔ Continue as a guest")
        wel_button3.setStyleSheet("""
        font-size: 30px; text-align: left; color: white; 
        border: none; background-color: transparent;
        """)
        wel_button_widget.layout().addWidget(wel_button3)

        fastbutton = QPushButton("HOME")
        wel_button_widget.layout().addWidget(fastbutton)
        fastbutton.clicked.connect(lambda: switch_func(2))

        #logo
        wel_logo_widget = QWidget()
        wel_logo_widget.setBaseSize(150, 150)
        wel_logo_widget.setLayout(QVBoxLayout())
        wel_1_widget.layout().addWidget(wel_logo_widget, 3, alignment=Qt.AlignmentFlag.AlignLeft)

        wel_logo = qsvg("imagesource/SeeChemLogo.svg")
        wel_logo_widget.layout().addWidget(wel_logo)

        wel_txt1 = QLabel("SeeChem All Rights Reserved")
        wel_logo_widget.layout().addWidget(wel_txt1)
        wel_txt1.setStyleSheet("color: white;")

    # draw the bg
    def paintEvent(self, event):
        painter = QPainter(self)
        self.welcome_bg.render(painter, QRectF(self.rect()))