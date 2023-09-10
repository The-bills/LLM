from repo.db import Db
from models.position import Position
from uuid import uuid4

class PositionRepo:
    @staticmethod
    def get_all():
        data = Db.query("SELECT * FROM positions;").fetchall()
        return [Position(*element) for element in data]


    @staticmethod
    def get_one(id):
        data = Db.query("SELECT * FROM positions WHERE id = %s;", (id, )).fetchone()
        return data and Position(*data) or None

    @staticmethod
    def insert(name, description, id = None):
        query = """
            INSERT INTO positions (id, name, description)
            VALUES (%s, %s, %s) RETURNING id;
        """
        id = Db.query(query, (id or uuid4(), name, description)).fetchone()[0]
        return PositionRepo.get_one(id)

    @staticmethod
    def delete(id):
        data = Db.query("DELETE FROM positions WHERE id = %s;", (id, )).fetchone()
        return data and Position(*data) or None
    