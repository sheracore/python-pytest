import pytest


months = ["Jan", "Feb", "Mar"]


def test_check_request_fixture(setup_conf_test_version04):
    assert 1 == 1
    assert "April" in setup_conf_test_version04
    assert "April" in months  # because lists are mutable


def test_fact_fixture(setup_conf_test_version05):
    assert isinstance(setup_conf_test_version05('list'), list)
    assert isinstance(setup_conf_test_version05('tuple'), tuple)
