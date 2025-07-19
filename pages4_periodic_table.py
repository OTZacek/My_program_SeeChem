from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import Qt

from seechem_gfuncs import box_shadow

class periodic_table(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.setLayout(QHBoxLayout())

        periodic_table_content = QWidget()
        periodic_table_content.setLayout(QGridLayout())
        periodic_table_content.setStyleSheet("border-radius: 10px; background-color: #4428B9;")
        box_shadow(periodic_table_content)
        self.layout().addWidget(periodic_table_content, 6)

        temp_notice_label = QLabel("118 elements will be put here")
        periodic_table_content.layout().addWidget(temp_notice_label)

        element_info = QWidget()
        element_info.setLayout(QVBoxLayout())
        element_info.setStyleSheet("border-radius: 10px; background-color: #2035D6;")
        box_shadow(element_info)
        self.layout().addWidget(element_info, 1)

        # element_info_title = ("Name:", "Atomic Number:", "Relative Mass:", "Category:", "Description:")

        # elements = [
        #     (0, 0, "H"),
        #     (0, 17, "He"),
        #     (2, 1, "Li"),
        #     (2, 2, "Be"),
        #     (),
        #     (),
        #     (),
        #     (),
        #     (),
        #     (),

        # ]
        # haven't finished yet

        info_label = QLabel("Hover on an element to check the details of the element!")
        info_label.setStyleSheet("color:white;")
        element_info.layout().addWidget(info_label, alignment=Qt.AlignmentFlag.AlignLeft)