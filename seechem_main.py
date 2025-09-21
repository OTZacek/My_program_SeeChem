from PyQt5.QtWidgets import QStackedWidget, QVBoxLayout, QWidget, QApplication
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtCore import QRectF
from func_menubar import seechem_menubar

from seechem_database import init_db1, init_db2

from pages1_welcome import welcome
from pages2_access import access
from pages3_home import calc_tools
from pages4_periodic_table import periodic_table
from pages5_account import account
from pages7_inLabs import inLabs
from pages93_home_notlogin import n_home

# base, switch page and apply changes globally
class switch(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()
        self.setMinimumSize(1000, 625)
        self.setWindowTitle("SeeChem")

        self.welcome = welcome(self.switch_p)
        self.access = access(self.switch_p)
        self.home = calc_tools(self.switch_p)
        self.periodic_table = periodic_table(self.switch_p)
        self.account = account(self.switch_p)
        self.inLabs = inLabs(self.switch_p)
        self.n_home = n_home(self.switch_p)

        self.stack.addWidget(self.welcome)          # 0
        self.stack.addWidget(self.access)           # 1
        self.stack.addWidget(self.home)             # 2
        self.stack.addWidget(self.periodic_table)   # 3
        self.stack.addWidget(self.account)          # 4
        self.stack.addWidget(self.inLabs)           # 5
        self.stack.addWidget(self.n_home)           # 6

        self.layout = QVBoxLayout(self)
        self.menubar = None # ensure no menubar initially
        self.layout.addWidget(self.stack)
        self.layout.setContentsMargins(0,0,0,0) # to ensure the bg can perfectly fit the windows

    app_bg = QSvgRenderer("imagesource/app_bg.svg")

    def paintEvent(self, event):
        if self.stack.currentIndex() not in [0,1]: # prevent drawing other pages' bgs on the pages don't need
            painter = QPainter(self)
            self.app_bg.render(painter, QRectF(self.rect()))

    def switch_p(self, index, mode=None):
        if index not in [0,1,6]:
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


# initiate the databases
init_db1()
init_db2()

app = QApplication([])
window = switch()
appicon = QIcon("imagesource/SeeChem_icon.png") #set app icon
app.setWindowIcon(appicon)
window.setMinimumSize(1000, 700)
window.show()

# run the app
app.exec_()