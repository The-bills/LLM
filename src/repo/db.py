import psycopg2

class Db:
    conn = psycopg2.connect(database = "llm", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)
    @staticmethod
    def query(sql: str, arguments: tuple | None = None):
        cur = Db.conn.cursor()
        cur.execute(sql, arguments) 
        return cur
    