from db import Db

class Cv:
    id: str
    name: str
    content: str
    filelink: str

    def __init__(self, id, name, filelink, content):
        self.id = id
        self.name = name
        self.filelink = filelink
        self.content = content
        return self
    

    @staticmethod
    def get_all():
        data = Db.query("SELECT * FROM cv;").fetchall()
        vec = [Cv(*element) for element in data]
        return vec


    @staticmethod
    def get_one(id):
        data = Db.query(f"SELECT * FROM cv WHERE id = '{id}'").fetchone()
        return data and Cv(*data) or None

    @staticmethod
    def insert():
        data = Db.query("SELECT * FROM cv;").fetchone()
        return data and Cv(*data) or None

    @staticmethod
    def delete(id):
        data = Db.query(f"DELETE FROM cv WHERE id = '{id}';").fetchone()
        return data and Cv(*data) or None
    