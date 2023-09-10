from repo.db import Db
from models.cv import Cv

class CvRepo:
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
    