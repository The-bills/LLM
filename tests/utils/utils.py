import os
import pytest
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def list_of_file_names(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        filenames = [filename for filename in os.listdir(folder_path)]
        return filenames
    
def get_one_position(position_name):
    url = os.getenv('POSITION_URL')
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for position in data:
            if position['name'] == position_name:
                return position['metadata']['doc_id']

def get_one_cv(cv_name):
    url = os.getenv('CV_URL')
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for index in data:
            if index['name'] == cv_name:
                return index['metadata']['doc_id']
            
def get_filenames(folder_path):
    filenames = []
    for file in os.listdir(folder_path):
        filenames.append(os.path.splitext(file)[0])
    return filenames
    