import sys
import pytest


@pytest.mark.xfail
def test_01():
    letter = 'abc'
    assert letter[3]


@pytest.mark.xfail(reason='known issue')
def test_02():
    assert 3 + '4'


@pytest.mark.xfail(sys.platform == 'win32', reason='works only in win32')
def test_03():
    letter = 'abc'
    assert letter[2]


@pytest.mark.xfail(raises=IndexError, reason='known issue')
def test_01():
    letter = 'abc'
    assert letter[3]


@pytest.mark.xfail(raises=TypeError, reason='known issue')
def test_04():
    letter = 'abc'
    assert letter[3]
