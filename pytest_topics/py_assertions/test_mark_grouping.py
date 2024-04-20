import pytest

pytestmark = [pytest.mark.smoke, pytest.mark.mamad]


@pytest.mark.sanity
def test_01():
    assert '1.4.5' < '1.4.6'


@pytest.mark.sanity
def test_02():
    assert '1.4.5' < '1.4.6'


@pytest.mark.str
def test_03():
    assert '1.4.5' < '1.4.6'


@pytest.mark.sanity
def test_04():
    assert '1.4.5' < '1.4.6'


@pytest.mark.str
@pytest.mark.sanity
def test_05():
    assert '1.4.5' < '1.4.6'
