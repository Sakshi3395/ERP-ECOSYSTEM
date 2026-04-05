import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row # THis  lets u access columns by name
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # USER TABLE
    cursor.execute(
        """

    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    # EMPLYOEES 

    cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            role TEXT,
            salary REAL,
            bonus REAL
        )
    """
    )


    # ASSETS
    cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            value REAL,
            condition TEXT,
            expiry_date TEXT,
            is_active INTEGER DEFAULT 1
        )
    """
    )

    # ASSIGNMENT
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS asset_assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT,
        asset_id TEXT,
        FOREIGN KEY(employee_id) REFERENCES employees(id),
        FOREIGN KEY(asset_id) REFERENCES assets(id)
     )
    """
    )

    conn.commit()
    conn.close()