from db import Db

class Position:
    id: str
    name: str 
    description: str

    @staticmethod
    def hydrate(id, name, description):
        position = Position()
        position.id = id
        position.name = name
        position.description = description
        return position

    @staticmethod
    def get_all():
        data = Db.query("SELECT * FROM positions;").fetchall()
        import sys
        vec = []
        for element in data:
            vec.append(Position.hydrate(*element))
        return vec


    @staticmethod
    def get_one(id):
        data = Db.query("SELECT * FROM positions WHERE id = %s;", (id,)).fetchone()
        return data and Position.hydrate(*data) or None

    @staticmethod
    def insert():
        data = Db.query("SELECT * FROM positions ;").fetchone()
        return data and Position.hydrate(*data) or None

    @staticmethod
    def delete(id):
        data = Db.query("DELETE FROM positions WHERE id = %s;", (id,)).fetchone()
        return data and Position.hydrate(*data) or None