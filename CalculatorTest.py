from unittest import TestCase

from Calculator import Calculator

class CalculatorTest(TestCase):

    def test_sum(self):
        self.assertEqual(Calculator().sum(''),0,'Empty string')

    def test_sum_one(self):
        self.assertEqual(Calculator().sum('1'),1,'One number')

    def test_sum_any_number(self):
        self.assertEqual(Calculator().sum('1'),1,'One string number')
        self.assertEqual(Calculator().sum('2'),2,'One string number')

    def test_sum_two_numbers(self):
        self.assertEqual(Calculator().sum('1,3'),4,'Two string numbers')

    def test_sum_any_numbers(self):
        self.assertEqual(Calculator().sum('5,2,4,1'),12,'Any string numbers')

    def test_sum_any_numbers_with_any_separators(self):
        self.assertEqual(Calculator().sum('5,2&4:1:2&8'),22,'Any string numbers with different separators')