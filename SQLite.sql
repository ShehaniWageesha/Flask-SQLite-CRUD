-- SQLite

-- Table Creations
CREATE TABLE IF NOT EXISTS user(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nic TEXT NOT NULL,
  name TEXT NOT NULL,
  phone TEXT NOT NULL,
  password TEXT NOT NULL,
  qrcode TEXT,
  status INTEGER,
  lastlogin TEXT
);

CREATE TABLE IF NOT EXISTS course(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  fee REAL NOT NULL
);

<<<<<<< HEAD
DROP TABLE IF EXISTS user;

=======
-- Drop Tables
DROP TABLE IF EXISTS user;
>>>>>>> 4296f23450a61961bfdfdddc49e1bfdf08891d79
