from PyQt5.QtWidgets import QStackedWidget, QVBoxLayout, QWidget, QApplication
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtCore import QRectF
from func_menubar import seechem_menubar

from pages1_welcome import welcome
from pages2_access import access
from pages3_home import home

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

        self.layout = QVBoxLayout(self)
        self.menubar = None # insure no menubar initially
        self.layout.addWidget(self.stack)
        self.layout.setContentsMargins(0,0,0,0) # to ensure the bg can perfectly fit the windows

    app_bg = QSvgRenderer("imagesource/app_bg.svg")

    def paintEvent(self, event):
        if self.stack.currentIndex() != 0 and self.stack.currentIndex() != 1: # prevent drawing other pages' bgs on welcome pg and access pg
            painter = QPainter(self)
            self.app_bg.render(painter, QRectF(self.rect()))

    def switch_p(self, index, mode=None):
        if index != 0 and index != 1:
            if not self.menubar:
                self.menubar = seechem_menubar(self.switch_p)
                self.layout.insertWidget(0, self.menubar)
        else:
            if self.menubar:
                self.layout.removeWidget(self.menubar)
                self.menubar.deleteLater()
                self.menubar = None

        if index == 1 and mode:
            self.access = access(self.switch_p, mode)
            self.stack.removeWidget(self.stack.widget(1))
            self.stack.insertWidget(1, self.access)
        
        self.stack.setCurrentIndex(index)


app = QApplication([])
window = switch()
appicon = QIcon("imagesource/SeeChem_icon.png") #set app icon
app.setWindowIcon(appicon)
window.show()

# run the app
app.exec_()