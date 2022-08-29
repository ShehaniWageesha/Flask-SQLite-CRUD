import sqlite3
DATABASE_NAME = "test.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables = [
"""CREATE TABLE IF NOT EXISTS user(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nic TEXT NOT NULL,
  phone TEXT NOT NULL,
  password TEXT NOT NULL,
  qrcode TEXT,
  status INTEGER,
  lastlogin TEXT
)""",
"""CREATE TABLE IF NOT EXISTS course(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  fee REAL NOT NULL
)"""
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
