import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
psycopg2.extras.register_uuid()

class Db:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.conn = psycopg2.connect(database = os.getenv("DB"), 
                        user = os.getenv("DB_USER"), 
                        host= os.getenv('DB_HOST'),
                        password = os.getenv("DB_PASWORD"),
                        port = os.getenv("DB_PORT"))
            cls._instance.conn.autocommit = True
        return cls._instance

    @staticmethod
    def query(sql: str, arguments: tuple | None = None):
        cur = Db._instance.conn.cursor()
        cur.execute(sql, arguments) 
        return cur
