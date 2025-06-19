from PyQt5.QtWidgets import QStackedWidget, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QMenuBar, QToolBar, QApplication
from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtSvg import QSvgWidget as qsvg
from PyQt5.QtCore import Qt, QRectF

# base, switch page and apply changes globally
class switch(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()
        self.setMinimumSize(1000, 625)
        self.setWindowTitle("SeeChem")

        self.welcome = welcome(self.switch_p)   # 0
        self.access = access(self.switch_p)     # 1
        self.home = home(self.switch_p)         # 2

        self.stack.addWidget(self.welcome)
        self.stack.addWidget(self.access)
        self.stack.addWidget(self.home)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
        layout.setContentsMargins(0,0,0,0) # to ensure the bg can perfectly fit the windows

    app_bg = QSvgRenderer("imagesource/app_bg.svg")

    def paintEvent(self, event):
        if self.stack.currentIndex() != 0 and self.stack.currentIndex() != 1: # prevent drawing other pages' bgs on welcome pg and access pg
            painter = QPainter(self)
            self.app_bg.render(painter, QRectF(self.rect()))

    def switch_p(self, index, mode=None):
        if index == 1 and mode:
            self.access = access(self.switch_p, mode)
            self.stack.removeWidget(self.stack.widget(1))
            self.stack.insertWidget(1, self.access)
        
        self.stack.setCurrentIndex(index)


# the welcome page (0)
class welcome(QWidget):
    def __init__(self, switch_func):
        super().__init__()

        self.setLayout(QHBoxLayout())
        self.welcome_bg = QSvgRenderer("imagesource/welcome_page_bg.svg")

        # content and image
        wel_1_widget = QWidget()
        wel_1_widget.setLayout(QVBoxLayout())
        self.layout().addWidget(wel_1_widget, 6)

        # text
        wel_title_widget = QWidget()
        wel_title_widget.setLayout(QVBoxLayout())
        wel_1_widget.layout().addWidget(wel_title_widget, 4, alignment=Qt.AlignmentFlag.AlignLeft)

        wel_title1 = QLabel("Welcome to SeeChem")
        wel_title_widget.layout().addWidget(wel_title1)
        wel_title1.setStyleSheet("font-family: 'poppins'; font-size: 80px; font-weight: bold; color: #DFF2EC;")


        wel_title2 = QLabel("where you start your chemistry")
        wel_title_widget.layout().addWidget(wel_title2)
        wel_title2.setStyleSheet("font-family: 'poppins'; font-size: 50px; color: #DFF2EC")

        # button

        wel_button_widget = QWidget()
        wel_button_widget.setLayout(QVBoxLayout())
        wel_1_widget.layout().addWidget(wel_button_widget, 3, alignment=Qt.AlignmentFlag.AlignLeft)


        wel_button1 = QPushButton("➔ Log in")
        wel_button1.setStyleSheet("font-size: 30px; text-align: left; " \
        "color: white; border: none; background-color: transparent;")
        wel_button_widget.layout().addWidget(wel_button1)
        wel_button1.clicked.connect(lambda: switch_func(1, "log in"))

        wel_button2 = QPushButton("➔ Create account")
        wel_button2.setStyleSheet("font-size: 30px; text-align: left; " \
        "color: white; border: none; background-color: transparent;")
        wel_button_widget.layout().addWidget(wel_button2)
        wel_button2.clicked.connect(lambda: switch_func(1, "create acc"))

        wel_button3 = QPushButton("➔ Continue as a guest")
        wel_button3.setStyleSheet("font-size: 30px; text-align: left; " \
        "color: white; border: none; background-color: transparent;")
        wel_button_widget.layout().addWidget(wel_button3)

        #logo
        wel_logo_widget = QWidget()
        wel_logo_widget.setBaseSize(150, 150)
        wel_logo_widget.setLayout(QVBoxLayout())
        wel_1_widget.layout().addWidget(wel_logo_widget, 3, alignment=Qt.AlignmentFlag.AlignLeft)

        wel_logo = qsvg("imagesource/SeeChemLogo.svg")
        wel_logo_widget.layout().addWidget(wel_logo)

        wel_txt1 = QLabel("SeeChem All Rights Reserved")
        wel_logo_widget.layout().addWidget(wel_txt1)
        wel_txt1.setStyleSheet("color: white;")

    # draw the bg
    def paintEvent(self, event):
        painter = QPainter(self)
        self.welcome_bg.render(painter, QRectF(self.rect()))



# the accesspage (1)
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
        acc_btn1.setStyleSheet("font-size: 15px; text-align: center; color: black; background-color: white; border-radius: 5px;")
        acc_btn_widget.layout().addWidget(acc_btn1)
        acc_btn1.clicked.connect(lambda: switch_func(0))

        if self.mode == "create acc":
            acc_btn2_name = "Create Account"
            acc_btn2_function = self.create_account
        else:
            acc_btn2_name = "Log in"
            acc_btn2_function = self.login

        acc_btn2 = QPushButton(acc_btn2_name)
        acc_btn2.setStyleSheet("font-size: 15px; text-align: center; color: black; background-color: white; border-radius: 5px;")
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
            QMessageBox.information(self, "Success", "Account created successfully!")
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
    

# the homepage (2)
class home(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.setLayout(QVBoxLayout())

        # text
        hom_caption1 = QLabel("Set up the experiments…")
        hom_caption1.setStyleSheet("font-family: LaoSangamMN; font-size: 50px; color: white;")
        self.layout().addWidget(hom_caption1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

        # buttons and recently created
        hom_content_widget = QWidget()
        hom_content_widget.setLayout(QHBoxLayout())
        self.layout().addWidget(hom_content_widget, 8)

        hom_btn_widget = QWidget()
        hom_btn_widget.setLayout(QVBoxLayout())
        hom_content_widget.layout().addWidget(hom_btn_widget, 5)

        hom_recent_widget = QWidget()
        hom_recent_widget.setLayout(QVBoxLayout())
        hom_content_widget.layout().addWidget(hom_recent_widget, 5)

        # home buttons

        # recently created
        recent_label = QLabel("Recently Created")
        recent_label.setStyleSheet("font-family: Galvji; font-size: 20px; color: white;")
        hom_recent_widget.layout().addWidget(recent_label, alignment=Qt.AlignmentFlag.AlignTop)

        back_button = QPushButton("Back to Welcome")
        self.layout().addWidget(back_button)
        back_button.clicked.connect(lambda: switch_func(0))



app = QApplication([])
window = switch()
appicon = QIcon("imagesource/SeeChem_icon.png") #set app icon
app.setWindowIcon(appicon)
window.show()

# run the app
app.exec_()