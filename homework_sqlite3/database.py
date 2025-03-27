import sqlite3

# database = sqlite3.connect('comments.db')
# cursor = database.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS comment(
#     postId INTEGER,
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     email CHAR(70),
#     body TEXT
#     )
#     ''')
# database.commit()
# database.close()

# database = sqlite3.connect('albums.db')
# cursor = database.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS album(
#     userId INTEGER,
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT)
#     ''')
# database.commit()
# database.close()


# database = sqlite3.connect('photos.db')
# cursor = database.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS photo(
#     albumId INTEGER,
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT,
#     url TEXT,
#     thumbnailUrl TEXT
#     )
#     ''')
# database.commit()
# database.close()

# database = sqlite3.connect('todos.db')
# cursor = database.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS todo(
#     userId INTEGER,
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT,
#     completed BOOLEAN
#     )
#     ''')
# database.commit()
# database.close()


database = sqlite3.connect('users.db')
cursor = database.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT,
    email TEXT,
    street TEXT,
    suite TEXT,
    city TEXT,
    zipcode TEXT,
    lat REAL,
    lng REAL,
    phone TEXT,
    website TEXT,
    company_name TEXT,
    company_catchphrase TEXT,
    company_bs TEXT
    )
    ''')
database.commit()
database.close()

