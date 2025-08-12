from PyQt5.QtWidgets import QStackedWidget, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QMenuBar, QToolBar, QApplication
from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtSvg import QSvgWidget as qsvg
from PyQt5.QtCore import Qt, QRectF

class home(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.setLayout(QVBoxLayout())

        # text
        hom_caption1 = QLabel("Get starting...")
        hom_caption1.setStyleSheet("font-size: 50px; color: white;")
        self.layout().addWidget(hom_caption1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

        # buttons and recently created
        hom_content_widget = QWidget()
        hom_content_widget.setLayout(QHBoxLayout())
        self.layout().addWidget(hom_content_widget, 8)

        hom_simu_widget = QWidget()
        hom_simu_widget.setLayout(QVBoxLayout())
        hom_content_widget.layout().addWidget(hom_simu_widget, 5)

        hom_recent_widget = QWidget()
        hom_recent_widget.setLayout(QVBoxLayout())
        hom_content_widget.layout().addWidget(hom_recent_widget, 5)

        # let's create
        create_label = QLabel("Rencently Used")
        create_label.setStyleSheet("font-family: Galvji; font-size: 20px; color: white;")
        hom_simu_widget.layout().addWidget(create_label, alignment=Qt.AlignmentFlag.AlignTop)