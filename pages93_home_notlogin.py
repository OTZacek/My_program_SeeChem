from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class n_home(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.switch_func = switch_func
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout().setSpacing(20)

        # Welcome text
        txt1 = QLabel("Looking forward to you joining!")
        txt1.setStyleSheet("font-size: 50px; color: white;")
        txt1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout().addWidget(txt1)

        # Container for image and buttons
        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        content_layout.setSpacing(20)
        content_widget.setLayout(content_layout)
        self.layout().addWidget(content_widget)

        # Demo image
        demo_label = QLabel()
        demo_img = QPixmap("imagesource/demonstration.png")
        if not demo_img.isNull():
            # Scale to width 400px while keeping aspect ratio
            demo_label.setPixmap(demo_img.scaledToWidth(650, Qt.TransformationMode.SmoothTransformation))
        demo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        content_layout.addWidget(demo_label)

        # Register button
        btn = QPushButton("Register Here")
        btn.setFixedWidth(200)
        btn.setStyleSheet("""
            QPushButton {
                font-size: 16px; color: black; 
                background-color: white; 
                border-radius: 8px; padding: 10px;
            }
            QPushButton:hover { background-color: #d3d3d3; }
        """)
        content_layout.addWidget(btn)
        btn.clicked.connect(lambda: switch_func(1))

        # Back button
        back_btn = QPushButton("Back to Welcome Page")
        back_btn.setFixedWidth(180)
        back_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px; color: black; 
                background-color: white; 
                border-radius: 5px; padding: 8px;
            }
            QPushButton:hover { background-color: #d3d3d3; }
        """)
        self.layout().addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        back_btn.clicked.connect(lambda: switch_func(0))
