from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QLabel, QTextBrowser
from PyQt5.QtWebEngineWidgets import QWebEngineView
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
        self.layout().addWidget(inb_content_widget, 4)

        self.text_browser = QTextBrowser()
        html_path = os.path.abspath(os.path.join("resources", "inLabs_regulations.html"))
        self.text_browser.setSource(QUrl.fromLocalFile(html_path))
        inb_content_widget.layout().addWidget(self.text_browser)

        # an area to display the common symbols occured in labs
        ghs_symbols_widget = QWidget()
        ghs_symbols_widget.setLayout(QVBoxLayout())
        ghs_symbols_widget.setStyleSheet("border-radius: 10px;")
        self.layout().addWidget(ghs_symbols_widget, 6)

        self.image_browser = QWebEngineView()
        self.image_browser.setStyleSheet("background: transparent;")
        self.image_browser.page().setBackgroundColor(Qt.transparent)

        html_path = os.path.abspath(os.path.join("imagesource", "inLabs_images.html"))
        self.image_browser.load(QUrl.fromLocalFile(html_path))
        ghs_symbols_widget.layout().addWidget(self.image_browser)

        

