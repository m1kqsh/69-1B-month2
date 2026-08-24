import sqlite3


DB_NAME = "library.db"


def create_table(connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)
    connection.commit()


def insert_books(connection):
    books = [
        (
            "1984",
            "George Orwell",
            1949,
            "Dystopian",
            328,
            3
        ),
        (
            "The Hobbit",
            "J.R.R. Tolkien",
            1937,
            "Fantasy",
            310,
            4
        ),
        (
            "Pride and Prejudice",
            "Jane Austen",
            1813,
            "Romance",
            432,
            2
        ),
        (
            "The Great Gatsby",
            "F. Scott Fitzgerald",
            1925,
            "Classic",
            180,
            3
        ),
        (
            "Harry Potter and the Philosopher's Stone",
            "J.K. Rowling",
            1997,
            "Fantasy",
            223,
            5
        ),
        (
            "To Kill a Mockingbird",
            "Harper Lee",
            1960,
            "Drama",
            281,
            2
        ),
        (
            "The Catcher in the Rye",
            "J.D. Salinger",
            1951,
            "Classic",
            277,
            2
        ),
        (
            "The Little Prince",
            "Antoine de Saint-Exupery",
            1943,
            "Fiction",
            96,
            4
        ),
        (
            "Fahrenheit 451",
            "Ray Bradbury",
            1953,
            "Science Fiction",
            256,
            3
        ),
        (
            "The Alchemist",
            "Paulo Coelho",
            1988,
            "Adventure",
            208,
            3
        )
    ]

    for book in books:
        connection.execute("""
            INSERT INTO books (
                name,
                author,
                publication_year,
                genre,
                number_of_pages,
                number_of_copies
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, book)

    connection.commit()


if __name__ == "__main__":
    connection = sqlite3.connect(DB_NAME)

    create_table(connection)
    insert_books(connection)

    connection.close()

    print("Таблица books создана, 10 книг добавлены.")
