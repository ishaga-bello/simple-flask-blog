import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as sql_file:
    connection.executescript(sql_file.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
    ('First Post', 'Content for the first post')
    )

cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
    ('Second Post', 'Content for the second post')
    )

connection.commit()
connection.close()