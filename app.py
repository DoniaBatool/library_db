import streamlit as st
import pandas as pd
from database import add_book, delete_book, update_book_status, get_books

# Streamlit Web UI
st.title("📚 Library Management System")

# Add a new book
st.header("➕ Add a New Book")
name = st.text_input("Book Name")
author = st.text_input("Author")
genre = st.text_input("Genre")
year = st.number_input("Publication Year", min_value=1800, max_value=2100, step=1)
read_status = st.radio("Read Status", ["Yes", "No"])

if st.button("Add Book"):
    if name and author and genre:
        add_book(name, author, genre, year, read_status)
        st.success("Book added successfully!")

# Show all books
st.header("📖 All Books")
books = get_books()
df = pd.DataFrame(books, columns=["ID", "Name", "Author", "Genre", "Year", "Read Status"])
st.dataframe(df)

# Delete a book
st.header("🗑️ Delete a Book")
book_id_delete = st.number_input("Enter Book ID to Delete", min_value=1, step=1)
if st.button("Delete Book"):
    delete_book(book_id_delete)
    st.warning("Book deleted successfully!")

# Update book status
st.header("📌 Update Read Status")
book_id_update = st.number_input("Enter Book ID to Update", min_value=1, step=1)
new_status = st.radio("New Read Status", ["Yes", "No"])
if st.button("Update Status"):
    update_book_status(book_id_update, new_status)
    st.success("Read status updated successfully!")

