import sqlite3

class Database():

    def __init__(self, banco):
        self.banco = banco
        self.conn = sqlite3.connect(self.banco + '.db')
        self.cur = self.conn.cursor()
        self.tabela = self.cur.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)")

    def add(self, note):
        self.cur.execute("INSERT INTO note (title, content) VALUES (?, ?)", (note.title, note.content))
        self.conn.commit()

class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content