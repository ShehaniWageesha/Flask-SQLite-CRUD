-- SQLite

-- Table Creations
CREATE TABLE IF NOT EXISTS user(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nic TEXT NOT NULL,
  phone TEXT NOT NULL,
  password TEXT NOT NULL,
  qrcode TEXT,
  status INTEGER,
  lastlogin TEXT
);

-- Drop Tables
DROP TABLE IF EXISTS user;
