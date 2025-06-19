from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QMenu, QAction, QToolButton
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgWidget as qsvg
from PyQt5.QtGui import QPainter, QIcon

class topbar(QWidget):
    def __init__(self, currentloc):
        super().__init__()

        self.setLayout(QHBoxLayout())
        self.setStyleSheet("background-color: #090E9A")

        # logo to home
        logo_home_btn = QPushButton()
        logo_home_btn.setIcon(QIcon("imagesource/home_logo.svg"))
        logo_home_btn.setFixedSize(20, 20)
        #logo_home_btn.clicked.connect(lambda: self.switch_page_func("Home"))
        self.layout().addWidget(logo_home_btn)

        # location
        topbar_loc = QLabel()
        
        

