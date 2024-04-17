import unittest

# The function we want to test
def add(x, y):
    return x + y

# A test case class that inherits from unittest.TestCase
class TestAddFunction(unittest.TestCase):

    # Each test is a method whose name starts with "test_"
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)  # Assert that add(1, 2) returns 3

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)  # Assert that add(-1, -2) returns -3

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -2), -1)  # Assert that add(1, -2) returns -1

# This block allows running the tests from the command line



