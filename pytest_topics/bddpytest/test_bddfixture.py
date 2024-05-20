import pytest

from pathlib import Path
from pytest_bdd import scenario, scenarios, given, when, then

feature_file_dir = 'my_features'
feature_file = 'fixture.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE_PATH = BASE_DIR.joinpath(feature_file_dir).joinpath(feature_file)


scenarios(FEATURE_FILE_PATH)


@pytest.fixture()
def setup_set():
    print("\n In fixture... setup() function.. \n")
    return {'Poland', 'America', 'Iran', 'Canada', 'Australia'}


@given('A set of 3 fruits', target_fixture='setup_set_given')
def set_of_elements(setup_set):
    if len(setup_set) == 0:
        pytest.xfail("The set of elements is empty")
    elif len(setup_set) > 3:
        while len(setup_set) > 3:
            setup_set.pop()
    return setup_set


@when('Add 2 elements to the set')
def add_elements(setup_set_given):
    setup_set_given.add('India')
    setup_set_given.add('UK')


@then('the set should have 5 elements')
def final_set_elements(setup_set_given):
    assert len(setup_set_given) == 5
