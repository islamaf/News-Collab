from flask import Blueprint, render_template, session, request, redirect

import app.interaction as interactionHandler
home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/static/home_bp')

@home_bp.route('/')
def home():
    return render_template('splash.html')
    # return bbc_sport_parsing()

best_news = interactionHandler.display_best_news()
best_music = interactionHandler.display_best_music()
best_sports = interactionHandler.display_best_sports()
best_lifestyle = interactionHandler.display_best_lifestyle()

@home_bp.route('/main')
def home_main():
    session['logged_in'] = False
    return render_template('home.html', best_news=best_news, best_music=best_music, best_sports=best_sports, best_lifestyle=best_lifestyle)

@home_bp.route('/home')
def home2():
    if session['logged_in']:
        session['logged_in'] = True
        username = session['username'].capitalize()
        return render_template('home.html', username=username, best_news=best_news, best_music=best_music, best_sports=best_sports, best_lifestyle=best_lifestyle)
    # return render_template('home.html', best_news=best_news, best_music=best_music)
    return redirect('/home')
