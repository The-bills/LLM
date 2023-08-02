import psycopg2

class Db:
    conn = psycopg2.connect(database = "llm", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)