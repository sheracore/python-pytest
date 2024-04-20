class TestClassBased:
    def test_type(self):
        assert type(1.3) is float

    def test_strs(self):
        assert 'python'.casefold() == 'PYThON'.casefold()
        assert 'pytest'.capitalize() == 'Pytest'


class TestClassBased2:
    def test_math(self):
        assert 4**2 == 16

