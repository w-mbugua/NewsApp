import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    """
    test class to test the news class
    """
    def setUp(self):
        self.hot_news = News('author', 'title', 'description', 'url', 'urlToImage', 'publishedAt')

    def test_instance(self):
        self.assertTrue(isinstance(self.hot_news, News))

if __name__ == '__main__':
    unittest.main()