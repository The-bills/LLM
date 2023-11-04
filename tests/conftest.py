import pytest
import os

@pytest.fixture(scope='session')
def get_folder_path():
    folder_path = os.getenv('TEST_FOLDER_PATH')
    return folder_path

@pytest.fixture(scope='session')
def get_url_cv_adress():
    url = os.getenv('CV_URL')
    return url

@pytest.fixture(scope='session')
def get_url_position_adress():
    url = os.getenv('POSITION_URL')
    return url

@pytest.fixture(scope='session')
def get_url_tokens_adress():
    url = os.getenv('TOKENS_URL')
    return url

#Wywoływanie sekwencji testów
@pytest.fixture(scope="session", autouse=True)
def run_test_sequence(request):
    test_sequence = [
        'test_insert_all_cv',
        'test_check_cvs',
        'test_insert_position',
        'test_check_position',
        'test_tokens_embedding_usage',
        'test_matcher_1',
        'test_matcher_2',
        'test_tokens_llm_usage',
        'test_delete_cvs',
        'test_delete_positions'
    ]
    request.config._sequence_counter = 0
    request.config._test_sequence = test_sequence

#Wywoływanie kolejnego testu z sekwencji
@pytest.fixture(scope="function", autouse=True)
def get_next_test(request):
    test_sequence = request.config._test_sequence
    if request.config._sequence_counter < len(test_sequence):
        next_test_name = test_sequence[request.config._sequence_counter]
        request.config._sequence_counter += 1
        return next_test_name
    else:
        return None
