import pytest


def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert (1/0)


def test_case02():
    with pytest.raises(Exception) as excinfo:
        func()

    print(str(excinfo))
    assert (str(excinfo.value)) == 'Exception func1 raised'


def func():
    raise ValueError('IndexError func1 raised')
