from dotenv import load_dotenv, find_dotenv
import numpy as np
import scipy.stats as st
import math as mt
from scipy.stats import chi2_contingency
from dics.default_position import test_rating, test_data
import warnings
from src.fixtures import base_classes, described_data, rate_test_cv
warnings.filterwarnings('ignore')
_ = load_dotenv(find_dotenv())


def test_described_data(described_data):
    assert described_data == test_data


def test_evaluate_cv(rate_test_cv):
    assert rate_test_cv == [80, 60, 100, 80, 80] 


def test_evaluate_approx(rate_test_cv):
    assert np.isclose(sum(rate_test_cv),sum(test_rating),rtol=1)


def test_check_evaluation_partialy(rate_test_cv):
    output = []
    for (i,j) in zip(rate_test_cv, test_rating):
        z = int(i) - int(j)
        output.append(z)
    assert abs(sum(output)) >= np.std(rate_test_cv)


def test_check_mean(rate_test_cv):
    assert np.isclose(np.mean(rate_test_cv),np.mean(test_rating),rtol=1)


def test_check_std(rate_test_cv):
    cv_std = np.std(rate_test_cv)
    manual_std = np.std(test_rating)
    assert np.isclose(cv_std, manual_std,rtol=1)        


def test_t_student(rate_test_cv):
    cv_rated_mean = np.mean(rate_test_cv)
    test_rated_mean = np.mean(test_rating)
    std_cv = np.std(rate_test_cv)
    std_test = np.std(test_rating)
    t_value = (cv_rated_mean-test_rated_mean)/mt.sqrt((pow(std_cv,2)/len(rate_test_cv))+(pow(std_test,2)/len(test_rating)))
    degrees_of_freedom = len(rate_test_cv) + len(test_rating) - 2
    p_value = 2 * (1 - st.t.cdf(abs(t_value), df=degrees_of_freedom))
    assert np.isclose(p_value, 0.05, rtol=0.01) or p_value >= 0.05
    

def test_levane(rate_test_cv):
    cv_median = np.median(rate_test_cv)
    test_median = np.median(test_rating)
    abs_cv = [abs(x - cv_median) for x in rate_test_cv]
    abs_test = [abs(x - test_median) for x in test_rating]
    cv_abs_median = np.median(abs_cv)
    test_abs_median = np.median(abs_test)
    levene_statistic = (pow(cv_abs_median,2)+ pow(test_abs_median,2))/2
    p_value = 1-st.chi2.cdf(levene_statistic, df=1)
    assert np.isclose(p_value, 0.05, rtol=0.01) or p_value <= 0.05


def test_pearson_correlation(rate_test_cv):
    corr_pearson = np.corrcoef(rate_test_cv, test_rating)[0, 1]
    assert corr_pearson > 0.0


def test_chi_square(rate_test_cv):
    test_array = np.array([rate_test_cv, test_rating])
    chi2, p, dof, expected = chi2_contingency(test_array)
    assert np.isclose(p, 0.05, rtol=0.01) or p >= 0.05


def test_percentage_diffrence(rate_test_cv):
    rate_test_cv_sum = sum(rate_test_cv)
    test_rating_sum = sum(test_rating)
    assert abs(rate_test_cv_sum-test_rating_sum)/test_rating_sum <= 0.1
