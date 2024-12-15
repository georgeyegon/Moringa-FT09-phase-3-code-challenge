import sqlite3

class Magazine:
    def __init__(self, id, name, category):
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be between 2 and 16 characters")
        if len(category) == 0:
            raise ValueError("Category must not be empty")
        
        self._id = id
        self._name = name
        self._category = category

        # Insert into the magazines table
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        self._category = value

    def articles(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id=?", (self._id,))
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    def contributors(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT authors.* FROM authors JOIN articles ON authors.id = articles.author_id WHERE articles.magazine_id=?", (self._id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def article_titles(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id=?", (self._id,))
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]
    
    def contributing_authors(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT authors.name FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.name
            HAVING COUNT(articles.id) > 2
        """, (self._id,))
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows] if rows else None
