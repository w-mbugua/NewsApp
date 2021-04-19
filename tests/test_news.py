import unittest
from app.model import News


class NewsTest(unittest.TestCase):
    """
    test class to test the news class
    """
    def setUp(self):
        self.hot_news = News('author', 'title', 'description', 'url', 'urlToImage', 'publishedAt')

    def test_instance(self):
        self.assertTrue(isinstance(self.hot_news, News))
