import sqlite3

# Database for storing users' private information
db1_seechem = "userinfo.db"


def init_db1():
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()

    # users table
import sqlite3

db1_seechem = "userinfo.db"

def init_db1():
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()

    # Add notes column if missing
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN notes TEXT DEFAULT NULL")
        conn.commit()
    except sqlite3.OperationalError:
        # column already exists, do nothing
        pass

    # Add updated_at column if missing
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
        conn.commit()
    except sqlite3.OperationalError:
        # column already exists, do nothing
        pass

    conn.close()


# User management functions
def add_user_db1(username, password):
    try:
        conn = sqlite3.connect(db1_seechem)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        user_id = cursor.lastrowid
        return True, user_id
    except sqlite3.IntegrityError:
        return False, None
    finally:
        conn.close()

def check_user_db1(username, password):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def update_username(old_username, new_username):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET username=? WHERE username=?", (new_username, old_username))
        conn.commit()
        updated = cursor.rowcount
        conn.close()
        return updated > 0
    except sqlite3.IntegrityError:
        conn.close()
        return False

def update_password(username, new_password):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
    conn.commit()
    conn.close()
    return True

def delete_user_db1(username, password):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    
    # only delete if username AND password match
    cursor.execute("DELETE FROM users WHERE username=? AND password=?", (username, password))
    conn.commit()
    deleted = cursor.rowcount > 0  # check if a row was actually deleted
    conn.close()
    return deleted

def update_notes(username, notes):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET notes=?, updated_at=CURRENT_TIMESTAMP WHERE username=?", (notes, username))
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated

def get_notes(username):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    cursor.execute("SELECT notes FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result and result[0] is not None else ""


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

valence_electrons_db = {
    "H": 1, "He": 2,
    "Li": 1, "Be": 2, "B": 3, "C": 4, "N": 5, "O": 6, "F": 7, "Ne": 8,
    "P": 5, "S": 6, "Cl": 7, "Br": 7, "I": 7
}

vsepr_shapes_db = {
    (2, 0): "Linear",
    (3, 0): "Trigonal Planar",
    (2, 1): "Bent",
    (4, 0): "Tetrahedral",
    (3, 1): "Trigonal Pyramidal",
    (2, 2): "Bent",
    (5, 0): "Trigonal Bipyramidal",
    (4, 1): "See-Saw",
    (3, 2): "T-Shaped",
    (2, 3): "Linear",
    (6, 0): "Octahedral",
    (5, 1): "Square Pyramidal",
    (4, 2): "Square Planar"
}


def get_valence_electrons(element: str):
    return valence_electrons_db.get(element)


def get_vsepr_shape(bonds: int, lone_pairs: int):
    return vsepr_shapes_db.get((bonds, lone_pairs))