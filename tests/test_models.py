import unittest
from models.author import Author
from models.magazine import Magazine
from models.article import Article
from database.setup import create_tables

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #create db
        create_tables()

    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.author(), (1, "John Doe"))
        self.assertEqual(article.magazine(), (1, "Tech Weekly", "Technology"))

if __name__ == '__main__':
    unittest.main()
