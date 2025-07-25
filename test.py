import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QGridLayout, QLabel, QToolTip, QMessageBox
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class PeriodicTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Periodic Table 1-20")
        self.resize(1100, 400)

        layout = QGridLayout()
        layout.setSpacing(5)
        self.setLayout(layout)

        # Element data: number, symbol, name, category, col, row
        elements = [
            (1, "H", "Hydrogen", "alkali-metal", 0, 0),
            (2, "He", "Helium", "noble-gas", 17, 0),

            (3, "Li", "Lithium", "alkali-metal", 0, 1),
            (4, "Be", "Beryllium", "alkaline-earth-metal", 1, 1),
            (5, "B", "Boron", "metalloid", 12, 1),
            (6, "C", "Carbon", "nonmetal", 13, 1),
            (7, "N", "Nitrogen", "nonmetal", 14, 1),
            (8, "O", "Oxygen", "nonmetal", 15, 1),
            (9, "F", "Fluorine", "halogen", 16, 1),
            (10, "Ne", "Neon", "noble-gas", 17, 1),

            (11, "Na", "Sodium", "alkali-metal", 0, 2),
            (12, "Mg", "Magnesium", "alkaline-earth-metal", 1, 2),
            (13, "Al", "Aluminum", "post-transition-metal", 12, 2),
            (14, "Si", "Silicon", "metalloid", 13, 2),
            (15, "P", "Phosphorus", "nonmetal", 14, 2),
            (16, "S", "Sulfur", "nonmetal", 15, 2),
            (17, "Cl", "Chlorine", "halogen", 16, 2),
            (18, "Ar", "Argon", "noble-gas", 17, 2),

            (19, "K", "Potassium", "alkali-metal", 0, 3),
            (20, "Ca", "Calcium", "alkaline-earth-metal", 1, 3),
        ]

        # Category colors
        colors = {
            "alkali-metal": "#ff6666",
            "alkaline-earth-metal": "#ffdead",
            "transition-metal": "#ffd700",
            "post-transition-metal": "#cccccc",
            "metalloid": "#aaffaa",
            "nonmetal": "#66ccff",
            "halogen": "#ffcc99",
            "noble-gas": "#99ccff",
        }

        for num, sym, name, cat, col, row in elements:
            btn = QPushButton(f"{sym}\n{num}")
            btn.setToolTip(f"{name} (Atomic Number: {num})")
            btn.setStyleSheet(f"background-color: {colors.get(cat, '#eee')}; font-weight: bold; font-size: 14px;")
            btn.setFixedSize(60, 60)

            # Example: on click show message box with element name and number
            btn.clicked.connect(lambda checked, n=num, nm=name: self.show_info(n, nm))

            layout.addWidget(btn, row, col)

    def show_info(self, number, name):
        QMessageBox.information(self, "Element Info", f"Element: {name}\nAtomic Number: {number}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PeriodicTable()
    window.show()
    sys.exit(app.exec_())
