from PyQt5.QtWidgets import QStackedWidget, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QMenuBar, QToolBar, QApplication
from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtSvg import QSvgWidget as qsvg
from PyQt5.QtCore import Qt, QRectF

class account(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.setLayout(QVBoxLayout())

        account_info_widget = QWidget()
        account_info_widget.setLayout(QVBoxLayout())
        account_info_widget.setContentsMargins(100, 0, 100, 0)
        self.layout().addWidget(account_info_widget, 5)

        aco_title = QLabel("Account Information")
        aco_title.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        account_info_widget.layout().addWidget(aco_title)

        # change the username and the password
        aco_widget1 = QWidget()
        aco_widget1.setLayout(QHBoxLayout())
        account_info_widget.layout().addWidget(aco_widget1)

        aco_widget2 = QWidget()
        aco_widget2.setLayout(QHBoxLayout())
        account_info_widget.layout().addWidget(aco_widget2)

        aco_widget3 = QWidget()
        aco_widget3.setLayout(QVBoxLayout())
        aco_widget1.layout().addWidget(aco_widget3)

        aco_widget4 = QWidget()
        aco_widget4.setLayout(QVBoxLayout())
        aco_widget1.layout().addWidget(aco_widget4)

        aco_txt1_label = QLabel("Username:")
        aco_txt1_label.setStyleSheet("color: white; font-size: 15px;")
        aco_widget3.layout().addWidget(aco_txt1_label)

        self.aco_enter1 = QLineEdit()
        aco_widget4.layout().addWidget(self.aco_enter1, alignment=Qt.AlignmentFlag.AlignLeft)

        aco_txt2_label = QLabel("Password:")
        aco_txt2_label.setStyleSheet("color: white; font-size: 15px;")
        aco_widget3.layout().addWidget(aco_txt2_label)

        self.aco_enter2 = QLineEdit()
        aco_widget4.layout().addWidget(self.aco_enter2, alignment=Qt.AlignmentFlag.AlignLeft)

        aco_btn = QPushButton("Save")
        aco_btn.setStyleSheet("font-size: 10px;")
        account_info_widget.layout().addWidget(aco_btn, alignment=Qt.AlignmentFlag.AlignRight)


        # button to save the changes


        # setting 
        setting_widget = QWidget()
        setting_widget.setLayout(QVBoxLayout())
        self.layout().addWidget(setting_widget, 5)

        set_title = QLabel("Setting")
        set_title.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        setting_widget.layout().addWidget(set_title)

        

    