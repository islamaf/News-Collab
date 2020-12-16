from flask import Blueprint, request, session, render_template, flash, redirect, json, url_for
import sqlite3 as sql
from datetime import datetime

from app.home import home2
import app.interaction as interactionHandler
from config import users_db_path

user_bp = Blueprint('user_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/static/user_bp')

# con = sqlite3.connect(users_db_path)
# con = sql.connect(users_db_path)

@user_bp.route('/user_profile')
def user_profile():
    username = session['username'].capitalize()

    show_post = interactionHandler.show_post(username.lower())

    titles = []
    links = []
    images = []
    summaries = []

    for i in show_post:
        titles.append(i[0])
        images.append(i[1])
        links.append(i[2])
        summaries.append(i[3])

    return render_template('user_profile.html', username=username, len=len(titles), titles=titles,
                           links=links, images=images, summaries=summaries)

# News interaction
@user_bp.route('/news_like', methods=['GET', 'POST'])
def news_like():
    if request.method == "POST":
        username = session['username']

        data_received = json.loads(request.data)
        post = interactionHandler.retrieve_newsid(data_received['postid'])
        like_count = interactionHandler.retrieve_newslikecount(data_received['postid'])
        like_count = like_count[0]

        relation = interactionHandler.retrieve_liked_user(username, data_received['postid'])
        if relation is None:
            if post:
                like_count = like_count + 1
                interactionHandler.news_update((like_count, data_received['postid']))
                interactionHandler.insert_liked_user(username, data_received['postid'])

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
        else:
            if post:
                pass

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
    return home2()

@user_bp.route('/news_dislike', methods=['GET', 'POST'])
def news_dislike():
    if request.method == "POST":
        username = session['username']

        data_received = json.loads(request.data)
        post = interactionHandler.retrieve_newsid(data_received['postid'])
        like_count = interactionHandler.retrieve_newslikecount(data_received['postid'])
        like_count = like_count[0]

        relation = interactionHandler.retrieve_liked_user(username, data_received['postid'])
        if relation is not None:
            if post:
                like_count = like_count - 1
                interactionHandler.news_update((like_count, data_received['postid']))
                interactionHandler.remove_liked_user(username, data_received['postid'])

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
        else:
            if post:
                pass

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
    return home2()

# Sports interaction
@user_bp.route('/sports_like', methods=['GET', 'POST'])
def sports_like():
    if request.method == "POST":
        username = session['username']

        data_received = json.loads(request.data)
        post = interactionHandler.retrieve_sportsid(data_received['postid'])
        like_count = interactionHandler.retrieve_sportslikecount(data_received['postid'])
        like_count = like_count[0]

        relation = interactionHandler.retrieve_liked_user(username, data_received['postid'])
        if relation is None:
            if post:
                like_count = like_count + 1
                interactionHandler.sports_update((like_count, data_received['postid']))
                interactionHandler.insert_liked_user(username, data_received['postid'])

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
        else:
            if post:
                pass

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
    return home2()

@user_bp.route('/sports_dislike', methods=['GET', 'POST'])
def sports_dislike():
    if request.method == "POST":
        username = session['username']

        data_received = json.loads(request.data)
        post = interactionHandler.retrieve_sportsid(data_received['postid'])
        like_count = interactionHandler.retrieve_sportslikecount(data_received['postid'])
        like_count = like_count[0]

        relation = interactionHandler.retrieve_liked_user(username, data_received['postid'])
        if relation is not None:
            if post:
                like_count = like_count - 1
                interactionHandler.sports_update((like_count, data_received['postid']))
                interactionHandler.remove_liked_user(username, data_received['postid'])

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
        else:
            if post:
                pass

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
    return home2()

# Music interaction
@user_bp.route('/music_like', methods=['GET', 'POST'])
def music_like():
    if request.method == "POST":
        username = session['username']

        data_received = json.loads(request.data)
        post = interactionHandler.retrieve_musicid(data_received['postid'])
        like_count = interactionHandler.retrieve_musiclikecount(data_received['postid'])
        like_count = like_count[0]

        relation = interactionHandler.retrieve_liked_user(username, data_received['postid'])
        if relation is None:
            if post:
                like_count = like_count + 1
                interactionHandler.music_update((like_count, data_received['postid']))
                interactionHandler.insert_liked_user(username, data_received['postid'])

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
        else:
            if post:
                pass

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
    return home2()

@user_bp.route('/music_dislike', methods=['GET', 'POST'])
def music_dislike():
    if request.method == "POST":
        username = session['username']

        data_received = json.loads(request.data)
        post = interactionHandler.retrieve_musicid(data_received['postid'])
        like_count = interactionHandler.retrieve_musiclikecount(data_received['postid'])
        like_count = like_count[0]

        relation = interactionHandler.retrieve_liked_user(username, data_received['postid'])
        if relation is not None:
            if post:
                like_count = like_count - 1
                interactionHandler.music_update((like_count, data_received['postid']))
                interactionHandler.remove_liked_user(username, data_received['postid'])

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
        else:
            if post:
                pass

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
    return home2()

# Lifestyle interaction
@user_bp.route('/lifestyle_like', methods=['GET', 'POST'])
def lifestyle_like():
    if request.method == "POST":
        username = session['username']

        data_received = json.loads(request.data)
        post = interactionHandler.retrieve_lifestyleid(data_received['postid'])
        like_count = interactionHandler.retrieve_lifestylelikecount(data_received['postid'])
        like_count = like_count[0]

        relation = interactionHandler.retrieve_liked_user(username, data_received['postid'])
        if relation is None:
            if post:
                like_count = like_count + 1
                interactionHandler.lifestyle_update((like_count, data_received['postid']))
                interactionHandler.insert_liked_user(username, data_received['postid'])

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
        else:
            if post:
                pass

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
    return home2()

@user_bp.route('/lifestyle_dislike', methods=['GET', 'POST'])
def lifestyle_dislike():
    if request.method == "POST":
        username = session['username']

        data_received = json.loads(request.data)
        post = interactionHandler.retrieve_lifestyleid(data_received['postid'])
        like_count = interactionHandler.retrieve_lifestylelikecount(data_received['postid'])
        like_count = like_count[0]

        relation = interactionHandler.retrieve_liked_user(username, data_received['postid'])
        if relation is not None:
            if post:
                like_count = like_count - 1
                interactionHandler.lifestyle_update((like_count, data_received['postid']))
                interactionHandler.remove_liked_user(username, data_received['postid'])

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
        else:
            if post:
                pass

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
    return home2()


@user_bp.route('/save_post', methods=['GET', 'POST'])
def save_post():
    if request.method == "POST":
        username = session['username']

        data_received = json.loads(request.data)
        post = interactionHandler.retrieve_postid(data_received['postid'])

        post_info = interactionHandler.get_post_info(data_received['postid'])
        relation = interactionHandler.check_post(username, post_info[0])
        if relation is None:
            if post:
                interactionHandler.save_post(username, data_received['postid'],
                                             post_info[0], post_info[1], post_info[2], post_info[3])

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
        else:
            if post:
                pass

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
    return home2()


@user_bp.route('/unsave', methods=['GET', 'POST'])
def unsave_post():
    if request.method == "POST":
        username = session['username']

        data_received = json.loads(request.data)
        post = interactionHandler.retrieve_postid(data_received['postid'])

        post_info = interactionHandler.get_post_info(data_received['postid'])
        relation = interactionHandler.check_post(username, post_info[0])
        if relation is not None:
            if post:
                interactionHandler.unsave_post(username, post_info[0])

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
        else:
            if post:
                pass

                return json.dumps({'status': 'success'})
            return json.dumps({'status': 'no post found'})
    return home2()


@user_bp.route('/add_comment', methods=['GET', 'POST'])
def post_comment():
    if request.method == "POST":
        username = session['username'].lower()
        body = request.form['body']
        print(body)
        time = datetime.now()
        # time = str(time)
        # print(body)

        # data_received = json.loads(request.data)
        # post = interactionHandler.retrieve_postid(data_received['postid'])

        # post_info = interactionHandler.get_post_info(data_received['postid'])
        # relation = interactionHandler.check_post(username, post_info[0])
        print(username)
        print(1)
        interactionHandler.insert_comment(1, username, body, time)
        # print(relation)
        # if relation:
        #     print(relation)
        # comments = interactionHandler.show_comment()
        # print(comments)
        # comments_first = []
        # for comment in comments:
        #     comments_first.append(comment[0])
        # print(comments_first)
        return json.dumps({'status': 'success'})
        # print(comments)
        # return render_template('news.html', comments=comments_first)
        # else:
        #     return json.dumps({'status': 'no post found'})
    else:
        return home2()

