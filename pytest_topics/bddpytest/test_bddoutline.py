from pathlib import Path
from pytest_bdd import scenarios, given, when, then, parsers

feature_file_dir = 'my_features'
feature_file = 'scenario_outline.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE_PATH = BASE_DIR.joinpath(feature_file_dir).joinpath(feature_file)


scenarios(FEATURE_FILE_PATH)


@given(parsers.parse('there are {start:d} cucumbers'), target_fixture='cucumbers')
def existing_cucumber(start):
    return dict(start=start)


@when(parsers.parse('I deposit {deposit:d} cucumbers'))
def deposit_cucumber(cucumbers, deposit):
    cucumbers["deposit"] = deposit
    print(cucumbers)


@when(parsers.parse('I withdraw {withdraw:d} cucumbers'))
def withdraw_cucumber(cucumbers, withdraw):
    cucumbers['withdraw'] = withdraw
    print(cucumbers)


@then(parsers.parse('I should have {final:d} cucumbers'))
def remain_cucumber(cucumbers, final):
    assert final == cucumbers['start'] + cucumbers['deposit'] - cucumbers['withdraw']