"""
Unit test for factorial calculator library.
"""
import unittest
from factorial_calculator import factorial

class  TestFactorialCalculator(unittest.TestCase):


    def test_factorial(self):
        res = factorial(0)
        self.assertEqual(res, 1)
