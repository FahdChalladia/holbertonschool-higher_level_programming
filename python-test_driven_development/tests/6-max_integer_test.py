#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.1]), 3.1)

    def test_strings_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

    def test_none_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_non_list_argument(self):
        with self.assertRaises(TypeError):
            max_integer("not a list")


if __name__ == "__main__":
    unittest.main()
