from importlib.resources import contents
from os import name
from flask import render_template
from app import app
from .requests import get_headlines,get_headline



# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popularity_headlines = get_headlines('popularity')
   
    title = 'Welcome to Your News Page'
    return render_template('index.html', title = title, popularity = popularity_headlines)


@app.route('/headline/headline_url')
def headline(headline_name):

    '''
    View headline page function that returns the headline details page and its data
    '''
    headline = get_headline(name)
    title = f'{headline.title}'


    return render_template('headline.html', title = title, headline = headline)