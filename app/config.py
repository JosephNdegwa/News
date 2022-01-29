class Config:
    '''
    General configuration parent class
    '''
    HEADLINE_API_BASE_URL = 'https://newsapi.org/v2/everything?q=news&from=2022-01-28&to=2022-01-28&sortBy={}&apiKey={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True