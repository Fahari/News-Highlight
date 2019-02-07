from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source
from ..models import Source

#Views
@main.route('/')
def source():

    '''
    View root page function that returns the source page and its data
    '''

    general_news = get_source('general')
    print(general_news)

    technology_news = get_source('technology')

    sport_news = get_source('sports')

    business_news = get_source('business')

    science_news = get_source('science')

    entertainment_news = get_source('entertainment')

    health_news = get_source('health')

    title = 'Home -Let us get to the briefs'
    return render_template('source.html', title = title,general=general_news,technology=technology_news,sports=sport_news,business=business_news,science=science_news,entertainment_news=entertainment,health_news=health)
