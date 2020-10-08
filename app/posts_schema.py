import sqlite3
from sqlite3 import Error
from config import posts_db_path

DATABASE = posts_db_path

con = sqlite3.connect(DATABASE)
cursorObj = con.cursor()

def sql_connection():
    try:
        con = sqlite3.connect(DATABASE)
        return con
    except Error:
        print(Error)

sql_connection()


def posts_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('''
        CREATE TABLE IF NOT EXISTS News(
            id INTEGER PRIMARY KEY,
            title VARCHAR(255),
            link VARCHAR(255),
            image VARCHAR(255),
            summary VARCHAR(255),
            like_count INTEGER
        );
    ''')

    cursorObj.execute('''
        CREATE TABLE IF NOT EXISTS Sports(
            id INTEGER PRIMARY KEY,
            title VARCHAR(255),
            link VARCHAR(255),
            image VARCHAR(255),
            summary VARCHAR(255),
            like_count INTEGER
        );
    ''')

    cursorObj.execute('''
        CREATE TABLE IF NOT EXISTS Music(
            id INTEGER PRIMARY KEY,
            title VARCHAR(255),
            link VARCHAR(255),
            image VARCHAR(255),
            summary VARCHAR(255),
            like_count INTEGER
        );
    ''')

    cursorObj.execute('''
        CREATE TABLE IF NOT EXISTS Lifestyle(
            id INTEGER PRIMARY KEY,
            title VARCHAR(255),
            link VARCHAR(255),
            image VARCHAR(255),
            summary VARCHAR(255),
            like_count INTEGER
        );
    ''')

    cursorObj.execute('''
        CREATE TABLE IF NOT EXISTS all_posts(
            id INTEGER PRIMARY KEY,
            title VARCHAR(255),
            link VARCHAR(255),
            image VARCHAR(255),
            summary VARCHAR(255),
            like_count INTEGER
        );
    ''')

    cursorObj.execute('''
        CREATE TABLE IF NOT EXISTS post_like(
            id INTEGER PRIMARY KEY,
            username VARCHAR(255),
            post_id INTEGER,
            FOREIGN KEY (username) REFERENCES Users(username),
            FOREIGN KEY (post_id) REFERENCES News(id)
        );
    ''')

    cursorObj.execute('''
        CREATE TABLE IF NOT EXISTS post_save(
            id INTEGER PRIMARY KEY,
            username VARCHAR(255),
            post_id INTEGER,
            title VARCHAR(255),
            link VARCHAR(255),
            image TEXT,
            summary TEXT,
            FOREIGN KEY (username) REFERENCES Users(username),
            FOREIGN KEY (post_id) REFERENCES News(id)
        );
    ''')

    con.commit()

