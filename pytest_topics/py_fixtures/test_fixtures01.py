import pytest


# tear-up
@pytest.fixture()
def setup_list():
    print("\n in fixtures...\n")
    city = ['a', 'v', 'c']
    return city


def my_reverse(lst: list) -> list:
    lst.reverse()
    return lst


def test_get_item(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'a'
    assert setup_list[::-1] == ['c', 'v', 'a']  # my_list[start:stop:step]
    assert setup_list[::-1] == my_reverse(setup_list)


def test_reverse_list(setup_list):
    assert setup_list[::-1] == my_reverse(setup_list)


@pytest.mark.xfail(reason="known issue: 'usefixtures' cannot use the fixture's return value")
@pytest.mark.usefixtures("setup_list")
def test_use_fixture_demo():
    assert 1 == 1
    print(setup_list[0])

