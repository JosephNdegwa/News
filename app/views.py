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
    business_headlines = get_headlines('business')
    technology_headlines = get_headlines('technology')
    sports_headlines = get_headlines('sports')
    title = 'Welcome to Your News Page'
    return render_template('index.html', title = title, popularity = popularity_headlines, business = business_headlines, technology = technology_headlines, sports = sports_headlines)


@app.route('/headline/<int:headline_id>')
def headline(headline_id):

    '''
    View headline page function that returns the headline details page and its data
    '''
    headline = get_headline(id)
    title = f'{headline.title}'


    return render_template('headline.html', title = title, headline = headline)