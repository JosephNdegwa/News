from importlib.resources import contents
from urllib.request import urlopen


class Headline:
    '''
    Headline class to define Headline Objects
    '''

    def __init__(self,name,author,tittle,description,image,publishedAt):
        self.name = name
        self.author = author
        self.title = tittle
        self.description = description
        self.image = 'urlToImage'
        self.publishedAt = publishedAt