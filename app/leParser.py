import requests
import re
from flask import Blueprint, render_template, session, request, json
import sqlite3 as sql
from bs4 import BeautifulSoup
from datetime import datetime

import app.interaction as interactionHandler
from app.home import home2
from config import posts_db_path

from app.userProfile import post_comment

parser_bp = Blueprint('parser_bp', __name__, template_folder='templates', static_folder='static',
                      static_url_path='/static/parser_bp')

headers = {
    'User-agent': 'Mozilla/5.0'
}


con = sql.connect(posts_db_path)


# interactionHandler.truncate()

def parse(link):
    web_url = link
    web_request = requests.get(web_url, headers=headers)
    soup = BeautifulSoup(web_request.text, 'html.parser')
    return soup


def newspaper_info(post_link):
    news_paper = []
    for i in post_link:
        x = re.findall(r'www.(.*?).co', i)
        str_x = ''.join(word for word in x)
        news_paper.append(str_x.upper())

    for i in post_link:
        xx = re.findall(r'\b(\w*sky\w*)\b', i)
        str_xx = ''.join(word for word in xx)
        news_paper.append(str_xx.upper())
        # news_paper.remove('')

    news_paper_link = []
    for i in news_paper:
        if i.lower() == 'express':
            link = 'https://www.express.co.uk'
        elif i.lower() == 'sky':
            link = 'https://news.sky.com/world'
        else:
            link = "https://www." + i.lower() + ".com"
        news_paper_link.append(link)

    return news_paper, news_paper_link


def sportpaper_info(post_link):
    news_paper = []
    for i in post_link:
        x = re.findall(r'www.(.*?).co', i)
        str_x = ''.join(word for word in x)
        news_paper.append(str_x.upper())

    for i in news_paper:
        if i == 'SKYSPORTSSKYSPORTS':
            news_paper.remove(i)
            news_paper.append('SKYSPORTS')

    news_paper_link = []
    for i in news_paper:
        if i.lower() == 'express':
            link = 'https://www.express.co.uk'
        elif i.lower() == 'sky':
            link = 'https://news.sky.com/world'
        else:
            link = "https://www." + i.lower() + ".com"
        news_paper_link.append(link)

    return news_paper, news_paper_link


def duplicate_limiter(post_item):
    post_item = list(dict.fromkeys(post_item))
    post_item = post_item[:10]

    return post_item


def news_save_to_db(post_title, post_link, post_image, post_summary, like_count):
    for i in range(0, len(post_title)):
        title = post_title[i]
        image = post_image[i]
        link = post_link[i]
        summary = post_summary[i]
        interactionHandler.news_post_insert(title, image, link, summary, like_count)


def sport_save_to_db(post_title, post_link, post_image, post_summary, like_count):
    for i in range(0, len(post_title)):
        title = post_title[i]
        image = post_image[i]
        link = post_link[i]
        summary = post_summary[i]
        interactionHandler.sport_post_insert(title, image, link, summary, like_count)


def music_save_to_db(post_title, post_link, post_image, post_summary, like_count):
    for i in range(0, len(post_title)):
        title = post_title[i]
        image = post_image[i]
        link = post_link[i]
        summary = post_summary[i]
        interactionHandler.music_post_insert(title, image, link, summary, like_count)


def lifestyle_save_to_db(post_title, post_link, post_image, post_summary, like_count):
    for i in range(0, len(post_title)):
        title = post_title[i]
        image = post_image[i]
        link = post_link[i]
        summary = post_summary[i]
        interactionHandler.lifestyle_post_insert(title, image, link, summary, like_count)


def save_to_db(post_title, post_link, post_image, post_summary, like_count):
    for i in range(0, len(post_title)):
        title = post_title[i]
        image = post_image[i]
        link = post_link[i]
        summary = post_summary[i]
        interactionHandler.all_posts(title, image, link, summary, like_count)

#######################################


def bbc_news_parsing():
    soup = parse("https://www.bbc.com/news")

    post_title = []
    post_image = []
    post_link = []
    post_summary = []

    for i in soup.findAll("h3", class_="gs-c-promo-heading__title"):
        post_title.append(i.text)
    post_title = duplicate_limiter(post_title)

    for i in soup.findAll("a", class_="gs-c-promo-heading"):
        post_link.append("https://www.bbc.com" + i.get('href'))
    post_link = duplicate_limiter(post_link)

    all_urls = []
    for i in range(0, len(post_link)):
        soup_post = parse(post_link[i])
        # print(post_link[i])
        post_images = soup_post.find_all("img")
        urls = [img['src'] for img in post_images]
        all_urls.append(urls)

    for i in all_urls:
        for j in i:
            if "a1.api.bbc.co.uk" in j:
                i.remove(j)

    for i in all_urls:
        post_image.append(i[0])

    for i in soup.findAll("p", class_="gs-c-promo-summary"):
        post_summary.append(i.text)
    post_summary = duplicate_limiter(post_summary)

    news_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    return post_title, post_link, post_image, post_summary


def rt_parsing():
    soup = parse('https://www.rt.com/news')

    post_title = []
    post_image = []
    post_link = []
    post_summary = []

    for i in soup.findAll("a", class_="link"):
        post_title.append(i.text.strip())
    post_title = duplicate_limiter(post_title)
    post_title = post_title[1:11]

    for i in soup.findAll("a", class_="link"):
        post_link.append("https://www.rt.com" + i.get('href').strip())
    post_link = duplicate_limiter(post_link)

    for i in soup.findAll("img", class_="media__item"):
        post_image.append(i.get('src'))
    post_image = duplicate_limiter(post_image)
    post_image = post_image[1:11]

    for i in soup.findAll("div", class_="card__summary"):
        post_summary.append(i.text.strip())
    post_summary = duplicate_limiter(post_summary)

    news_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    return post_title, post_link, post_image, post_summary


def reuters_parsing():
    soup = parse('https://www.reuters.com/news/world')

    post_title = []
    post_image = []
    post_link = []
    post_summary = []

    for i in soup.findAll("div", class_="story-content"):
        post_title.append(i.a.text.strip())
    post_title = duplicate_limiter(post_title)

    for i in soup.findAll("div", class_="story-content"):
        post_link.append("https://www.reuters.com" + i.a.get('href'))
    post_link = duplicate_limiter(post_link)

    for i in soup.findAll("div", class_="story-photo"):
        post_image.append(i.a.img.get('org-src'))

    for i in post_image:
        if i is None:
            post_image.remove(i)

    while len(post_title) > len(post_image):
        post_image.append("")

    post_image = duplicate_limiter(post_image)

    for i in soup.findAll("div", class_="story-content"):
        post_summary.append(i.p.text)

    news_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    # return post_title
# print(len(reuters_parsing()))
    return post_title, post_link, post_image, post_summary


def express_parsing():
    soup = parse('https://www.express.co.uk/news/world')

    post_title = []
    post_image = []
    post_link = []
    post_summary = []

    for i in soup.findAll("li", class_="last"):
        if i.h4 is not None:
            post_title.append(i.h4.text)
    # post_title = duplicate_limiter(post_title)
    post_title = post_title[:11]

    for i in soup.findAll("li", class_="last"):
        if i.a is not None:
            post_link.append("https://www.express.co.uk" + i.a.get('href'))
    # post_link = duplicate_limiter(post_link)
    post_link = post_link[1:12]

    for i in range(0, len(post_link)):
        soup_link = parse(post_link[i])
        # print(post_link[i])
        post_image1 = soup_link.find("img", class_="lazy").get('data-src')
        post_image.append(post_image1)

    for i in post_link:
        post_summary.append('')

    news_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    return post_title, post_link, post_image, post_summary


def skynews_parsing():
    soup = parse('https://news.sky.com/world')

    post_title = []
    post_link = []
    post_image = []
    post_summary = []

    for i in soup.findAll("a", class_="sdc-site-tile__headline-link"):
        post_title.append(i.text.strip())
    post_title = duplicate_limiter(post_title)

    for i in soup.findAll("img", class_="sdc-site-tile__image"):
        post_image.append(i.get('src'))
    post_image = duplicate_limiter(post_image)

    for i in soup.findAll("a", class_="sdc-site-tile__headline-link"):
        post_link.append("https://news.sky.com" + i.get('href'))
    post_link = duplicate_limiter(post_link)

    for i in post_link:
        post_summary.append('')

    news_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    return post_title, post_link, post_image, post_summary


@parser_bp.route('/news')
def all_news():
    username = session['username'].capitalize()
    bbc_title, bbc_link, bbc_image, bbc_summary = bbc_news_parsing()
    rt_title, rt_link, rt_image, rt_summary = rt_parsing()
    # reuters_title, reuters_link, reuters_image, reuters_summary = reuters_parsing()
    express_title, express_link, express_image, express_summary = express_parsing()
    skynews_title, skynews_link, skynews_image, skynews_summary = skynews_parsing()

    joined_titles = bbc_title + rt_title + express_title + skynews_title
    joined_links = bbc_link + rt_link + express_link + skynews_link
    joined_images = bbc_image + rt_image + express_image + skynews_image
    joined_summary = bbc_summary + rt_summary + express_summary + skynews_summary

    # joined_titles = rt_title
    # joined_links = rt_link
    # joined_images = rt_image
    # joined_summary = rt_summary

    news_paper, news_paper_link = newspaper_info(joined_links)

    all_comments = []
    for i in range(40):
        comments = interactionHandler.show_comment(i)
        all_comments.append(comments)
        print(all_comments)

    return render_template("news.html", username=username, len=len(joined_titles), post_title=joined_titles, post_image=joined_images,
                           post_link=joined_links, post_summary=joined_summary, newspaper=news_paper,
                           paper_link=news_paper_link, comments=all_comments)


####################################################################################################


def bbc_sport():
    soup = parse("https://www.bbc.com/sport")

    post_title = []
    post_image = []
    post_link = []
    post_summary = []

    for i in soup.findAll("h3", class_="gs-c-promo-heading__title"):
        post_title.append(i.text)
    post_title = duplicate_limiter(post_title)

    for i in soup.findAll("img", class_="qa-lazyload-image"):
        post_image.append(i.get('data-src').replace('{width}', '240'))
    post_image = duplicate_limiter(post_image)

    for i in soup.findAll("a", class_="gs-c-promo-heading"):
        post_link.append("https://www.bbc.com" + i.get('href'))
    post_link = duplicate_limiter(post_link)

    for i in soup.findAll("p", class_="gs-c-promo-summary"):
        post_summary.append(i.text)
    post_summary = duplicate_limiter(post_summary)

    sport_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    return post_title, post_link, post_image, post_summary


def rt_sport():
    soup = parse('https://www.rt.com/sport/')

    post_title = []
    post_image = []
    post_link = []
    post_summary = []

    for i in soup.findAll("a", class_="link"):
        post_title.append(i.text.strip())
    post_title = duplicate_limiter(post_title)

    for i in soup.findAll("a", class_="link"):
        post_link.append("https://www.rt.com" + i.get('href'))
    post_link = duplicate_limiter(post_link)

    for i in soup.findAll("img", class_="media__item"):
        post_image.append(i.get('data-src'))
    post_image = duplicate_limiter(post_image)

    for i in soup.findAll("div", class_="card__summary"):
        post_summary.append(i.text.strip())
    post_summary = duplicate_limiter(post_summary)

    for i in post_title:
        if i == '':
            post_title.remove(i)

    for i in post_image:
        if i is None:
            post_image.remove(i)

    sport_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    return post_title, post_link, post_image, post_summary


def sky_sport():
    soup = parse('https://www.skysports.com')

    post_title = []
    post_image = []
    post_link = []
    post_summary = []

    for i in soup.findAll("a", class_="sdc-site-tile__headline-link"):
        post_title.append(i.span.text)
    post_title = duplicate_limiter(post_title)

    for i in soup.findAll("a", class_="sdc-site-tile__headline-link"):
        post_link.append("https://www.skysports.com" + i.get('href'))
    post_link = duplicate_limiter(post_link)

    for i in soup.findAll("img", class_="sdc-site-tile__image"):
        post_image.append(i.get('src'))
    post_image = duplicate_limiter(post_image)

    # try:
    #     for i in post_link:
    #         soup_link = parse(i)
    #         for j in soup_link.findAll("div", class_="sdc-article-body"):
    #             post_summary.append(j.p)
    # except Exception as e:
    #     pass

    sport_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    return post_title, post_link, post_image, post_summary


@parser_bp.route('/sport')
def all_sports():
    username = session['username'].capitalize()
    bbc_title, bbc_link, bbc_image, bbc_summary = bbc_sport()
    rt_title, rt_link, rt_image, rt_summary = rt_sport()
    skynews_title, skynews_link, skynews_image, skynews_summary = sky_sport()

    joined_titles = bbc_title + rt_title + skynews_title
    joined_links = bbc_link + rt_link + skynews_link
    joined_images = bbc_image + rt_image + skynews_image
    joined_summary = bbc_summary + rt_summary + skynews_summary

    news_paper, news_paper_link = sportpaper_info(joined_links)

    return render_template("sports.html", username=username, len=len(joined_titles), post_title=joined_titles, post_image=joined_images,
                           post_link=joined_links, post_summary=joined_summary, newspaper=news_paper,
                           paper_link=news_paper_link)


##################################################################################################################


def nme_music():
    soup = parse('https://www.nme.com/news/music')

    post_title = []
    post_image = []
    post_link = []
    post_summary = []

    for i in soup.findAll("h3", class_="entry-title"):
        post_title.append(i.a.text)
    post_title = duplicate_limiter(post_title)

    for i in soup.findAll("h3", class_="entry-title"):
        post_link.append(i.a.get('href'))
    post_link = duplicate_limiter(post_link)

    for i in soup.findAll("span", class_="entry-thumb"):
        post_image.append(i.get('data-img-url'))
    post_image = duplicate_limiter(post_image)

    for i in soup.findAll("div", class_="td-excerpt"):
        post_summary.append(i.text)
    post_summary = duplicate_limiter(post_summary)

    music_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    return post_title, post_link, post_image, post_summary


def spin_music():
    soup = parse('https://www.spin.com/')

    post_title = []
    post_image = []
    post_link = []
    post_summary = []

    for i in soup.findAll("div", class_="preview-holder"):
        post_title.append(i.a.text.strip())
    post_title = duplicate_limiter(post_title)

    for i in soup.findAll("div", class_="preview-holder"):
        post_link.append(i.a.get('href'))
    post_link = duplicate_limiter(post_link)

    for i in soup.findAll("div", class_="img-wrap"):
        post_image.append(i.img.attrs.get('src'))
    post_image = duplicate_limiter(post_image)

    for i in soup.findAll("div", class_="preview"):
        post_summary.append(i.text.strip())
    post_summary = duplicate_limiter(post_summary)

    music_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    return post_title, post_link, post_image, post_summary


def stereogum_music():
    soup = parse('https://www.stereogum.com/')

    post_title = []
    post_image = []
    post_link = []
    post_summary = []

    for i in soup.findAll("div", class_="preview-holder"):
        post_title.append(i.a.text.strip())
    post_title = duplicate_limiter(post_title)

    for i in soup.findAll("div", class_="preview-holder"):
        post_link.append(i.a.get('href'))
    post_link = duplicate_limiter(post_link)

    for i in soup.findAll("div", class_="img-wrap"):
        post_image.append(i.img.get('src'))
    post_image = duplicate_limiter(post_image)

    for i in soup.findAll("div", class_="preview"):
        post_summary.append(i.text.strip())
    post_summary = duplicate_limiter(post_summary)

    music_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    return post_title, post_link, post_image, post_summary


#     return post_link
# print(stereogum_music())

@parser_bp.route('/music')
def all_music():
    username = session['username'].capitalize()
    nme_title, nme_link, nme_image, nme_summary = nme_music()
    spin_title, spin_link, spin_image, spin_summary = spin_music()
    stereogum_title, stereogum_link, stereogum_image, stereogum_summary = stereogum_music()

    joined_titles = nme_title + spin_title + stereogum_title
    joined_links = nme_link + spin_link + stereogum_link
    joined_images = nme_image + spin_image + stereogum_image
    joined_summary = nme_summary + spin_summary + stereogum_summary

    news_paper, news_paper_link = sportpaper_info(joined_links)

    return render_template("sports.html", username=username, len=len(joined_titles), post_title=joined_titles, post_image=joined_images,
                           post_link=joined_links, post_summary=joined_summary, newspaper=news_paper,
                           paper_link=news_paper_link)


##################################################################################################################


def cupOfJo():
    soup = parse('https://cupofjo.com/')

    post_title = []
    post_image = []
    post_link = []
    post_summary = []

    for i in soup.findAll("header", class_="entry-header"):
        post_title.append(i.h2.a.text)
    post_title = duplicate_limiter(post_title)

    for i in soup.findAll("header", class_="entry-header"):
        post_link.append(i.h2.a.get('href'))
    post_link = duplicate_limiter(post_link)

    for i in soup.findAll("img", class_="alignnone"):
        post_image.append(i.get('data-jpibfi-src'))
    post_image = duplicate_limiter(post_image)

    # for i in soup.find("div", {"class": "entry-content"}):
    #     post_summary.append(i.p.text)
    # post_summary = duplicate_limiter(post_summary)

    for i in post_title:
        post_summary.append('')

    lifestyle_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    return post_title, post_link, post_image, post_summary


def earthlingorgeous():
    soup = parse('https://www.earthlingorgeous.com/')

    post_title = []
    post_image = []
    post_link = []
    post_summary = []

    for i in soup.findAll("h2", class_="entry-title"):
        post_title.append(i.a.text)
    post_title = duplicate_limiter(post_title)

    for i in soup.findAll("h2", class_="entry-title"):
        post_link.append(i.a.get('href'))
    post_link = duplicate_limiter(post_link)

    for i in soup.findAll("img", class_="attachment-saaya-full-width"):
        post_image.append(i.get('src'))
    post_image = duplicate_limiter(post_image)

    post_summary1 = []
    for i in soup.findAll("div", class_="entry-content"):
        post_summary.append(i.p.text)

    for i in post_summary:
        i = i.replace("\xa0", "")
        post_summary1.append(i)
    post_summary1 = duplicate_limiter(post_summary1)

    lifestyle_save_to_db(post_title, post_link, post_image, post_summary, 0)
    save_to_db(post_title, post_link, post_image, post_summary, 0)

    return post_title, post_link, post_image, post_summary1


@parser_bp.route('/lifestyle')
def all_lifestyle():
    username = session['username'].capitalize()
    cup_title, cup_link, cup_image, cup_summary = cupOfJo()
    earth_title, earth_link, earth_image, earth_summary = earthlingorgeous()

    joined_titles = cup_title + earth_title
    joined_links = cup_link + earth_link
    joined_images = cup_image + earth_image
    joined_summary = cup_summary + earth_summary

    news_paper, news_paper_link = newspaper_info(joined_links)

    return render_template("news.html", username=username, len=len(joined_titles), post_title=joined_titles, post_image=joined_images,
                           post_link=joined_links, post_summary=joined_summary, newspaper=news_paper,
                           paper_link=news_paper_link)


###################################################################################

# ADDING COMMENTS AND DISPLAYING THEM
# @parser_bp.route('/add_comment', methods=['GET', 'POST'])
# def post_comment():
#     if request.method == "POST":
#         username = session['username'].lower()
#         body = request.form['body']
#         time = datetime.now().strftime("%B %d, %Y %I:%M%p")
#
#         data_received = json.loads(request.data)
#         post = interactionHandler.retrieve_postid(data_received['postid'])
#
#         # post_info = interactionHandler.get_post_info(data_received['postid'])
#         # relation = interactionHandler.check_post(username, post_info[0])
#         print(username)
#         print(data_received['postid'])
#         relation = interactionHandler.insert_comment(body, time, post, username)
#         print(relation)
#         if relation:
#             print(relation)
#             comments = interactionHandler.show_comment(data_received['postid'])
#             print(comments)
#             json.dumps({'status': 'success'})
#             return render_template('news.html', comments=comments)
#         else:
#             return json.dumps({'status': 'no post found'})
#     return home2()
