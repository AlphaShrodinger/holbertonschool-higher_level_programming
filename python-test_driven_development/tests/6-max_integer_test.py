#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer_with_non_empty_list(self):
        test_cases = [
            ([1, 2, 3, 4], 4),
            ([1, 3, 4, 2], 4),
            ([-1, -2, -3, -4], -1),
            ([5], 5)
        ]
        for input_list, expected_result in test_cases:
            with self.subTest(input_list=input_list, expected_result=expected_result):
                self.assertEqual(max_integer(input_list), expected_result)

    def test_max_integer_with_empty_list(self):
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
    print("ok")
