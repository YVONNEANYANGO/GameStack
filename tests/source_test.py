import unittest
from .models import source
Source = source.Source


class SourceTest(unittest.TestCase):
    ''' test class to test behavior of Source class '''

    def setUp(self):
        ''' set up method that will run before every test '''
        self.new_source = Source("Kay", "Kay news", "Daily News plug", "https://www.kay.com", "news", "english", "ke")

    def test_instance(self):
        ''' checks if object self.new_source is an instance of Source class '''
        self.assertTrue(isinstance(self.new_source,Source))

        	
            
class SourceNewsTest(unittest.TestCase):
    ''' test class to test behavior of Source class '''

    def setUp(self):
        ''' set up method that will run before every test '''

        self.new_source_news = Source_News("Kay news", "bananas are awesome", "Minions love bananas", "www.kay.com/articles", "www.kay.com/photos/sdfkjd", "2018-10-01T20:47:36Z")
    
    def test_instance(self):
        ''' checks if object self.new_source is an instance of Source class '''
       
        self.assertTrue(isinstance(self.new_source_news,Source_News))
        
