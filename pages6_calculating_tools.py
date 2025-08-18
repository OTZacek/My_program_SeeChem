from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt

from seechem_wfuncs import calculate_ph, calculate_molar_mass


class calc_tools(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        self.setLayout(QVBoxLayout())

        top_widget = QWidget()
        top_widget.setLayout(QHBoxLayout())
        self.layout().addWidget(top_widget, 5)

        down_widget = QWidget()
        down_widget.setLayout(QHBoxLayout())
        self.layout().addWidget(down_widget, 5)

        # top
        ph_widget = QWidget()
        ph_widget.setLayout(QVBoxLayout())
        top_widget.layout().addWidget(ph_widget, 5)

        molar_widget = QWidget()
        molar_widget.setLayout(QVBoxLayout())
        top_widget.layout().addWidget(molar_widget, 5)

        # down
        shape_widget = QWidget()
        shape_widget.setLayout(QVBoxLayout())
        down_widget.layout().addWidget(shape_widget, 5)



# PH CALC UI
        title_widget = QWidget()
        title_widget.setLayout(QVBoxLayout())
        ph_widget.layout().addWidget(title_widget)

        title = QLabel("1. pH and Ion Calculator")
        title.setStyleSheet("font-size: 26px; font-weight: bold; color: white;")
        title_widget.layout().addWidget(title, alignment=Qt.AlignLeft)

        ph_input_widget = QWidget()
        ph_input_widget.setLayout(QHBoxLayout())
        ph_widget.layout().addWidget(ph_input_widget)

        ph_label = QLabel("pH:")
        ph_label.setStyleSheet("color: white; font-size: 16px;")
        ph_input_widget.layout().addWidget(ph_label)

        self.ph_edit = QLineEdit()
        self.ph_edit.setPlaceholderText("Enter pH (0-14)")
        self.ph_edit.setFixedWidth(200)
        ph_input_widget.layout().addWidget(self.ph_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        h_input_widget = QWidget()
        h_input_widget.setLayout(QHBoxLayout())
        ph_widget.layout().addWidget(h_input_widget)

        h_label = QLabel("[H⁺]:")
        h_label.setStyleSheet("color: white; font-size: 16px;")
        h_input_widget.layout().addWidget(h_label)

        self.h_edit = QLineEdit()
        self.h_edit.setPlaceholderText("Enter [H⁺] (mol/L)")
        self.h_edit.setFixedWidth(200)
        h_input_widget.layout().addWidget(self.h_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        oh_input_widget = QWidget()
        oh_input_widget.setLayout(QHBoxLayout())
        ph_widget.layout().addWidget(oh_input_widget)

        oh_label = QLabel("[OH⁻]:")
        oh_label.setStyleSheet("color: white; font-size: 16px;")
        oh_input_widget.layout().addWidget(oh_label)

        self.oh_edit = QLineEdit()
        self.oh_edit.setPlaceholderText("Enter [OH⁻] (mol/L)")
        self.oh_edit.setFixedWidth(200)
        oh_input_widget.layout().addWidget(self.oh_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        button_widget = QWidget()
        button_widget.setLayout(QVBoxLayout())
        ph_widget.layout().addWidget(button_widget)

        calc_btn = QPushButton("Calculate")
        calc_btn.setStyleSheet("""
        QPushButton {font-size: 16px; color: black; background-color: white; border-radius: 5px; padding: 5px 10px;}
        QPushButton:hover {background-color: #C4B9B9;}
        """)
        button_widget.layout().addWidget(calc_btn, alignment=Qt.AlignLeft)
        calc_btn.clicked.connect(lambda: calculate_ph(self.ph_edit, self.h_edit, self.oh_edit, self.result, self))

        # show the calculation results
        result_widget = QWidget()
        result_widget.setLayout(QVBoxLayout())
        ph_widget.layout().addWidget(result_widget)

        self.result = QLabel("")
        self.result.setStyleSheet("color: white; font-size: 16px;")
        self.result.setWordWrap(True)
        result_widget.layout().addWidget(self.result, alignment=Qt.AlignLeft)

        bottom_widget = QWidget()
        self.layout().addWidget(bottom_widget, 5)


# MOLAR MASS UI
        molar_title_widget = QWidget()
        molar_title_widget.setLayout(QVBoxLayout())
        molar_widget.layout().addWidget(molar_title_widget)

        molar_title = QLabel("2. Molar Mass Calculator")
        molar_title.setStyleSheet("font-size: 26px; font-weight: bold; color: white;")
        molar_title_widget.layout().addWidget(molar_title, alignment=Qt.AlignLeft)

        formula_widget = QWidget()
        formula_widget.setLayout(QHBoxLayout())
        molar_widget.layout().addWidget(formula_widget)

        formula_label = QLabel("Formula:")
        formula_label.setStyleSheet("color: white; font-size: 16px;")
        formula_widget.layout().addWidget(formula_label)

        self.formula_edit = QLineEdit()
        self.formula_edit.setPlaceholderText("e.g. H2SO4")
        self.formula_edit.setFixedWidth(200)
        formula_widget.layout().addWidget(self.formula_edit, alignment=Qt.AlignCenter)

        molar_button_widget = QWidget()
        molar_button_widget.setLayout(QVBoxLayout())
        molar_widget.layout().addWidget(molar_button_widget)

        molar_calc_btn = QPushButton("Calculate")
        molar_calc_btn.setStyleSheet("""
        QPushButton {font-size: 16px; color: black; background-color: white; border-radius: 5px; padding: 5px 10px;}
        QPushButton:hover {background-color: #C4B9B9;}
        """)
        molar_button_widget.layout().addWidget(molar_calc_btn, alignment=Qt.AlignLeft)
        molar_calc_btn.clicked.connect(lambda: calculate_molar_mass(self.formula_edit, self.molar_result, self))

        # show the calculation results
        molar_result_widget = QWidget()
        molar_result_widget.setLayout(QVBoxLayout())
        molar_widget.layout().addWidget(molar_result_widget)

        self.molar_result = QLabel("")
        self.molar_result.setStyleSheet("color: white; font-size: 16px;")
        self.molar_result.setWordWrap(True)
        molar_result_widget.layout().addWidget(self.molar_result, alignment=Qt.AlignLeft)


# # SHAPE FINDER UI
#         shape_title_widget = QWidget()
#         shape_title_widget.setLayout(QVBoxLayout())
#         shape_widget.layout().addWidget(shape_title_widget)

#         shape_title = QLabel("2. Shape Finder")
#         shape_title.setStyleSheet("font-size: 26px; font-weight: bold; color: white;")
#         shape_title_widget.layout().addWidget(shape_title, alignment=Qt.AlignLeft)

#         shape_formula_widget = QWidget()
#         shape_formula_widget.setLayout(QHBoxLayout())
#         shape_widget.layout().addWidget(shape_formula_widget)

#         shape_formula_label = QLabel("Formula:")
#         shape_formula_label.setStyleSheet("color: white; font-size: 16px;")
#         shape_formula_widget.layout().addWidget(shape_formula_label)

#         self.shape_formula_edit = QLineEdit()
#         self.shape_formula_edit.setPlaceholderText("e.g. CH4")
#         self.shape_formula_edit.setFixedWidth(200)
#         shape_formula_widget.layout().addWidget(self.shape_formula_edit, alignment=Qt.AlignCenter)

#         shape_button_widget = QWidget()
#         shape_button_widget.setLayout(QVBoxLayout())
#         shape_widget.layout().addWidget(shape_button_widget)

#         shape_find_btn = QPushButton("Calculate")
#         shape_find_btn.setStyleSheet("""
#         QPushButton {font-size: 16px; color: black; background-color: white; border-radius: 5px; padding: 5px 10px;}
#         QPushButton:hover {background-color: #C4B9B9;}
#         """)
#         shape_button_widget.layout().addWidget(shape_find_btn, alignment=Qt.AlignLeft)
#         shape_find_btn.clicked.connect(lambda: calculate_molar_mass(self.shape_formula_edit, self.shape_result, self))

#         # show the calculation results
#         shape_result_widget = QWidget()
#         shape_result_widget.setLayout(QVBoxLayout())
#         shape_widget.layout().addWidget(shape_result_widget)

#         self.shape_result = QLabel("")
#         self.shape_result.setStyleSheet("color: white; font-size: 16px;")
#         self.shape_result.setWordWrap(True)
#         shape_result_widget.layout().addWidget(self.shape_result, alignment=Qt.AlignLeft)
        