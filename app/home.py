from flask import Blueprint, render_template, session

home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/static/home_bp')

@home_bp.route('/')
def home():
    return render_template('splash.html')
    # return bbc_sport_parsing()

@home_bp.route('/home')
def home2():
    if session['logged_in']:
        session['logged_in'] = True
        username = session['username'].capitalize()
        return render_template('home.html', username=username)
    session['logged_in'] = False
    return render_template('home.html')

