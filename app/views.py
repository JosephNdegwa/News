from flask import render_template
from app import app
from .requests import get_articles



# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popularity_article = get_articles('popularity')
    title = 'Welcome to Your News Page'
    return render_template('index.html', title = title, popularity = popularity_article)


@app.route('/article/<int:article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('article.html',id = article_id)