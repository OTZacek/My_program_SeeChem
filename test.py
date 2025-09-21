import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

DB_FILE = "users.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    # Insert 5 example users
    users = [("alice", "123"), ("bob", "456"), ("carol", "789"), ("dave", "abc"), ("eve", "xyz")]
    for u in users:
        c.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", u)
    conn.commit()
    conn.close()

class UpdateUserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update User Account")

        layout = QVBoxLayout()

        self.current_label = QLabel("Current Username:")
        self.current_input = QLineEdit()
        layout.addWidget(self.current_label)
        layout.addWidget(self.current_input)

        self.new_user_label = QLabel("New Username:")
        self.new_user_input = QLineEdit()
        layout.addWidget(self.new_user_label)
        layout.addWidget(self.new_user_input)

        self.new_pass_label = QLabel("New Password:")
        self.new_pass_input = QLineEdit()
        self.new_pass_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.new_pass_label)
        layout.addWidget(self.new_pass_input)

        self.update_button = QPushButton("Update")
        self.update_button.clicked.connect(self.update_user)
        layout.addWidget(self.update_button)

        self.setLayout(layout)

    def update_user(self):
        current_username = self.current_input.text().strip()
        new_username = self.new_user_input.text().strip()
        new_password = self.new_pass_input.text().strip()

        if not current_username or not new_username or not new_password:
            QMessageBox.warning(self, "Error", "All fields are required!")
            return

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()

        c.execute("UPDATE users SET username=?, password=? WHERE username=?",
                  (new_username, new_password, current_username))
        conn.commit()

        if c.rowcount == 0:  # No rows updated
            QMessageBox.warning(self, "Error", "User not found!")
        else:
            QMessageBox.information(self, "Success", "User updated successfully!")

        conn.close()

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    window = UpdateUserWindow()
    window.show()
    sys.exit(app.exec_())
