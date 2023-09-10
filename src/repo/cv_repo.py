from repo.db import Db
from models.cv import Cv
from uuid import uuid4

class CvRepo:
    @staticmethod
    def get_all():
        data = Db().query("SELECT * FROM cv;").fetchall()
        return [Cv(*element) for element in data]


    @staticmethod
    def get_one(id):
        data = Db().query(f"SELECT * FROM cv WHERE id = '{id}'").fetchone()
        return data and Cv(*data) or None

    @staticmethod
    def insert(name, filelink, category, doc_id = None, id = None):
        query = """
            INSERT INTO cv (id, name, filelink, category, doc_id)
            VALUES (%s, %s, %s, %s, %s) RETURNING id;
        """
        id = Db().query(query, (id or uuid4(), name, filelink, category, doc_id)).fetchone()[0]
        return CvRepo.get_one(id)

    @staticmethod
    def delete(id):
        data = Db().query(f"DELETE FROM cv WHERE id = '{id}';").fetchone()
        return data and Cv(*data) or None
    