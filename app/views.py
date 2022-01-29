from flask import render_template
from app import app
from .requests import get_headlines



# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popularity_headline = get_headlines('popularity')
    title = 'Welcome to Your News Page'
    return render_template('index.html', title = title, popularity = popularity_headline)


@app.route('/headline/<int:headline_id>')
def headline(headline_id):

    '''
    View headline page function that returns the headline details page and its data
    '''
    return render_template('headline.html',id = headline_id)