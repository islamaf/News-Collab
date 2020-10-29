import sqlite3
from sqlite3 import Error
from config import users_db_path

DATABASE = users_db_path

con = sqlite3.connect(DATABASE)
cursorObj = con.cursor()

def sql_connection():
    try:
        con = sqlite3.connect(DATABASE)
        return con
    except Error:
        print(Error)

sql_connection()

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            role_id INTEGER,
            username VARCHAR(20) NOT NULL,
            email TEXT NOT NULL,
            password VARCHAR(25) NOT NULL,
            confirm VARCHAR(25) NOT NULL
        );
    ''')

    cursorObj.execute('''
        CREATE TABLE IF NOT EXISTS RolesID (
            RoleID INTEGER PRIMARY KEY,
            RoleDescription VARCHAR(25)
        );
    ''')

    con.commit()

# con = sql_connection()
# sql_table(con)
