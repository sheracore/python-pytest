import pytest
import math


@pytest.mark.parametrize('test_input', [32, 78, 95, 66])
def test_param01(test_input):
    assert test_input < 80


@pytest.mark.parametrize("inp, oup", [(2, 4), (3, 27), (4, 256)])
def test_param02(inp, oup):
    assert (inp ** inp) == oup


data = [
    ([2, 3, 4], 'sum', 9),
    ([2, 3, 4], 'prod', 24)
]


@pytest.mark.parametrize('a, b, c', data)
def test_param03(a, c, b):
    if b == 'sum':
        assert sum(a) == c
    elif b == 'prod':
        assert math.prod(a) == c
