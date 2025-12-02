import sqlite3
from pathlib import Path

DB_PATH = Path("data/local_data.db")

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS datasets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        path TEXT,
        uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()
    conn.close()

def insert_dataset(name, path):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO datasets (name, path) VALUES (?, ?)", (name, path))
    conn.commit()
    conn.close()
