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
    return result is not None   # return True or False to tell whether successful login or not

def delete_user_db1(username, password):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()

# Database 2, stores some common chemical elements' molar masses
db2_elements = "elements.db"

def init_db2():
    conn = sqlite3.connect(db2_elements)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS elements (
            symbol TEXT PRIMARY KEY,
            molar_mass REAL NOT NULL
        )
    ''')

    elements_data = [
        ("H", 1.008), ("He", 4.0026), ("Li", 6.94), ("Be", 9.0122),
        ("B", 10.81), ("C", 12.01), ("N", 14.01), ("O", 16.00),
        ("F", 18.998), ("Ne", 20.18), ("Na", 22.99), ("Mg", 24.305),
        ("Al", 26.982), ("Si", 28.085), ("P", 30.974), ("S", 32.06),
        ("Cl", 35.45), ("Ar", 39.95), ("K", 39.10), ("Ca", 40.08),
        ("Fe", 55.845), ("Cu", 63.546), ("Zn", 65.38), ("Ag", 107.8682),
        ("I", 126.90), ("Ba", 137.33), ("Au", 196.97), ("Hg", 200.59),
        ("Pb", 207.2)
    ]
    # Ignore if the elements have been in the table
    cursor.executemany('''
        INSERT OR IGNORE INTO elements (symbol, molar_mass)
        VALUES (?, ?)
    ''', elements_data)

    conn.commit()
    conn.close()

def get_molar_mass_db2(symbol):
    conn = sqlite3.connect(db2_elements)
    cursor = conn.cursor()
    cursor.execute("SELECT molar_mass FROM elements WHERE symbol=?", (symbol,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    return None