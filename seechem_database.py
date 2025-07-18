import sqlite3


# Database 1, for storing users' private information
db1_seechem = "userinfo.db"

# UNIQUE ensures no repeated usernames in the database
def init_db1():
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user_db1(username, password):
    try:
        conn = sqlite3.connect(db1_seechem)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:  # ensure code functions even if illegal characters or words be put in
        return False
    finally:
        conn.close()

def check_user_db1(username, password):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None