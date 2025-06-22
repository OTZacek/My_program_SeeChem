from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from PyQt5.QtGui import QPainter
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtCore import Qt, QRectF

class access(QWidget):
    def __init__(self, switch_func, mode="create acc"):
        super().__init__()
        self.setLayout(QVBoxLayout())

        self.mode = mode
        self.switch_func = switch_func

        # background image
        self.access_bg = QSvgRenderer("imagesource/access_page_bg.svg")

        # the interact window
        access_widget = QWidget()
        access_widget.setLayout(QVBoxLayout())
        access_widget.setMinimumSize(500, 250)
        self.layout().addWidget(access_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        # text
        acc_widget1 = QWidget()
        acc_widget1.setLayout(QHBoxLayout())
        access_widget.layout().addWidget(acc_widget1)

        acc_widget2 = QWidget()
        acc_widget2.setLayout(QHBoxLayout())
        access_widget.layout().addWidget(acc_widget2)

        acc_widget3 = QWidget()
        acc_widget3.setLayout(QVBoxLayout())
        acc_widget1.layout().addWidget(acc_widget3)

        acc_widget4 = QWidget()
        acc_widget4.setLayout(QVBoxLayout())
        acc_widget1.layout().addWidget(acc_widget4)

        acc_txt1_label = QLabel("Username:")
        acc_txt1_label.setStyleSheet("color: white; font-size: 15px;")
        acc_widget3.layout().addWidget(acc_txt1_label)

        self.acc_enter1 = QLineEdit()
        acc_widget4.layout().addWidget(self.acc_enter1)

        acc_txt2_label = QLabel("Password:")
        acc_txt2_label.setStyleSheet("color: white; font-size: 15px;")
        acc_widget3.layout().addWidget(acc_txt2_label)

        self.acc_enter2 = QLineEdit()
        acc_widget4.layout().addWidget(self.acc_enter2)

        # Confirm password (only for create mode)
        if self.mode == "create acc":
            acc_txt3_label = QLabel("Confirmed Password:")
            acc_txt3_label.setStyleSheet("color: white; font-size: 15px;")
            acc_widget3.layout().addWidget(acc_txt3_label)

            self.acc_enter3 = QLineEdit()
            acc_widget4.layout().addWidget(self.acc_enter3)
        
        # button
        acc_btn_widget = QWidget()
        acc_btn_widget.setLayout(QHBoxLayout())
        acc_widget2.layout().addWidget(acc_btn_widget)
        
        acc_btn1 = QPushButton("Back")
        acc_btn1.setStyleSheet("""
                               font-size: 15px; text-align: center; color: black; 
                               background-color: white; border-radius: 5px;
                               """)
        acc_btn_widget.layout().addWidget(acc_btn1)
        acc_btn1.clicked.connect(lambda: switch_func(0))

        if self.mode == "create acc":
            acc_btn2_name = "Create Account"
            acc_btn2_function = self.create_account
        else:
            acc_btn2_name = "Log in"
            acc_btn2_function = self.login

        acc_btn2 = QPushButton(acc_btn2_name)
        acc_btn2.setStyleSheet("""
                               font-size: 15px; text-align: center; color: black; 
                               background-color: white; border-radius: 5px;
                               """)
        acc_btn_widget.layout().addWidget(acc_btn2)
        acc_btn2.clicked.connect(acc_btn2_function)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        self.access_bg.render(painter, QRectF(self.rect()))

    def create_account(self):
        username = self.acc_enter1.text().strip()
        password = self.acc_enter2.text().strip()
        confirm_password = self.acc_enter3.text().strip()

        if not username or not password or not confirm_password:
            QMessageBox.warning(self, "Input Error", "All fields are required!")
            return
        
        if password != confirm_password:
            QMessageBox.warning(self, "Password Error", "Passwords do not match!")
            return
        
        try:
            with open("accounts.txt", "a") as file:
                file.write(f"{username},{password}\n")
            QMessageBox.information(self, "Success", "Welcome to SeeChem!")
            self.acc_enter1.clear()
            self.acc_enter2.clear()
            self.acc_enter3.clear()
        except Exception as e:  # error seeking
            QMessageBox.critical(self, "Error", f"An error occurred while saving the account: {e}")

        # log in function
    def login(self):
        username = self.acc_enter1.text().strip()
        password = self.acc_enter2.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Both fields are required!")
            return
        
        try:
            with open("accounts.txt", "r") as file:
                accounts = file.readlines()
                for account in accounts:
                    stored_username, stored_password = account.strip().split(",")
                    if username == stored_username and password == stored_password:
                        QMessageBox.information(self, "Success", "Login successful!")
                        self.switch_func(2)
                        return

            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "Accounts file not found!")
        except Exception as e:  # error seeking
            QMessageBox.critical(self, "Error", f"An error occurred during login: {e}")