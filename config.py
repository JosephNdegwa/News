import os
class Config:
    '''
    General configuration parent class
    '''
    HEADLINE_API_BASE_URL = 'https://newsapi.org/v2/everything?q=news&from=2022-01-29&to=2022-01-28&sortBy={}&apiKey={}'
    #SOURCE_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category=politics&apiKey=2ea95dbe70bd417e9d0238241ea17c60'
    HEADLINE_API_KEY = os.environ.get('HEADLINE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


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


config_options = {
'development':DevConfig,
'production':ProdConfig
}