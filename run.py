from flask import Flask
from config import secret_key
import sqlite3 as sql

from app.home import home_bp
from app.login import login_bp
from app.leParser import parser_bp
from app.userProfile import user_bp

app = Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(parser_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.secret_key = secret_key
    app.run(host="0.0.0.0", debug=True)
