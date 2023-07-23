from dics.constants import position_perfect_description_prompt, rate_cv_prompt
from utilis import get_completion_from_prompt

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
        prompt = position_perfect_description_prompt(self)
        self.characteristics = get_completion_from_prompt(prompt)
        return self
        
    
    def rate_cv(self, cv: str):
        prompt = rate_cv_prompt(self, cv)
        return get_completion_from_prompt(prompt)