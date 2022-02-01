from urllib.request import urlopen


class Headline:
    '''
    Headline class to define Headline Objects
    '''

    def __init__(self,name,tittle,content,urlToImage,publishedAt,url):
        self.name = name
        self.title = tittle
        self.content = content
        self.urlToimage = urlToImage
        self.publishedAt = publishedAt
        self.url = url



class Headline_source:
    '''
    Headline_source class to define Headline_source objects
    '''

    def  __init__(self,name):
        self.name =name
        