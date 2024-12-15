from models.article import Article
from models.author import Author
from models.magazine import Magazine
from database.setup import create_tables

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Create author and magazine instances
    author = Author(None, author_name) 
    magazine = Magazine(None, magazine_name, magazine_category)

    # Create article instance
    article = Article(None, article_title, article_content, author.id, magazine.id)

    print(f"Article '{article.title}' by {author.name} in {magazine.name}")

if __name__ == "__main__":
    main()
