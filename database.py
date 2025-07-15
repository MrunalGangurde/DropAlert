import sqlite3
import os

DB_PATH = "prices.db"

def init_db():
    """Initialize SQLite DB and table"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            price REAL NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def store_price(url, price):
    """Store new price into DB"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO price_history (url, price) VALUES (?, ?)", (url, price))
    conn.commit()
    conn.close()

def get_latest_price(url):
    """Get the most recent price for a URL"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT price FROM price_history
        WHERE url = ?
        ORDER BY date DESC
        LIMIT 1
    """, (url,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None