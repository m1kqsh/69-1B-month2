import sqlite3


DB_NAME = "library.db"


class Book:
    def __init__(self, name, author, year, genre, pages, copies):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        self.copies = copies

    def __str__(self):
        return f"{self.name} — {self.author}"


def create_table(connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            year INTEGER,
            genre TEXT,
            pages INTEGER,
            copies INTEGER
        )
    """)
    connection.commit()


def add_book(connection, book):
    connection.execute("""
        INSERT INTO books
        (name, author, year, genre, pages, copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        book.name,
        book.author,
        book.year,
        book.genre,
        book.pages,
        book.copies
    ))

    connection.commit()


if __name__ == "__main__":
    connection = sqlite3.connect(DB_NAME)

    create_table(connection)

    books = [
        Book("1984", "George Orwell", 1949, "Dystopian", 328, 3),
        Book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 4),
        Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", 180, 3)
    ]

    for book in books:
        add_book(connection, book)

    connection.close()

    print("База данных создана, книги добавлены.")
