from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QLabel, QTextBrowser
from PyQt5.QtCore import Qt, QUrl
import os


class inLabs(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.setLayout(QHBoxLayout())

        # an area to place the lab rules
        inb_content_widget = QWidget()
        inb_content_widget.setLayout(QVBoxLayout())
        inb_content_widget.setStyleSheet("background-color: transparent; border-radius: 10px;")
        self.layout().addWidget(inb_content_widget, 5)

        self.text_browser = QTextBrowser()
        html_path = os.path.abspath(os.path.join("resources", "inLabs_regulations.html"))
        self.text_browser.setSource(QUrl.fromLocalFile(html_path))
        inb_content_widget.layout().addWidget(self.text_browser)

        ghs_symbols_widget = QWidget()
        ghs_symbols_widget.setLayout(QGridLayout())
        self.layout().addWidget(ghs_symbols_widget, 5)

        temp_notice = QLabel("GHS Symbols will be updated here...")
        ghs_symbols_widget.layout().addWidget(temp_notice)