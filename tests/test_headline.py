import unittest
from app.models import Headline


class HeadineTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Headline class
    '''

    def setup(self):
        '''
        Set up method that will run before every Test
        '''
        self.headline_articles = Headline('UBS posts fall in quarterly profit to $1.35 billion, sets ambitious new targets - CNBC,Myanmars coup leaders tried to crush resistance. But one year on, its stronger than ever - CNN')

        
    def test_instance(self):
        self.assertTrue(isinstance(self.headline_articles, Headline))
