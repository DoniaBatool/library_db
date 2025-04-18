import sqlite3
import os

# Database file path
DB_PATH = os.path.join(os.path.dirname(__file__), "library.db")

def connect_db():
    """Connect to (or create) SQLite database."""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn

# Ensure table exists
with connect_db() as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            genre TEXT,
            year INTEGER,
            read_status TEXT
        )
    """)
    conn.commit()

def add_book(name, author, genre, year, read_status):
    conn = connect_db()
    conn.execute(
        "INSERT INTO books (name, author, genre, year, read_status) VALUES (?, ?, ?, ?, ?)",
        (name, author, genre, year, read_status)
    )
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = connect_db()
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

def update_book_status(book_id, new_status):
    conn = connect_db()
    conn.execute("UPDATE books SET read_status = ? WHERE id = ?", (new_status, book_id))
    conn.commit()
    conn.close()

def get_books():
    conn = connect_db()
    cursor = conn.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books
