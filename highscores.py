import sqlite3
from datetime import datetime

class Highscores:
    def __init__(self, db_name="lingo.sqlite3"):
        """Maak verbinding met de database en creëer de highscores-tabel indien nodig."""
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        """Creëert de highscores-tabel als deze nog niet bestaat."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS highscores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                attempts INTEGER NOT NULL,
                time_elapsed REAL NOT NULL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def add_entry(self, name, score, attempts, time_elapsed):
        """Voegt een nieuwe highscore toe aan de database."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO highscores (name, score, attempts, time_elapsed, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, score, attempts, time_elapsed, datetime.now()))
        conn.commit()
        conn.close()
