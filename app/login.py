from flask import Blueprint, request, session, render_template, flash, redirect
import sqlite3
import re

import app.db_models as dbHandler
from config import users_db_path
from app.home import home2, home_main

login_bp = Blueprint('login_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/static/login_bp')

con = sqlite3.connect(users_db_path)

@login_bp.route('/login')
def login_page():
    return render_template('login.html')

@login_bp.route('/register')
def register_page():
    return render_template('register.html')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username'].lower()
        password = request.form['password']

        user_auth = dbHandler.retrieveUserName(session['username'])
        if user_auth:
            user_pass = dbHandler.retrieveUserPassword(password)
            if user_pass:
                session['logged_in'] = True
                flash('Logged in!')
                # return render_template('home.html', username=(session['username']).capitalize())
                return redirect('/home')
            else:
                flash("Wrong password. Try again!")
                return render_template('login.html')
    else:
        return render_template('login.html')

@login_bp.route('/logout')
def logout():
    session['logged_in'] = False
    # return home_main()
    return redirect('/main')

@login_bp.route('/userRegistration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].lower()
        email = request.form['email'].lower()
        password = request.form['password']
        confirm = request.form['confirm']

        # Password validation
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    
        register_users = dbHandler.retrieveUsersRegister(username)
        if register_users is None:
            pat = re.compile(reg)
            mat = re.search(pat, password)
            if mat:    
                if password == confirm:
                    user = dbHandler.insertUser(username, email, password, confirm)
                    flash("You are registered, now you can login!", "success")
                    return render_template('login.html', user=user)
                else:
                    flash("Passwords does not match :(", "danger")
                    return render_template('register.html')
            else:
                flash("Password invalid. Please check conditions :(", "danger")
                return render_template('register.html')
        else:
            flash("User already exists, please login or contact admin", "danger")
            return render_template('login.html')
    return render_template('register.html')

con.close()