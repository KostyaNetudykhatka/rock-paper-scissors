import sqlite3
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# 1
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT
)
""")

# 2.
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("1984", "George Orwell"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Harry Potter", "J.K. Rowling"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("The Hobbit", "J.R.R. Tolkien"))

conn.commit()

print("Список книг:")
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

for book in books:
    print(book)

# 3
delete_id = int(input("Введіть id книги для видалення: "))
cursor.execute("DELETE FROM books WHERE id = ?", (delete_id,))
conn.commit()

print("Книга видалена.")

cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

print("Список після видалення:")
for book in books:
    print(book)

conn.close()