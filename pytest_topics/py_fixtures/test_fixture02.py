import pytest
import os

weekdays1 = ['mon', 'tue', 'wed']
weekdays2 = ['fri', 'sat', 'sun']
filename = 'file1.txt'


@pytest.fixture()
def setup01():
    wk1 = weekdays1.copy()
    wk1.append('thur')
    yield wk1
    # below two lines is related to tear-down operation, in another example you can close the selenium driver
    print('\n After yield in setup01 Fixture')
    wk1.clear()


@pytest.fixture()
def setup02():
    wk2 = weekdays2.copy()
    wk2.insert(0, 'thur')
    yield wk2


@pytest.fixture()
def setup03():
    f = open(filename, 'w')
    f.write('Pytest is good')
    f.close()
    f = open(filename, 'r+')
    yield f
    f.close()
    os.remove(filename)


def test_extend_list(setup01):
    setup01.extend(weekdays2)
    assert setup01 == ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']


def test_len(setup01, setup02):
    assert len(weekdays1 + setup02) == len(setup01 + weekdays2)


def test_filetest(setup03):
    assert (setup03.readline()) == 'Pytest is good'
