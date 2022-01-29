class Headline:
    '''
    Headline class to define Headline Objects
    '''

    def __init__(self,id,name,author,tittle,description,image,publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = tittle
        self.description = description
        self.image = 'urlToImage' + image
        self.publishedAt = publishedAt