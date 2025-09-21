from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from PyQt5.QtCore import Qt, QRectF

from seechem_database import check_user_db1, update_username, update_password

class account(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.setLayout(QHBoxLayout())

# to make the widget sit in the middle
        empty1 = QWidget()
        self.layout().addWidget(empty1, 2)

        self1 = QWidget()
        self1.setLayout(QVBoxLayout())
        self.layout().addWidget(self1, 5)

        empty2 = QWidget()
        self.layout().addWidget(empty2, 3)

        # Account info section container
        account_info_widget = QWidget()
        account_info_widget.setLayout(QVBoxLayout())
        self1.layout().addWidget(account_info_widget, 4)

        # Title
        aco_title = QLabel("Account Information")
        aco_title.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        aco_title.setAlignment(Qt.AlignCenter)
        account_info_widget.layout().addWidget(aco_title)

        # --- Username row ---
        username_row = QWidget()
        username_row.setLayout(QHBoxLayout())
        account_info_widget.layout().addWidget(username_row)

        aco_txt1_label = QLabel("Current username:")
        aco_txt1_label.setStyleSheet("color: white; font-size: 15px;")
        username_row.layout().addWidget(aco_txt1_label)

        self.aco_enter1 = QLineEdit()
        self.aco_enter1.setPlaceholderText("write down your current username here")
        self.aco_enter1.setFixedWidth(200)
        username_row.layout().addWidget(self.aco_enter1)

        aco_txt3_label = QLabel("New username:")
        aco_txt3_label.setStyleSheet("color: white; font-size: 15px;")
        username_row.layout().addWidget(aco_txt3_label)

        self.aco_enter3 = QLineEdit()
        self.aco_enter3.setPlaceholderText("update your username here")
        self.aco_enter3.setFixedWidth(200)
        username_row.layout().addWidget(self.aco_enter3)

        # --- Password row ---
        password_row = QWidget()
        password_row.setLayout(QHBoxLayout())
        account_info_widget.layout().addWidget(password_row)

        aco_txt2_label = QLabel("Current password:")
        aco_txt2_label.setStyleSheet("color: white; font-size: 15px;")
        password_row.layout().addWidget(aco_txt2_label)

        self.aco_enter2 = QLineEdit()
        self.aco_enter2.setPlaceholderText("enter your current password")
        self.aco_enter2.setEchoMode(QLineEdit.Password)
        self.aco_enter2.setFixedWidth(200)
        password_row.layout().addWidget(self.aco_enter2)

        aco_txt4_label = QLabel("New password:")
        aco_txt4_label.setStyleSheet("color: white; font-size: 15px;")
        password_row.layout().addWidget(aco_txt4_label)

        self.aco_enter4 = QLineEdit()
        self.aco_enter4.setPlaceholderText("enter your new password")
        self.aco_enter4.setEchoMode(QLineEdit.Password)
        self.aco_enter4.setFixedWidth(200)
        password_row.layout().addWidget(self.aco_enter4)

        # Save button
        aco_btn = QPushButton("Save")
        aco_btn.setStyleSheet("""
            QPushButton {font-size: 15px; color: black; background-color: white; border-radius: 5px; padding: 5px 10px;}
            QPushButton:hover {background-color: #C4B9B9;}
        """)
        aco_btn.clicked.connect(self.update_userinfo)
        account_info_widget.layout().addWidget(aco_btn, alignment=Qt.AlignRight)

        # setting 
        # setting_widget = QWidget()
        # setting_widget.setLayout(QVBoxLayout())
        # self1.layout().addWidget(setting_widget, 6)

        # set_title = QLabel("Setting")
        # set_title.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        # setting_widget.layout().addWidget(set_title)

        # set_btn_widget = QWidget()
        # set_btn_widget.setLayout(QVBoxLayout())
        # setting_widget.layout().addWidget(set_btn_widget, alignment=Qt.AlignmentFlag.AlignTop)

        # set_btn1 = QPushButton("Erase all history")
        # set_btn1.setStyleSheet("""
        # QPushButton {font-size: 15px; color: black; background-color: white; border-radius: 5px; padding: 5px 10px;}
        # QPushButton:hover {background-color: #C4B9B9;}""")
        # set_btn_widget.layout().addWidget(set_btn1, alignment=Qt.AlignmentFlag.AlignLeft)

        # set_btn2 = QPushButton("Delete the account")
        # set_btn2.setStyleSheet("""
        # QPushButton {font-size: 15px; color: black; background-color: white; border-radius: 5px; padding: 5px 10px;}
        # QPushButton:hover {background-color: #C4B9B9;}""")
        # set_btn_widget.layout().addWidget(set_btn2, alignment=Qt.AlignmentFlag.AlignLeft)

        # functions here

        # change userinfo function
    def update_userinfo(self):
        current_username = self.aco_enter1.text().strip()
        current_password = self.aco_enter2.text().strip()
        new_username = self.aco_enter3.text().strip()
        new_password = self.aco_enter4.text().strip()

        if not current_username or not current_password:
            QMessageBox.warning(self, "Error", "Current username and password are required!")
            return
        if not new_username and not new_password:
            QMessageBox.warning(self, "Error", "Please enter a new username and/or password!")
            return

        try:
            verification = check_user_db1(current_username, current_password)
            if verification:  # user exists

                if new_username:
                    ok = update_username(current_username, new_username)
                    if not ok:
                        QMessageBox.warning(self, "Error", "New username already exists!")
                        return
                    current_username = new_username  # update reference for password update

                if new_password:
                    update_password(current_username, new_password)

                QMessageBox.information(self, "Success", "Account updated successfully!")

            else:
                QMessageBox.warning(self, "Error", "Current username and password do not match!")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")