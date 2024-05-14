# Parameterization with fixture
import pytest


@pytest.fixture(params=[(3, 4), [3, 5]], ids=['tuple', 'list'])
def param_fixture01(request):
    return request.param


@pytest.fixture(params=["access", "slice"])
def param_fixture02(request):
    return request.param


def test_fix_param02(param_fixture01, param_fixture02):
    if param_fixture02 == 'access':
        assert param_fixture01[0]
    elif param_fixture02 == 'slice':
        assert param_fixture01[::-1]


def test_fix_param01(param_fixture01):
    assert type(param_fixture01) in [tuple, list]
