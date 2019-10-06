import unittest
from collections import namedtuple
from day_17 import find_value_after_last_insert
from day_17 import find_value_after_zero_brute_force, find_value_after_zero

class TestCircularBuffer(unittest.TestCase):
    """Test Circular Buffer."""

    def test_find_value_after_last_insert(self):
        Test = namedtuple('Test', ['steps', 'max_value', 'expected'])
        tests = [Test(steps=3, max_value=9, expected=5)]

        for test in tests:
            result = find_value_after_last_insert(test.steps, test.max_value)
            self.assertEqual(result, test.expected)

    def test_find_value_after_zero_brute_force(self):
        Test = namedtuple('Test', ['steps', 'max_value', 'expected'])
        tests = [Test(steps=3, max_value=9, expected=9),
                 Test(steps=3, max_value=7, expected=5),
                 Test(steps=3, max_value=8, expected=5)]

        for test in tests:
            result = find_value_after_zero_brute_force(
                test.steps, test.max_value)
            self.assertEqual(result, test.expected)

    def test_find_value_after_zero(self):
        Test = namedtuple('Test', ['steps', 'max_value', 'expected'])
        tests = [Test(steps=3, max_value=9, expected=9),
                 Test(steps=3, max_value=7, expected=5),
                 Test(steps=3, max_value=8, expected=5)]

        for test in tests:
            result = find_value_after_zero(test.steps, test.max_value)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
