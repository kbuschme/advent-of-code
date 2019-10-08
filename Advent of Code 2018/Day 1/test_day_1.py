import unittest
from collections import namedtuple
from day_1 import find_frequency_sum, find_repeated_frequency

class TestFrequencyModule(unittest.TestCase):
    """Test the frequency module."""

    def test_find_frequency_sum(self):
        Test = namedtuple('Test', ['changes', 'expected'])
        tests = [Test(changes=[1, -2, 3, 1], expected=3)]

        for test in tests:
            result = find_frequency_sum(test.changes)
            self.assertEqual(result, test.expected)

    def test_find_repeated_frequency(self):
        Test = namedtuple('Test', ['changes', 'expected'])
        tests = [Test(changes=[1, -2, 3, 1], expected=2)]

        for test in tests:
            result = find_repeated_frequency(test.changes)
            self.assertEqual(result, test.expected)


if __name__ == '__main__':
    unittest.main()
