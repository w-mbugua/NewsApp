import unittest
from models import source

Source = source.Source

class NewsTest(unittest.TestCase):
    """
    test class to test the sources class
    """
    def setUp(self):
        self.new_source = Source('aa-news', 'AA', 'Most reliable news source')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

if __name__ == '__main__':
    unittest.main()