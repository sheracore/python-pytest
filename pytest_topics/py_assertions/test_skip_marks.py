import sys
import pytest

pytestmark = pytest.mark.skipif(sys.version_info < (3, 8, 2), reason="does not run on windows")
# pytestmark = pytest.mark.skipif(pytest.__version__ != '8.1.1', reason='default value test, so skipping')
# pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")

const = 9/5


def celsius_to_fahrenheit(celsius=0):
    """
    Convert Celsius to Fahrenheit.

    Parameters:
    - celsius (float): Temperature in Celsius.

    Returns:
    - float: Temperature converted to Fahrenheit.
    """
    fahrenheit = (celsius * const) + 32
    return fahrenheit


@pytest.mark.skip(reason="Skipping for no reason specified")
def test_01():
    assert type(const) is float


@pytest.mark.skipif(sys.version_info < (3, 8, 2), reason="Doesn't work on py version above 3.8.2")
def test_02():
    assert celsius_to_fahrenheit(100) == 212


@pytest.mark.skipif(False, reason="Doesn't work on py version above 3.8.2")
def test_03():
    assert celsius_to_fahrenheit(30) == 86


@pytest.mark.skipif(celsius_to_fahrenheit() == 32, reason='default value test, so skipping')
def test_04():
    assert celsius_to_fahrenheit(44) == 111.2


@pytest.mark.skipif(pytest.__version__ > '8.1.0', reason='default value test, so skipping')
def test_05():
    assert celsius_to_fahrenheit(44) == 111.2

