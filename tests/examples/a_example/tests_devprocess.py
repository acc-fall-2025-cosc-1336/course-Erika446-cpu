import unittest

from src.examples.a_example.devprocess import echo_value, multiply_numbers

class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self):
        self.assertEqual(2, multiply_numbers(7, 7))
        self.assertEqual(2, multiply_numbers(5, 5))

