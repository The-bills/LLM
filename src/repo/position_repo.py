from repo.db import Db
from models.position import Position

class PositionRepo:
    @staticmethod
    def get_all():
        data = Db.query("SELECT * FROM positions;").fetchall()
        vec = [Position(*element) for element in data]
        return vec


    @staticmethod
    def get_one(id):
        data = Db.query(f"SELECT * FROM positions WHERE id = '{id}';").fetchone()
        return data and Position(*data) or None

    @staticmethod
    def insert():
        data = Db.query("SELECT * FROM positions ;").fetchone()
        return data and Position(*data) or None

    @staticmethod
    def delete(id):
        data = Db.query(f"DELETE FROM positions WHERE id = '{id}';").fetchone()
        return data and Position(*data) or None
    