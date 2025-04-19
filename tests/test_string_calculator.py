import unittest
from calculator.string_calculator import add
import logging

logging.basicConfig(level=logging.DEBUG)

class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_zero(self):
        self.assertEqual(add(""), 0)
    
    def test_single_number(self):
        self.assertEqual(add("1"), 1)
    
    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(add("1,2,3,4"), 10)

    def test_newlines_as_delimiters(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_char_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_multiple_negative_numbers_in_exception(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2,-5")
        self.assertIn("negative numbers not allowed -2, -5", str(context.exception))

    def test_ignore_numbers_greater_than_1000(self):
        self.assertEqual(add("1001,2"), 2)
        self.assertEqual(add("1000,1001"), 1000)
        self.assertEqual(add("1000,1"), 1001)
    
    def test_delimiter_of_any_length(self):
        self.assertEqual(add("//[***]\n1***2***3"), 6)
    
    def test_multiple_single_char_delimiters(self):
        self.assertEqual(add("//[*][%]\n1*2%3"), 6)
    
    def test_multiple_long_delimiters(self):
        self.assertEqual(add("//[***][%%]\n1***2%%3"), 6)




if __name__ == "__main__":
    unittest.main()