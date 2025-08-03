from PyQt5.QtWidgets import QMessageBox
import re
import math

from seechem_database import get_molar_mass_db2

# pH calc 1
def ph_from_h(h_conc: float) -> float:
    """Calculate pH from hydrogen ion concentration [H⁺]."""
    if h_conc <= 0:
        raise ValueError("[H⁺] must be positive")
    return -math.log10(h_conc)

def ph_from_oh(oh_conc: float) -> float:
    """Calculate pH from hydroxide ion concentration [OH⁻]."""
    if oh_conc <= 0:
        raise ValueError("[OH⁻] must be positive")
    poh = -math.log10(oh_conc)
    return 14 - poh

def concentrations_from_ph(ph: float) -> tuple[float, float]:
    """Calculate [H⁺] and [OH⁻] concentrations from pH value."""
    if not (0 <= ph <= 14):
        raise ValueError("pH must be between 0 and 14")
    h_conc = 10 ** (-ph)
    oh_conc = 10 ** (-(14 - ph))
    return h_conc, oh_conc

# pH calc 2
def calculate_ph(ph_edit, h_edit, oh_edit, result_label, parent_widget):
    ph_text = ph_edit.text().strip()
    h_text = h_edit.text().strip()
    oh_text = oh_edit.text().strip()

    filled = [bool(ph_text), bool(h_text), bool(oh_text)]
    if sum(filled) == 0:
        QMessageBox.warning(parent_widget, "Input error", "Please enter a value.")
        return
    if sum(filled) > 1:
        QMessageBox.warning(parent_widget, "Input error", "Please fill only one field.")
        return

    try:
        if ph_text:
            ph = float(ph_text)
            h, oh = concentrations_from_ph(ph)
            result_label.setText(f"pH = {ph:.2f}\n[H⁺] = {h:.4e} mol/L\n[OH⁻] = {oh:.4e} mol/L")
        elif h_text:
            h = float(h_text)
            ph = ph_from_h(h)
            oh = 10 ** (-(14 - ph))
            result_label.setText(f"[H⁺] = {h:.4e} mol/L\npH = {ph:.2f}\n[OH⁻] = {oh:.4e} mol/L")
        else:
            oh = float(oh_text)
            ph = ph_from_oh(oh)
            h = 10 ** (-ph)
            result_label.setText(f"[OH⁻] = {oh:.4e} mol/L\npH = {ph:.2f}\n[H⁺] = {h:.4e} mol/L")
    except ValueError:
        QMessageBox.warning(parent_widget, "Invalid input", "Please enter valid numbers.")

# molar mass calc
def calculate_molar_mass(formula_edit, result_label, parent_widget):
    formula = formula_edit.text().strip()
    if not formula:
        QMessageBox.warning(parent_widget, "Input error", "Please enter a chemical formula.")
        return

    pattern = r'([A-Z][a-z]?)(\d*)'
    parts = re.findall(pattern, formula)
    if not parts:
        QMessageBox.warning(parent_widget, "Input error", "Invalid chemical formula.")
        return

    try:
        total_mass = 0
        for element, count in parts:
            mass = get_molar_mass_db2(element)
            if mass is None:
                raise ValueError(f"Unknown element: {element}")
            n = int(count) if count else 1
            total_mass += mass * n
        result_label.setText(f"Molar Mass of {formula} = {total_mass:.3f} g/mol")
    except ValueError as e:
        QMessageBox.warning(parent_widget, "Error", str(e))