# utils/database_config.py
import sqlite3

def initialize_db(db_path="database/feedback.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY,
        anime TEXT NOT NULL,
        rating INTEGER NOT NULL,
        comment TEXT
    )
    """)
    conn.commit()
    conn.close()

initialize_db()
