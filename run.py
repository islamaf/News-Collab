from flask import Flask
from config import secret_key

from app.home import home_bp

app = Flask(__name__)
app.register_blueprint(home_bp)

if __name__ == "__main__":
    app.secret_key = secret_key
    app.run(debug=True)
