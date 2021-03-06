import urllib.request,json
from .models import  Headline, Headline_source


# Getting api key
api_key = None

# Getting the headline base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['HEADLINE_API_KEY']
    base_url = app.config['HEADLINE_API_BASE_URL']



def get_headlines(category):
    '''
    Function that gets the json response to our url request
    '''
    get_headlines_url = base_url.format("articles",api_key)
    print(get_headlines_url)

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

        name = headline_item.get('name')
        title = headline_item.get('title')
        content = headline_item.get('content')
        urlToImage = headline_item.get('urlToImage')
        publishedAt = headline_item.get('publishedAt')
        url = headline_item.get('url')
        

        if urlToImage:
            headline_object = Headline(name,title,content,urlToImage,publishedAt,url)
            headline_articles.append(headline_object)


    return headline_articles


def get_headline(newsroom):
    get_headline_details_url = base_url.format("politics",api_key)
    print(get_headline_details_url)

    with urllib.request.urlopen(get_headline_details_url) as url:
        headline_deatails_data = url.read()
        headline_deatails_response = json.loads(headline_deatails_data)

        headline_object = None

        if headline_deatails_response ['articles']: 
            name = headline_deatails_response.get('name')
            
            

            headline_object = Headline_source(name)

    return headline_object

    