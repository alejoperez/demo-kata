from unittest import TestCase

from Calculator import Calculator

class CalculatorTest(TestCase):
    def test_sum(self):
        self.assertEqual(Calculator().sum(''),0,'Cadena Vacia')
