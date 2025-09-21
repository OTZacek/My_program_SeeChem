from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt

class n_home(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.switch_func = switch_func
        self.setLayout(QVBoxLayout())

        # text
        txt1 = QLabel("Looking forward for your joining!")
        txt1.setStyleSheet("font-size: 50px; color: white;")
        self.layout().addWidget(txt1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

        # buttons container
        btn_container = QWidget()
        btn_container.setLayout(QHBoxLayout())
        self.layout().addWidget(btn_container)

        # Button 1
        btn1 = QPushButton("Periodic Table")
        btn1.setStyleSheet("""
            QPushButton {
                font-size: 16px; color: black; 
                background-color: white; 
                border-radius: 8px; padding: 15px;
                min-width: 150px;
            }
            QPushButton:hover { background-color: #45a049; }
        """)
        btn_container.layout().addWidget(btn1)
        btn1.clicked.connect(lambda: switch_func(3))

        # Button 2
        btn2 = QPushButton("Useful Tools")
        btn2.setStyleSheet("""
            QPushButton {
                font-size: 16px; color: black; 
                background-color: white; 
                border-radius: 8px; padding: 15px;
                min-width: 150px;
            }
            QPushButton:hover { background-color: #1976D2; }
        """)
        btn_container.layout().addWidget(btn2)
        btn2.clicked.connect(lambda: switch_func(5))

        # Button 3
        btn3 = QPushButton("If in Lab")
        btn3.setStyleSheet("""
            QPushButton {
                font-size: 16px; color: black; 
                background-color: white; 
                border-radius: 8px; padding: 15px;
                min-width: 150px;
            }
            QPushButton:hover { background-color: #F57C00; }
        """)
        btn_container.layout().addWidget(btn3)
        btn3.clicked.connect(lambda: switch_func(6))

        # Back button
        back_btn = QPushButton("Back to Welcome Page")
        back_btn.setStyleSheet("""
            QPushButton {
                font-size: 13px; color: black; 
                background-color: white; 
                border-radius: 5px; padding: 10px;
            }
            QPushButton:hover { background-color: #e0e0e0; }
        """)
        self.layout().addWidget(back_btn)
        back_btn.clicked.connect(lambda: switch_func(0))