import os
import PyPDF2
from utilis import get_completion_from_prompt
from dics.constants import extract_name_prompt

class Cv:
    name: str
    content: str
    scores: list((str, int))

    def __init__(self, content: str):
        prompt = extract_name_prompt(content)
        self.name = get_completion_from_prompt(prompt)
        self.content = content

    def add_score(self, category: str, value: int):
       self.scores.push((category, value)) 

    def from_file(filename: str, folder_path=os.getenv('FOLDER_PATH')):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = [page.extract_text() for page in pdf_reader.pages]
            return Cv(' '.join(text))
        
    
    def from_directory(folder_path=os.getenv('FOLDER_PATH')):
        [Cv.from_file(file, folder_path) for file in os.listdir(folder_path)]