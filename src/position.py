from cv import Cv
from llm.llm import Llm
from db import Db

class Position:
    name: str
    description: str
    qualifications: [str]

    def hydrate(self, id, name, description, qualifications):
        self.id = id
        self.name = name
        self.description = description
        self.qualifications = qualifications
        return self

    def __init__(self):
        self.name = ""
        self.description = ""
        
    
    def set_name(self, name: str):
        self.name = name
        return self

    def set_description(self, description: str):
        self.description = description
        return self
    
    def gen_qualifications (self):
        self.qualifications = Llm.describe_position(self.name, self.description)
        return self
        
    
    def rate_cv(self, cv: Cv):
        return Llm.rate_cv(self.name, self.description, self.qualifications , cv.content)

    def get(id):
        cur = Db.conn.cursor()
        cur.execute("SELECT * FROM positions WHERE id = %s;", (id,))
        data = cur.fetchone()
        return Position().hydrate(*data)