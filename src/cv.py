from db import Db

class Cv:
    id: str
    name: str
    content: str
    filelink: str

    @staticmethod
    def hydrate(id, name, filelink, content):
        cv = Cv()
        cv.id = id
        cv.name = name
        cv.filelink = filelink
        cv.content = content
        return cv

    @staticmethod
    def get_all():
        data = Db.query("SELECT * FROM cv;").fetchall()
        vec = []
        for element in data:
            vec.append(Cv().hydrate(*element))
        return vec


    @staticmethod
    def get_one(id):
        data = Db.query("SELECT * FROM cv WHERE id = %s;", (id,)).fetchone()
        return data and Cv().hydrate(*data) or None

    @staticmethod
    def insert():
        data = Db.query("SELECT * FROM cv ;").fetchone()
        return data and Cv().hydrate(*data) or None

    @staticmethod
    def delete(id):
        data = Db.query("DELETE FROM cv WHERE id = %s;", (id,)).fetchone()
        return data and Cv().hydrate(*data) or None