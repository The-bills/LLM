import psycopg2
import psycopg2.extras
psycopg2.extras.register_uuid()

class Db:
    conn = psycopg2.connect(database = "llm", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)
    conn.autocommit = True
    @staticmethod
    def query(sql: str, arguments: tuple | None = None):
        cur = Db.conn.cursor()
        cur.execute(sql, arguments) 
        return cur
    