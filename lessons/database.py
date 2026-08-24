import sqlite3


def create_tables(connection):
    # делаем sql запрос для создание таблицы student
    connection.execute('''
        CREATE TABLE students (
            id INTEGER,
            name TEXT,
            age INTEGER,
            city TEXT
        )   
    ''')

conn = sqlite3.connect("database.db") # .sqlite, .sqlite3
create_tables(conn)