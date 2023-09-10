import psycopg2
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

class Db:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.conn = psycopg2.connect(database = "DB", 
                        user = "DB_USER", 
                        host= 'DB_HOST',
                        password = "DB_PASWORD",
                        port = "DB_PORT")
        return cls._instance

    @staticmethod
    def query(sql: str, arguments: tuple | None = None):
        cur = Db.conn.cursor()
        cur.execute(sql, arguments) 
        return cur