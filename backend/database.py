import sqlite3
from datetime import datetime
from typing import List, Dict, Any
import json

DB_NAME = "history.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  date TEXT,
                  score INTEGER,
                  level TEXT,
                  details TEXT)''')
    conn.commit()
    conn.close()

def save_result(score: int, level: str, details: str):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO history (date, score, level, details) VALUES (?, ?, ?, ?)",
              (date_str, score, level, details))
    conn.commit()
    conn.close()

def get_history() -> List[Dict[str, Any]]:
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM history ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]
