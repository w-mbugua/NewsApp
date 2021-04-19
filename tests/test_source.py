import unittest
from app.model import Source


class NewsTest(unittest.TestCase):
    """
    test class to test the sources class
    """
    def setUp(self):
        self.new_source = Source('aa-news', 'AA', 'Most reliable news source')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

