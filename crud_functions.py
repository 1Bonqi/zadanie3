import sqlite3


def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products


def check():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    check_db = cursor.execute('SELECT COUNT (*) FROM Products')
    if check_db.fetchone()[0] == 0:
        for i in range(1, 5):
            cursor.execute('INSERT INTO Products (title,description,price) VALUES (?,?,?)',
                           (f'product{i}', f'Описание {i}', i * 100))
    connection.commit()
    connection.close()


def add_user(username, email, age, balance=1000):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email,age,balance) '
                   'VALUES (?,?,?,?)', (username, email, age, balance))
    connection.commit()
    connection.close()


def is_include(username):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    check_name = cursor.execute(f'SELECT * FROM Users WHERE username=?', (username,))
    connection.commit()
    if check_name.fetchone():
        return True
    else:
        return False
