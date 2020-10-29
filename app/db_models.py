import sqlite3 as sql
from config import users_db_path
from app.schema import sql_connection, sql_table

con = sql.connect(users_db_path)
sql_table(con)

def insertUser(username, email, password, confirm):
    con = sql.connect(users_db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO Users (username, email, password, confirm) VALUES (?,?,?,?)",
                (username, email, password, confirm))
    con.commit()
    con.close()

def retrieveUserName(username):
    con = sql.connect(users_db_path)
    cur = con.cursor()
    # Users = cur.execute("SELECT username, password FROM Users WHERE username=:username",
    #                     {"username": username, "password": password}).fetchone()
    Users = cur.execute("SELECT username FROM Users WHERE username = (?)", [username]).fetchone()
    con.close()
    return Users

def retrieveUserPassword(password):
    con = sql.connect(users_db_path)
    cur = con.cursor()
    Users = cur.execute("SELECT password FROM Users WHERE password = (?)", [password]).fetchone()
    con.close()
    return Users

def retrieveUsersRegister(username):
    con = sql.connect(users_db_path)
    cur = con.cursor()
    # Users = cur.execute("SELECT username FROM Users WHERE username=:username",
    #                     {"username": username}).fetchone()
    Users = cur.execute("SELECT username FROM Users WHERE username = (?)", [username]).fetchone()
    con.close()
    return Users
