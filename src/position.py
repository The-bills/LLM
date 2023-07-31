from cv import Cv
from llm.llm import Llm

class Position:
    name: str
    description: str

    def __init__(self):
        self.name = ""
        self.description = ""
        self.characteristics = ""
    
    def set_name(self, name: str):
        self.name = name
        return self

    def set_description(self, description: str):
        self.description = description
        return self
    
    def gen_characteristics(self):
        self.characteristics = Llm.describe_position(self.name, self.description)
        return self
        
    
    def rate_cv(self, cv: Cv):
        return Llm.rate_cv(self.name, self.description, self.characteristics, cv.content)