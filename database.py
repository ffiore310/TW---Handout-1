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

    def get_all(self):
        l = []
        cursor = self.cur.execute("SELECT id, title, content FROM note")
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            l.append(Note(id, title, content))
        return l
    
    def update(self,entry):
        self.cur.execute("UPDATE note SET title = ?, content = ? WHERE id = ?", (entry.title, entry.content, entry.id))
        self.conn.commit()

    def delete(self, note_id):
        self.cur.execute("DELETE FROM note WHERE id = ?", (note_id,))
        self.conn.commit()

class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content