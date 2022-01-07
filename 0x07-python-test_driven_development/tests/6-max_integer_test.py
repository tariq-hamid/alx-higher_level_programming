#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unittest class for max_integer """
    def test_ProperInput(self):
        """ test case for proper input """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([1.1, 1.3, 1.2]), 1.3)
        self.assertEqual(max_integer(['c', 'b', 'a']), 'c')
        self.assertEqual(max_integer([]), None)

    def test_ImproperInput(self):
        """ test case for improper input """
        with self.assertRaises(TypeError):
            max_integer(None)
            max_integer(['y', 2.5, 0])
            max_integer([[1, 2], 3])


if __name__ == "__main__":
    unittest.main()
