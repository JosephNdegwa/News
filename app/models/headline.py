from importlib.resources import contents
from urllib.request import urlopen


class Headline:
    '''
    Headline class to define Headline Objects
    '''

    def __init__(self,name,author,tittle,content,urlToImage,publishedAt,url):
        self.name = name
        self.author = author
        self.title = tittle
        self.content = content
        self.urlToimage = urlToImage
        self.publishedAt = publishedAt
        self.url = url
        