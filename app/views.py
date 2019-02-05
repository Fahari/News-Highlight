
from flask import render_template
from app import app

# Views
@app.route('/')
def source():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('source.html')
