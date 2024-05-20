import pytest

from pathlib import Path
from pytest_bdd import scenario, scenarios, given, when, then

feature_file_dir = 'my_features'
feature_file = 'feature01.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE_PATH = BASE_DIR.joinpath(feature_file_dir).joinpath(feature_file)


def pytest_configure():  #global variable
    pytest.AMT = 0


scenarios(FEATURE_FILE_PATH)


# @scenario(FEATURE_FILE_PATH, 'Withdrawal of money')
# def test_withdrawal():
#     print("End of withdeawal test")
#     pass


@given('the account balance is 100')
def current_balance():
    pytest.AMT = 100


@when('the account holder withdraws 30')
def withdraw_amount():
    pytest.AMT = pytest.AMT - 30


@then('the account balance should be 70')
def final_balance():
    assert pytest.AMT == 70


# @scenario(FEATURE_FILE_PATH,'Removal of items from set')
# def test_remove_of_items():
#     pass


@given('A set of 3 fruits', target_fixture="my_set")
def current_balance():
    return {"apple", "banana", "cherry"}


@when('We remove a fruit from the set')
def remove_fruit(my_set):
    my_set.pop()
    print(my_set)


@then('the set should have 5 elements')
def final_set(my_set):
    assert len(my_set) == 2
