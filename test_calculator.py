"""
Unit test for calculator library.
"""

import calculator


class TestCalculator:

    def test_adition(self):
        assert 4 == calculator.add(2, 2)

    def test_substraction(self):
        assert 2 == calculator.subtract(4, 2)
