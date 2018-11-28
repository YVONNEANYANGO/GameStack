from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source_news
from ..models import Source,Source_News

 #views
@main.route('/')
def index():
    ''' returns index page and its data '''

    news = get_source_news()
    title = f"{id} | All Articles"

    return render_template('index.html', title = title, news = news)

