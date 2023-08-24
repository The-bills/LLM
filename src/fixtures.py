import pytest
from dotenv import load_dotenv, find_dotenv
from utilis.LangModel import LangModel
from utilis.Cv import Cv
from dics.default_position import test_description, test_name, test_rating, test_data
import warnings
warnings.filterwarnings('ignore')
_ = load_dotenv(find_dotenv())



@pytest.fixture
def base_classes():
    llm = LangModel
    cv = Cv.from_file('Raynell_Sciota.pdf')
    return llm, cv


@pytest.fixture
def described_data(base_classes):
    llm, cv = base_classes
    described_data = llm.describe_position(test_name, test_description)
    return described_data


@pytest.fixture
def rate_test_cv(base_classes, described_data):
    llm, cv = base_classes
    tests_rate_cv = llm.rate_cv(test_name, test_description, described_data,cv)
    tests_rate_cv_int = list(map(int, tests_rate_cv))
    return tests_rate_cv_int
