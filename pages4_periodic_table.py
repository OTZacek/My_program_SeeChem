from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl
import os

class periodic_table(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.setLayout(QHBoxLayout())

        periodic_table_content = QWidget()
        periodic_table_content.setLayout(QVBoxLayout())
        self.layout().addWidget(periodic_table_content)

        # only for html method
        self.table_browser = QWebEngineView()
        self.table_browser.setStyleSheet("background: transparent;")
        self.table_browser.page().setBackgroundColor(Qt.transparent)

        html_path = os.path.abspath(os.path.join("resources", "seechem_periodic_table.html"))
        self.table_browser.load(QUrl.fromLocalFile(html_path))
        periodic_table_content.layout().addWidget(self.table_browser)