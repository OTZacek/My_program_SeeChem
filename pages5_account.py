from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from PyQt5.QtCore import Qt

from seechem_database import check_user_db1, update_username, update_password, delete_user_db1

class account(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.setLayout(QHBoxLayout())

        # to make the widget sit in the middle
        empty1 = QWidget()
        self.layout().addWidget(empty1, 2)

        account_info_widget = QWidget()
        account_info_widget.setLayout(QVBoxLayout())
        self.layout().addWidget(account_info_widget, 5)

        empty2 = QWidget()
        self.layout().addWidget(empty2, 3)

        # Title
        aco_title = QLabel("Account Management")
        aco_title.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        aco_title.setAlignment(Qt.AlignLeft)
        account_info_widget.layout().addWidget(aco_title)

        # Verification Section
        verify_label = QLabel("Verify your account")
        verify_label.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        account_info_widget.layout().addWidget(verify_label)

        verify_row = QWidget()
        verify_row.setLayout(QHBoxLayout())
        account_info_widget.layout().addWidget(verify_row)

        # Current username
        current_user_label = QLabel("Current username:")
        current_user_label.setStyleSheet("color: white; font-size: 15px;")
        verify_row.layout().addWidget(current_user_label)

        self.aco_enter1 = QLineEdit()
        self.aco_enter1.setPlaceholderText("enter your current username")
        self.aco_enter1.setFixedWidth(200)
        verify_row.layout().addWidget(self.aco_enter1)

        # Current password
        current_pass_label = QLabel("Current password:")
        current_pass_label.setStyleSheet("color: white; font-size: 15px;")
        verify_row.layout().addWidget(current_pass_label)

        self.aco_enter2 = QLineEdit()
        self.aco_enter2.setPlaceholderText("enter your current password")
        self.aco_enter2.setFixedWidth(200)
        verify_row.layout().addWidget(self.aco_enter2)


        # Update Section
        update_label = QLabel("Update account information")
        update_label.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        account_info_widget.layout().addWidget(update_label)

        update_row = QWidget()
        update_row.setLayout(QHBoxLayout())
        account_info_widget.layout().addWidget(update_row)

        # New username
        new_user_label = QLabel("New username:")
        new_user_label.setStyleSheet("color: white; font-size: 15px;")
        update_row.layout().addWidget(new_user_label)

        self.aco_enter3 = QLineEdit()
        self.aco_enter3.setPlaceholderText("enter new username")
        self.aco_enter3.setFixedWidth(200)
        update_row.layout().addWidget(self.aco_enter3)

        # New password
        new_pass_label = QLabel("New password:")
        new_pass_label.setStyleSheet("color: white; font-size: 15px;")
        update_row.layout().addWidget(new_pass_label)

        self.aco_enter4 = QLineEdit()
        self.aco_enter4.setPlaceholderText("enter new password")
        self.aco_enter4.setFixedWidth(200)
        update_row.layout().addWidget(self.aco_enter4)


        # Update button
        aco_btn = QPushButton("Update")
        aco_btn.setStyleSheet("""
            QPushButton {font-size: 15px; color: black; background-color: white; border-radius: 5px; padding: 5px 10px;}
            QPushButton:hover {background-color: #C4B9B9;}
        """)
        aco_btn.clicked.connect(self.update_userinfo)
        account_info_widget.layout().addWidget(aco_btn, alignment=Qt.AlignRight)


        # setting 
        setting_widget = QWidget()
        setting_widget.setLayout(QVBoxLayout())
        account_info_widget.layout().addWidget(setting_widget, 6)

        set_title = QLabel("Setting")
        set_title.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        setting_widget.layout().addWidget(set_title)

        tips_label = QLabel("You need to fill the verification part before deleting your account")
        tips_label.setStyleSheet("color: white; font-size: 20px;")
        setting_widget.layout().addWidget(tips_label)

        set_btn_widget = QWidget()
        set_btn_widget.setLayout(QVBoxLayout())
        setting_widget.layout().addWidget(set_btn_widget, alignment=Qt.AlignmentFlag.AlignTop)

        set_btn2 = QPushButton("Delete the account")
        set_btn2.setStyleSheet("""
        QPushButton {font-size: 15px; color: black; background-color: white; border-radius: 5px; padding: 5px 10px;}
        QPushButton:hover {background-color: #C4B9B9;}""")
        set_btn2.clicked.connect(self.delete_userinfo)
        set_btn_widget.layout().addWidget(set_btn2, alignment=Qt.AlignmentFlag.AlignLeft)

    
    # functions here

    # update userinfo function
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
    
    # delete userinfo function
    def delete_userinfo(self):
        current_username = self.aco_enter1.text().strip()
        current_password = self.aco_enter2.text().strip()

        if not current_username or not current_password:
            QMessageBox.warning(self, "Error", "Current username and password are required!")
            return

        confirm = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete account '{current_username}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm != QMessageBox.Yes:
            return

        try:
            deleted = delete_user_db1(current_username, current_password)
            if deleted:
                QMessageBox.information(self, "Success", "Account deleted successfully!")
                # optional: clear all fields
                self.aco_enter1.clear()
                self.aco_enter2.clear()
                self.aco_enter3.clear()
                self.aco_enter4.clear()
            else:
                QMessageBox.warning(self, "Error", "Username and password do not match!")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

        