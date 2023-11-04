import requests
import os
from tests.conftest import *
# from pytest
from .utils.positions import *
from .utils.utils import *
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def test_insert_all_cvs(get_folder_path: str | None, get_url_cv_adress: str | None):
    folder_path = get_folder_path
    url = get_url_cv_adress
    for filename in list_of_file_names(folder_path):
        path = os.path.join(folder_path, filename)
        files = {'cv': open(path, 'rb')}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print("File inserted")
            assert response.status_code == 200 

def test_check_cvs(get_url_cv_adress: str | None):
    url = get_url_cv_adress
    response = requests.get(url)
    assert response.status_code == 200 
    response_data_list = response.json()
    for response_data in response_data_list:
        type_exp_scr = response_data.get("metadata")["experience_score"]
        type_edc_scr = response_data.get("metadata")["education_score"]
        assert response_data.get("name") is not None
        assert response_data.get("id") is not None
        assert response_data.get("metadata") is not None
        assert type(type_exp_scr) == int
        assert type(type_edc_scr) == int
        assert response_data.get("filelink") is not None
        assert response_data.get("inserted_at") is not None

def test_insert_position(get_url_position_adress: str | None):
    url = get_url_position_adress
    for position_name, position_desc in positions.items():
        data = {
            'name': position_name,
            'description': position_desc
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("position inserted")
            assert response.status_code == 200

def test_check_position(get_url_position_adress: str | None):
    url = get_url_position_adress
    response = requests.get(url)
    assert response.status_code == 200 
    response_data_list = response.json()
    for response_data in response_data_list:
        assert response_data.get("metadata") is not None
        assert response_data.get("id") is not None
        assert response_data.get("name") is not None
        assert response_data.get("description") is not None
        assert response_data.get("inserted_at") is not None

def test_tokens_embedding_usage(get_url_tokens_adress: str | None):
    url = get_url_tokens_adress
    url = url + '/embedding'
    response = requests.get(url)
    assert response.status_code == 200
    assert int(response.text) > 0

def test_matcher_1(get_url_position_adress: str | None):
    for position_name in positions:
        id = get_one_position(position_name)
        url = get_url_position_adress + str(id) + '/match'
        response = requests.get(url)
        assert response.status_code == 200 

def test_matcher_2(get_url_position_adress: str | None):
    for position_name in positions:
        id = get_one_position(position_name)
        url = get_url_position_adress + str(id) + '/match2' 
        response = requests.get(url)
        assert response.status_code == 200

def test_tokens_llm_usage(get_url_tokens_adress: str | None):
    url = get_url_tokens_adress
    url = url + '/llm'
    response = requests.get(url)
    assert response.status_code == 200
    assert int(response.text) > 0

def test_delete_cvs(get_folder_path: str | None, get_url_cv_adress: str | None):
    folder_path = get_folder_path
    for name in get_filenames(folder_path):
        id = get_one_cv(name)
        url = get_url_cv_adress + str(id)
        response = requests.delete(url)
        assert response.status_code == 200
    url = get_url_cv_adress
    response = requests.get(url)
    assert response.status_code == 200
    response_data_list = response.json()
    for response_data in response_data_list:
        assert response_data.get("name") is None
        assert response_data.get("id") is None
        assert response_data.get("metadata") is None
        assert response_data.get("filelink") is None
        assert response_data.get("inserted_at") is None

def test_delete_positions(get_url_position_adress: str | None):
    for positions_name in positions:
        id = get_one_position(positions_name)
        url = get_url_position_adress + str(id)
        response = requests.delete(url)
        assert response.status_code == 200
    url = get_url_position_adress
    response = requests.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert "name" not in response_data
    assert "description" not in response_data
    assert "metadata" not in response_data
