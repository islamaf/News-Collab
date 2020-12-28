import sqlite3 as sql
from config import posts_db_path, users_db_path
# from app.posts_schema import sql_connection, posts_table
from app.schema import sql_connection, sql_table

con = sql.connect(users_db_path)
sql_table(con)

def news_post_insert(title, link, image, summary, like_count):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO News (title, link, image, summary, like_count) VALUES (?,?,?,?,?)",
                (title, link, image, summary, like_count))
    con.commit()
    con.close()


def sport_post_insert(title, link, image, summary, like_count):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO Sports (title, link, image, summary, like_count) VALUES (?,?,?,?,?)",
                (title, link, image, summary, like_count))
    con.commit()
    con.close()


def music_post_insert(title, link, image, summary, like_count):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO Music (title, link, image, summary, like_count) VALUES (?,?,?,?,?)",
                (title, link, image, summary, like_count))
    con.commit()
    con.close()


def lifestyle_post_insert(title, link, image, summary, like_count):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO Lifestyle (title, link, image, summary, like_count) VALUES (?,?,?,?,?)",
                (title, link, image, summary, like_count))
    con.commit()
    con.close()


def all_posts(title, link, image, summary, like_count):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO all_posts (title, link, image, summary, like_count) VALUES (?,?,?,?,?)",
                (title, link, image, summary, like_count))
    con.commit()
    con.close()

def check_post_news(title):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    exists = cur.execute("SELECT title FROM News WHERE title=?",
                      [title]).fetchone()
    con.commit()
    con.close()
    return exists

def check_post_sports(title):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    exists = cur.execute("SELECT title FROM Sports WHERE title=?",
                      [title]).fetchone()
    con.commit()
    con.close()
    return exists

def check_post_music(title):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    exists = cur.execute("SELECT title FROM Music WHERE title=?",
                      [title]).fetchone()
    con.commit()
    con.close()
    return exists

def check_post_lifestyle(title):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    exists = cur.execute("SELECT title FROM Lifestyle WHERE title=?",
                      [title]).fetchone()
    con.commit()
    con.close()
    return exists

# News table alteration
def retrieve_newsid(id):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    pid = cur.execute("SELECT id FROM News WHERE id=?",
                      [id]).fetchone()
    con.commit()
    con.close()
    return pid

def retrieve_newslikecount(id):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    likecount = cur.execute("SELECT like_count FROM News WHERE id=?",
                            [id]).fetchone()
    con.commit()
    con.close()
    return likecount

def news_update(task):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("UPDATE News SET like_count=? WHERE id=?", task)
    con.commit()
    con.close()

# Sports table alteration
def retrieve_sportsid(id):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    pid = cur.execute("SELECT id FROM Sports WHERE id=?",
                      [id]).fetchone()
    con.commit()
    con.close()
    return pid

def retrieve_sportslikecount(id):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    likecount = cur.execute("SELECT like_count FROM Sports WHERE id=?",
                            [id]).fetchone()
    con.commit()
    con.close()
    return likecount

def sports_update(task):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("UPDATE Sports SET like_count=? WHERE id=?", task)
    con.commit()
    con.close()

# Music table alteration
def retrieve_musicid(id):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    pid = cur.execute("SELECT id FROM Music WHERE id=?",
                      [id]).fetchone()
    con.commit()
    con.close()
    return pid

def retrieve_musiclikecount(id):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    likecount = cur.execute("SELECT like_count FROM Music WHERE id=?",
                            [id]).fetchone()
    con.commit()
    con.close()
    return likecount

def music_update(task):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("UPDATE Music SET like_count=? WHERE id=?", task)
    con.commit()
    con.close()

def retrieve_postid(id):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    pid = cur.execute("SELECT id FROM News WHERE id=?",
                      [id]).fetchone()
    con.commit()
    con.close()
    return pid

# Lifestyle table alteration
def retrieve_lifestyleid(id):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    pid = cur.execute("SELECT id FROM Lifestyle WHERE id=?",
                      [id]).fetchone()
    con.commit()
    con.close()
    return pid

def retrieve_lifestylelikecount(id):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    likecount = cur.execute("SELECT like_count FROM Lifestyle WHERE id=?",
                            [id]).fetchone()
    con.commit()
    con.close()
    return likecount

def lifestyle_update(task):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("UPDATE Lifestyle SET like_count=? WHERE id=?", task)
    con.commit()
    con.close()


def insert_liked_user(username, pid):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO post_like (username, post_id) VALUES (?,?)",
                           [username, pid])
    con.commit()
    con.close()


def retrieve_liked_user(username, pid):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    relation = cur.execute("SELECT username, post_id FROM post_like WHERE username = (?) AND post_id = (?)",
                           [username, pid]).fetchone()
    con.commit()
    con.close()
    return relation


def remove_liked_user(username, pid):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    relation = cur.execute("DELETE FROM post_like WHERE username = (?) AND post_id = (?)",
                           [username, pid]).fetchone()
    con.commit()
    con.close()
    return relation


def save_post(username, pid, title, link, image, summary):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO post_save (username, post_id, title, link, image, summary) VALUES (?,?,?,?,?,?)",
                [username, pid, title, link, image, summary])
    con.commit()
    con.close()


def unsave_post(username, title):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("DELETE FROM post_save WHERE username = (?) AND title = (?)",
                [username, title])
    con.commit()
    con.close()


def check_post(username, title):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    saved_post = cur.execute("SELECT username, title FROM post_save WHERE username = (?) AND title = (?)",
                             [username, title]).fetchone()
    con.commit()
    con.close()
    return saved_post


def get_post_info(pid):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    post_info = cur.execute("SELECT title, link, image, summary FROM News WHERE id = (?)",
                            [pid]).fetchone()
    con.commit()
    con.close()
    return post_info


def show_post(username):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    show = cur.execute("SELECT title, link, image, summary FROM post_save WHERE username = (?)",
                       [username]).fetchall()
    con.commit()
    con.close()
    return show


def insert_comment(post_id, username, body, timestamp):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO comments(post_id, username, body, post_time) VALUES (?,?,?,?)",
                    [post_id, username, body, str(timestamp)])
    con.commit()
    con.close()


def show_comment(post_id):
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    show = cur.execute("SELECT body FROM comments WHERE post_id = (?)",
                       [post_id]).fetchall()
    con.commit()
    con.close()
    return show


def display_best_news():
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    show = cur.execute("SELECT * FROM News ORDER BY like_count DESC").fetchall()
    con.commit()
    con.close()
    return show


def display_best_music():
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    show = cur.execute("SELECT * FROM Music ORDER BY like_count DESC").fetchall()
    con.commit()
    con.close()
    return show


def truncate():
    con = sql.connect(posts_db_path)
    cur = con.cursor()
    cur.execute("DELETE FROM all_posts")
    cur.execute("DELETE FROM News")
    cur.execute("DELETE FROM Music")
    cur.execute("DELETE FROM Lifestyle")
    con.commit()
    con.close()

