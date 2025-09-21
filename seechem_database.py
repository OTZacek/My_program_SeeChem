import sqlite3

# Database for storing users' private information
db1_seechem = "userinfo.db"

current_logged_in_username = None

def set_current_user(username):
    global current_logged_in_username
    current_logged_in_username = username

def get_current_user():
    global current_logged_in_username
    return current_logged_in_username

def init_db1():
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()

    # users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            notes TEXT DEFAULT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
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

def delete_notes(username):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE users SET notes=NULL WHERE username=?", (username,))
    conn.commit()
    conn.close()
    return True

def delete_user_db1(username):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM users WHERE username=?", (username,))
    conn.commit()
    conn.close()
    return True

def view_notes(username, password):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    
    cursor.execute("SELECT notes FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    
    conn.close()
    return result[0] if result and result[0] is not None else "No notes found."

def delete_notes(username, password):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    
    # Verify user credentials first
    cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    
    if user:
        cursor.execute("UPDATE users SET notes=NULL, updated_at=CURRENT_TIMESTAMP WHERE username=?", (username,))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

def clear_all_notes(username, password):
    return delete_notes(username, password)

def get_user_stats(username, password):
    conn = sqlite3.connect(db1_seechem)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT username, LENGTH(notes) as notes_length, 
               created_at, updated_at 
        FROM users WHERE username=? AND password=?
    ''', (username, password))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return {
            'username': result[0],
            'notes_length': result[1] if result[1] else 0,
            'created_at': result[2],
            'last_updated': result[3]
        }
    else:
        return None











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