from PyQt5.QtWidgets import QStackedWidget, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QMenuBar, QToolBar, QApplication
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

        self.welcome = welcome(self.switch_p)
        self.home = home(self.switch_p)

        self.stack.addWidget(self.welcome)
        self.stack.addWidget(self.home)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
        layout.setContentsMargins(0,0,0,0) # to ensure the bg can perfectly fit the windows

    app_bg = QSvgRenderer("imagesource/app_bg.svg")

    def paintEvent(self, event):
        if self.stack.currentIndex() != 0: # prevent drawing other pages' bgs on welcome pg
            painter = QPainter(self)
            self.app_bg.render(painter, QRectF(self.rect()))

    def switch_p(self, index):
        self.stack.setCurrentIndex(index)


# the welcome page
class welcome(QWidget):
    def __init__(self, switch_func):
        super().__init__()

        self.setWindowTitle("Welcome!")
        self.setLayout(QHBoxLayout())
        self.welcome_bg = QSvgRenderer("imagesource/welcome_page_bg.svg")

        # content and image
        wel_1_widget = QWidget()
        wel_1_widget.setLayout(QVBoxLayout())
        self.layout().addWidget(wel_1_widget, 6)

        # text
        wel_title_widget = QWidget()
        wel_title_widget.setLayout(QVBoxLayout())
        wel_1_widget.layout().addWidget(wel_title_widget, alignment=Qt.AlignmentFlag.AlignLeft)

        wel_title1 = QLabel("Welcome to SeeChem")
        wel_title_widget.layout().addWidget(wel_title1)
        wel_title1.setStyleSheet("font-family: 'poppins'; font-size: 80px; font-weight: bold; color: #DFF2EC;")


        wel_title2 = QLabel("where you start your chemistry")
        wel_title_widget.layout().addWidget(wel_title2)
        wel_title2.setStyleSheet("font-family: 'poppins'; font-size: 50px; color: #DFF2EC")

        # button

        wel_button_widget = QWidget()
        wel_button_widget.setLayout(QVBoxLayout())
        wel_1_widget.layout().addWidget(wel_button_widget, alignment=Qt.AlignmentFlag.AlignLeft)


        wel_button1 = QPushButton("➔ Log in")
        wel_button1.setStyleSheet("QPushButton {font-size: 30px; text-align: left; " \
        "color: white; border: none; background-color: transparent;}")
        wel_button_widget.layout().addWidget(wel_button1)
        wel_button1.clicked.connect(lambda: switch_func(1))

        wel_button2 = QPushButton("➔ Create account")
        wel_button2.setStyleSheet("font-size: 30px; text-align: left; " \
        "color: white; border: none; background-color: transparent;")
        wel_button_widget.layout().addWidget(wel_button2)

        wel_button3 = QPushButton("➔ Continue as a guest")
        wel_button3.setStyleSheet("font-size: 30px; text-align: left; " \
        "color: white; border: none; background-color: transparent;")
        wel_button_widget.layout().addWidget(wel_button3)

        #logo
        wel_logo_widget = QWidget()
        wel_logo_widget.setBaseSize(150, 150)
        wel_logo_widget.setLayout(QVBoxLayout())
        wel_1_widget.layout().addWidget(wel_logo_widget, alignment=Qt.AlignmentFlag.AlignLeft)

        wel_logo = qsvg("imagesource/SeeChemLogo.svg")
        wel_logo_widget.layout().addWidget(wel_logo)

        wel_txt1 = QLabel("SeeChem All Rights Reserved")
        wel_logo_widget.layout().addWidget(wel_txt1)
        wel_txt1.setStyleSheet("color: white;")

    def paintEvent(self, event):
        painter = QPainter(self)
        self.welcome_bg.render(painter, QRectF(self.rect()))


# the homepage
class home(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.setLayout(QVBoxLayout())

        # menu bar
        menu_bar = QMenuBar(self)
        self.layout().addWidget(menu_bar)

        # tool bar
        tool_bar = QToolBar()
        self.layout().addWidget(tool_bar)

        # button
        home_logo = qsvg()
        home_button = QPushButton()

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