from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QPushButton, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
import sys


class seechem_menubar(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.switch_func = switch_func
        self.menubar_ui()

    def menubar_ui(self):
        self.setStyleSheet("""
            QWidget {;}
            QLabel {background: transparent; border: none; font-family: ; font-size: 16px; color: white; font-weight: bold;}
            QPushButton {background: transparent; border: none; padding: 10px 20px;}
            QPushButton:hover {background-color: #7C6FC1; border-radius: 5px;}
            """)
        
        # an unknown glitch about the syntax highlighting on QLabel and QPushButton, that if I delete the QWidget, the /
        # code runs well, yet the color of mentioned sentences will be strange /
        # so I keep the QWidget...

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        home_btn = QPushButton()
        home_btn.setIcon(QIcon("imagesource/home_logo.svg"))
        home_btn.setIconSize(QSize(30, 30))
        home_btn.clicked.connect(lambda: self.switch_func(2))
        layout.addWidget(home_btn)

        current_loc = QLabel("SeeChem")
        layout.addWidget(current_loc)

        layout.addStretch()

        account_btn = QPushButton()
        account_btn.setIcon(QIcon("imagesource/account_icon.svg"))
        layout.addWidget(account_btn)


        # more button with dropdown menu
        more_btn = QPushButton()
        more_btn.setIcon(QIcon("imagesource/more_icon.svg"))
        layout.addWidget(more_btn)

        more_menu = QMenu()
        more_menu.addAction("Periodic Tabel")
        more_menu.addAction("Simulator")
        more_menu.addAction("Chemistry Principles")
        more_menu.addAction("If in Lab")
        more_menu.addAction("Setting")
        more_menu.addAction("save 'n exit", lambda: sys.exit())

        more_btn.setMenu(more_menu)
