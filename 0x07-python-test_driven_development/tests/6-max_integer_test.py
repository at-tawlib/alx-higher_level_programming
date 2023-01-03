#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])"""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [4, 2, 1, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 2, 3, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_max_at_end(self):
        """Test a list with max at the end."""
        max_at_end = [2, 3, 1, 4]
        self.assertEqual(max_integer(max_at_end), 4)

    def test_empty_list(self):
        """Test for an empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_elemen_list(self):
        """Test a list with a single element"""
        one_element = [5]
        self.assertEqual(max_integer(one_element), 5)

    def test_floats(self):
        """Test a list of floats"""
        floats = [1.4, 5.7, 7.0, 8.9]
        self.assertEqual(max_integer(floats), 8.9)

    def test_ints_and_floats(self):
        """Test a list of ints and floats"""
        ints_and_floats = [3, 4.5, -9, 2.9]
        self.assertEqual(max_integer(ints_and_floats), 4.5)

    def test_string(self):
        """Test a string"""
        string_ = "Azindo"
        self.assertEqual(max_integer(string_), 'z')

    def test_list_of_strings(self):
        "Test a list of strings"""
        strings_ = ["Azindo", "at", "tawlib", "great"]
        self.assertEqual(max_integer(strings_), 'tawlib')

    def test_empty_string(self):
        """Test an empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
