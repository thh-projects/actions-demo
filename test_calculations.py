from calculations import add, multiply, power


class TestCalculations:
    def test_add(self):
        assert add(2, 3) == 5
        assert add(2, 2) != 5

    def test_multiply(self):
        assert multiply(4, 5) == 20

    def test_power(self):
        assert power(3, 5) == 243
