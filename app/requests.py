from distutils.command.config import config
from app import app
import urllib.request,json
from .models import  headline

Headline = headline.Headline

# Getting api key
api_key = app.config['HEADLINE_API_KEY']

# Getting the headline base url
base_url = app.config["HEADLINE_API_BASE_URL"]



def get_headlines(category):
    '''
    Function that gets the json response to our url request
    '''
    get_headlines_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headline_articles = None

        if get_headlines_response['articles']:
            headline_articles_list = get_headlines_response['articles']
            headline_articles = process_articles(headline_articles_list)


    return headline_articles



def process_articles(headline_list):
    '''
    Function that processes the headline articles and transform them to a list of objects
    
    Args:
        headline_list: A list of dictionaries that contain movie details

    Returns:
        headline_articles: A list of headline objects
    '''
    headline_articles = []
    for headline_item in headline_list:
        id = headline_item.get('id')
        name = headline_item.get('name')
        author = headline_item.get('author')
        title = headline_item.get('title')
        description = headline_item.get('description')
        image = headline_item.get('urlToImage')
        publishedAt = headline_item.get('publishedAt')

        if image:
            headline_object = Headline(id,name,author,title,description,image,publishedAt)
            headline_articles.append(headline_object)


    return headline_articles

    