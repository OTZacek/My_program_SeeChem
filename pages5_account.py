from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtSvg import QSvgWidget as qsvg
from PyQt5.QtCore import Qt, QRectF

class account(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.setLayout(QHBoxLayout())

        # to make the widget can sit in the middle
        empty1 = QWidget()
        self.layout().addWidget(empty1, 2)
        
        self1 = QWidget()
        self1.setLayout(QVBoxLayout())
        self.layout().addWidget(self1, 5)

        empty2 = QWidget()
        self.layout().addWidget(empty2, 3)

        account_info_widget = QWidget()
        account_info_widget.setLayout(QVBoxLayout())
        self1.layout().addWidget(account_info_widget, 4)

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

        # button to save the changes
        aco_btn = QPushButton("Save")
        aco_btn.setStyleSheet("font-size: 15px; border-radius: 5px;")
        account_info_widget.layout().addWidget(aco_btn, alignment=Qt.AlignmentFlag.AlignRight)


        # setting 
        setting_widget = QWidget()
        setting_widget.setLayout(QVBoxLayout())
        self1.layout().addWidget(setting_widget, 6)

        set_title = QLabel("Setting")
        set_title.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        setting_widget.layout().addWidget(set_title)

        set_btn_widget = QWidget()
        set_btn_widget.setLayout(QVBoxLayout())
        setting_widget.layout().addWidget(set_btn_widget, alignment=Qt.AlignmentFlag.AlignTop)

        set_btn1 = QPushButton("Erase all history")
        set_btn1.setStyleSheet("font-size: 15px; border-radius: 5px;")
        set_btn_widget.layout().addWidget(set_btn1, alignment=Qt.AlignmentFlag.AlignLeft)

        set_btn2 = QPushButton("Delete the account")
        set_btn2.setStyleSheet("font-size: 15px; border-radius: 5px;")
        set_btn_widget.layout().addWidget(set_btn2, alignment=Qt.AlignmentFlag.AlignLeft)

        

    