import pytest
import os


def pytest_configure():
    pytest.filename = 'file1.txt'


@pytest.fixture()
def setup_conf_test_version03():
    f = open(pytest.filename, 'w')
    f.write('Pytest is good')
    f.close()
    f = open(pytest.filename, 'r+')
    yield f
    f.close()
    os.remove(pytest.filename)


QA_config = '/home/mohammad/Desktop/technical bump projects/python-pytest/pytest_topics/qa.prop'
prod_config = '/home/mohammad/Desktop/technical bump projects/python-pytest/pytest_topics/prod.prop'


def pytest_addoption(parser):
    parser.addoption("--cmdopt", default='QA')


@pytest.fixture()
def command_opt(pytestconfig):
    print("\n In command_opt fixture")
    opt = pytestconfig.getoption('cmdopt')
    if opt == 'QA':
        f = open(QA_config, 'r')
    else:
        f = open(prod_config, 'r')
    yield f
