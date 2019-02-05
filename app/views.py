
from flask import render_template
from app import app

# Views
@app.route('/')
def source():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to News Highlight'
    return render_template('source.html', title = title)
