import psycopg2 
import os

def connect_db():
    """Connects to PostgreSQL database using environment variables."""
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        sslmode="require"
    )

# Function to Add a Book
def add_book(name, author, genre, year, read_status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (name, author, genre, year, read_status) VALUES (%s, %s, %s, %s, %s)",
                   (name, author, genre, year, read_status))
    conn.commit()
    conn.close()

# Function to Delete a Book
def delete_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    conn.close()

# Function to Update Read Status
def update_book_status(book_id, new_status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET read_status = %s WHERE id = %s", (new_status, book_id))
    conn.commit()
    conn.close()

# Function to Get All Books
def get_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

