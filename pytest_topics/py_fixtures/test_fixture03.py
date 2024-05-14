import pytest


def test_del_item(setup_conf_test_version01):
    del setup_conf_test_version01[-1]
    print(setup_conf_test_version01)
    assert setup_conf_test_version01 == pytest.weekdays1


def test_remove_item(setup_conf_test_version02):
    print(setup_conf_test_version02)
    setup_conf_test_version02.remove('thur')
    assert setup_conf_test_version02 == pytest.weekdays2


def test_filetest_with_outer_conf_test(setup_conf_test_version03):
    assert (setup_conf_test_version03.readline()) == 'Pytest is good'
