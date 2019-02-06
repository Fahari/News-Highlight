
from flask import render_template
from app import app
from .request import get_source

# Views
@app.route('/')
def source():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to News Highlight'
    general_news = get_source('general')
    business_news = get_source('business')
    entertainment_news = get_source('entertainment')
    health_news = get_source('health')
    science_news = get_source('science')
    sports_news = get_source('sports')
    technology_news = get_source('technology')
    # print(general_news)
    return render_template('source.html', title = title,general = general_news,business = business_news,entertainment = entertainment_news,health = health_news,science = science_news,sports = sports_news,technology = technology_news)
