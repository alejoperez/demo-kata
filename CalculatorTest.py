from unittest import TestCase

from Calculator import Calculator

class CalculatorTest(TestCase):

    def test_sum(self):
        self.assertEqual(Calculator().sum(''),0,'Empty string')

    def test_sum_one(self):
        self.assertEqual(Calculator().sum('1'),1,'One number')