import sqlite3

class Author:
    def __init__(self, id, name):
        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        self._id = id
        self._name = name
        
        # Insert into the authors table if not already present
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
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

    # Method to fetch all articles by this author
    def articles(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id=?", (self._id,))
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    # Method to fetch all magazines by this author
    def magazines(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT magazines.* FROM magazines JOIN articles ON magazines.id = articles.magazine_id WHERE articles.author_id=?", (self._id,))
        rows = cursor.fetchall()
        conn.close()
        return rows
