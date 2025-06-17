from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QDialog, QLabel, QLineEdit, QHBoxLayout, QDialogButtonBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog Example")
        self.setMinimumSize(400, 300)

        # Main layout
        self.layout = QVBoxLayout()

        # Add a button to open the dialog
        self.open_dialog_button = QPushButton("Open Dialog")
        self.open_dialog_button.clicked.connect(self.show_dialog)
        self.layout.addWidget(self.open_dialog_button)

        # Set central widget
        central_widget = QPushButton()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def show_dialog(self):
        # Create and show the dialog
        dialog = InputDialog()
        if dialog.exec_() == QDialog.Accepted:  # If the dialog is accepted
            data = dialog.get_data()
            print("User Input:", data)


class InputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog")
        self.setMinimumSize(300, 200)

        # Dialog layout
        self.layout = QVBoxLayout()

        # Add input fields
        self.name_label = QLabel("Name:")
        self.layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_input)

        self.age_label = QLabel("Age:")
        self.layout.addWidget(self.age_label)

        self.age_input = QLineEdit()
        self.layout.addWidget(self.age_input)

        # Dialog buttons (OK and Cancel)
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)  # OK button action
        self.buttons.rejected.connect(self.reject)  # Cancel button action
        self.layout.addWidget(self.buttons)

        # Set the dialog layout
        self.setLayout(self.layout)

    def get_data(self):
        # Collect data from input fields
        return {
            "name": self.name_input.text(),
            "age": self.age_input.text(),
        }


# Run the application
app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec_()
