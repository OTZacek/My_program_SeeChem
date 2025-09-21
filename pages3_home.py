from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QFormLayout
from PyQt5.QtCore import Qt

from seechem_wfuncs import calculate_ph, calculate_molar_mass, find_shape, calculate_percent_composition
from seechem_gfuncs import box_shadow


class calc_tools(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # top, pH & Molar
        top_widget = QWidget()
        top_layout = QHBoxLayout()
        top_widget.setLayout(top_layout)
        main_layout.addWidget(top_widget, stretch=2)

        # down, shape
        down_widget = QWidget()
        down_layout = QHBoxLayout()
        down_widget.setLayout(down_layout)
        main_layout.addWidget(down_widget, stretch=2)

        # 1. pH CALCULATOR
        ph_widget = QWidget()
        ph_layout = QVBoxLayout()
        ph_widget.setLayout(ph_layout)
        top_layout.addWidget(ph_widget, stretch=1)

        # Title
        ph_title = QLabel("1. pH and Ion Calculator")
        ph_title.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        ph_layout.addWidget(ph_title, alignment=Qt.AlignLeft)
        box_shadow(ph_title)

        # Formula input using FormLayout
        ph_form = QFormLayout()
        ph_form.setLabelAlignment(Qt.AlignLeft)
        ph_form.setFormAlignment(Qt.AlignLeft)

        self.ph_edit = QLineEdit()
        self.h_edit = QLineEdit()
        self.oh_edit = QLineEdit()

        self.ph_edit.setPlaceholderText("Enter pH (0-14)")
        self.h_edit.setPlaceholderText("Enter [H⁺] (mol/L)")
        self.oh_edit.setPlaceholderText("Enter [OH⁻] (mol/L)")

        self.ph_edit.setFixedWidth(200)
        self.h_edit.setFixedWidth(200)
        self.oh_edit.setFixedWidth(200)

        ph_form.addRow("pH:", self.ph_edit)
        ph_form.addRow("[H⁺]:", self.h_edit)
        ph_form.addRow("[OH⁻]:", self.oh_edit)
        ph_layout.addLayout(ph_form)

        # Calculate button
        calc_btn = QPushButton("Calculate")
        calc_btn.setStyleSheet("""
        QPushButton {font-size: 16px; color: black; background-color: white; 
        border-radius: 5px; padding: 5px 10px;}
        QPushButton:hover {background-color: #C4B9B9;}
        """)

        # Connect button to function
        calc_btn.clicked.connect(lambda: calculate_ph(self.ph_edit, self.h_edit, self.oh_edit, self.result, self))
        ph_layout.addWidget(calc_btn, alignment=Qt.AlignLeft)

        # Result label
        self.result = QLabel("")
        self.result.setStyleSheet("color: white; font-size: 16px;")
        self.result.setWordWrap(True)
        ph_layout.addWidget(self.result, alignment=Qt.AlignLeft)

        # 2. MOLAR MASS CALCULATOR
        molar_widget = QWidget()
        molar_layout = QVBoxLayout()
        molar_widget.setLayout(molar_layout)
        top_layout.addWidget(molar_widget, stretch=1)

        molar_title = QLabel("2. Molar Mass Calculator")
        molar_title.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        molar_layout.addWidget(molar_title, alignment=Qt.AlignLeft)
        box_shadow(molar_title)

        molar_form = QFormLayout()
        molar_form.setLabelAlignment(Qt.AlignLeft)
        molar_form.setFormAlignment(Qt.AlignLeft)

        self.formula_edit = QLineEdit()
        self.formula_edit.setPlaceholderText("e.g. H2SO4")
        self.formula_edit.setFixedWidth(200)
        molar_form.addRow("Formula:", self.formula_edit)
        molar_layout.addLayout(molar_form)

        molar_calc_btn = QPushButton("Calculate")
        molar_calc_btn.setStyleSheet("""
        QPushButton {font-size: 16px; color: black; background-color: white; 
        border-radius: 5px; padding: 5px 10px;}
        QPushButton:hover {background-color: #C4B9B9;}
        """)
        molar_calc_btn.clicked.connect(lambda: calculate_molar_mass(self.formula_edit, self.molar_result, self))
        molar_layout.addWidget(molar_calc_btn, alignment=Qt.AlignLeft)

        self.molar_result = QLabel("")
        self.molar_result.setStyleSheet("color: white; font-size: 16px;")
        self.molar_result.setWordWrap(True)
        molar_layout.addWidget(self.molar_result, alignment=Qt.AlignLeft)

        # 3. SHAPE FINDER
        shape_widget = QWidget()
        shape_layout = QVBoxLayout()
        shape_widget.setLayout(shape_layout)
        down_layout.addWidget(shape_widget, stretch=1)

        shape_title = QLabel("3. Shape finder")
        shape_title.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        shape_layout.addWidget(shape_title, alignment=Qt.AlignLeft)
        box_shadow(shape_title)

        shape_form_widget = QWidget()
        shape_form_layout = QFormLayout()
        shape_form_layout.setLabelAlignment(Qt.AlignLeft)
        shape_form_layout.setFormAlignment(Qt.AlignLeft)
        shape_form_widget.setLayout(shape_form_layout)

        self.shape_formula_edit = QLineEdit()
        self.shape_formula_edit.setPlaceholderText("e.g. CH4")
        self.shape_formula_edit.setFixedWidth(200)
        shape_form_layout.addRow("Formula:", self.shape_formula_edit)
        shape_layout.addWidget(shape_form_widget)

        shape_find_btn = QPushButton("Calculate")
        shape_find_btn.setStyleSheet("""
        QPushButton {font-size: 16px; color: black; background-color: white; 
        border-radius: 5px; padding: 5px 10px;}
        QPushButton:hover {background-color: #C4B9B9;}
        """)
        shape_find_btn.clicked.connect(lambda: find_shape(self.shape_formula_edit, self.shape_result, self))
        shape_layout.addWidget(shape_find_btn, alignment=Qt.AlignLeft)

        self.shape_result = QLabel("")
        self.shape_result.setStyleSheet("color: white; font-size: 16px;")
        self.shape_result.setWordWrap(True)
        shape_layout.addWidget(self.shape_result, alignment=Qt.AlignLeft)

        # 4. Percent Composition Calculator
        percent_widget = QWidget()
        percent_layout = QVBoxLayout()
        percent_widget.setLayout(percent_layout)
        down_layout.addWidget(percent_widget, stretch=1)

        percent_title = QLabel("4. Percent Composition Calculator")
        percent_title.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        percent_layout.addWidget(percent_title, alignment=Qt.AlignLeft)
        box_shadow(percent_title)

        percent_form = QFormLayout()
        percent_form.setLabelAlignment(Qt.AlignLeft)
        percent_form.setFormAlignment(Qt.AlignLeft)

        percent_formula_edit = QLineEdit()
        percent_formula_edit.setPlaceholderText("e.g. C6H12O6")
        percent_formula_edit.setFixedWidth(200)
        percent_form.addRow("Formula:", percent_formula_edit)
        percent_layout.addLayout(percent_form)

        percent_calc_btn = QPushButton("Calculate")
        percent_calc_btn.setStyleSheet("""
        QPushButton {font-size: 16px; color: black; background-color: white; 
        border-radius: 5px; padding: 5px 10px;}
        QPushButton:hover {background-color: #C4B9B9;}
        """)
        percent_layout.addWidget(percent_calc_btn, alignment=Qt.AlignLeft)

        percent_result = QLabel("")
        percent_result.setStyleSheet("color: white; font-size: 16px;")
        percent_result.setWordWrap(True)
        percent_layout.addWidget(percent_result, alignment=Qt.AlignLeft)

        percent_calc_btn.clicked.connect(lambda: calculate_percent_composition(percent_formula_edit, percent_result, percent_widget))
