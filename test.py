import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt


class CustomMenuBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Custom Embedded Menu Bar")
        self.setGeometry(100, 100, 800, 600)

        # 主窗口布局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # 创建自定义菜单栏
        menu_bar = self.create_custom_menu_bar()
        layout.addWidget(menu_bar, 1)

        # 主内容区域
        content = QLabel("这里是主内容区域")
        content.setAlignment(Qt.AlignCenter)
        content.setStyleSheet("font-size: 18px; background-color: #f5f5f5;")
        layout.addWidget(content, 19)

    def create_custom_menu_bar(self):
        menu_bar = QWidget()
        menu_bar.setStyleSheet("""
            QWidget {
                background-color: #4CAF50;
                border-bottom: 2px solid #087F23;
            }
            QPushButton {
                color: white;
                background: transparent;
                font-size: 16px;
                border: none;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #66BB6A;
                border-radius: 5px;
            }
        """)

        # 菜单栏布局
        layout = QHBoxLayout(menu_bar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 添加按钮
        file_button = QPushButton("文件")
        file_button.clicked.connect(lambda: self.menu_action("文件"))
        layout.addWidget(file_button)

        edit_button = QPushButton("编辑")
        edit_button.clicked.connect(lambda: self.menu_action("编辑"))
        layout.addWidget(edit_button)

        help_button = QPushButton("帮助")
        help_button.clicked.connect(lambda: self.menu_action("帮助"))
        layout.addWidget(help_button)

        return menu_bar

    def menu_action(self, menu_name):
        print(f"{menu_name} 菜单被点击了！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CustomMenuBar()
    window.show()
    sys.exit(app.exec_())
