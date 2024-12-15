import sqlite3

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id

        # Insert into the articles table
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)
        ''', (title, content, author_id, magazine_id))
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    
    def author(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id=?", (self._author_id,))
        author = cursor.fetchone()
        conn.close()
        return author

    def magazine(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id=?", (self._magazine_id,))
        magazine = cursor.fetchone()
        conn.close()
        return magazine
