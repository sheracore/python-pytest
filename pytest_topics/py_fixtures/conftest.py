import pytest


def pytest_configure():
    pytest.weekdays1 = ['mon', 'tue', 'wed']
    pytest.weekdays2 = ['fri', 'sat', 'sun']


@pytest.fixture(scope="module")
def setup_conf_test_version01():
    wk1 = pytest.weekdays1.copy()
    wk1.append('thur')
    yield wk1
    # below two lines is related to tear-down operation, in another example you can close the selenium driver
    print('\n After yield in setup01 Fixture')
    wk1.clear()


@pytest.fixture()
def setup_conf_test_version02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, 'thur')
    yield wk2


@pytest.fixture()
def setup_conf_test_version04(request):
    mon = getattr(request.module, "months")
    print("\n in Fixture version04")
    print(f"\n Fixture scope: {str(request.scope)}")
    print(f"\n Calling function: {str(request.function.__name__)}")
    print(f"\n Calling module: {str(request.module.__name__)}")
    mon.append("April")
    yield mon


@pytest.fixture()
def setup_conf_test_version05():
    def get_structure(name):
        if name == 'list':
            return [1, 2, 3]
        elif name == 'tuple':
            return 1, 2, 3
    return get_structure
