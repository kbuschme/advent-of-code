import unittest
from collections import namedtuple
from day_24 import find_strongest_bridge, find_longest_bridge

class TestBridge(unittest.TestCase):
    """Test Bridge."""

    def test_find_strongest_bridge(self):
        Test = namedtuple('Test', ['components', 'expected'])
        tests = [
            Test(expected=([(0, 1), (1, 10), (10, 9)], 31),
                 components=[(2, 0), (2, 2), (2, 3), (3, 4),
                             (3, 5), (0, 1), (10, 1), (9, 10)])
        ]

        for test in tests:
            result = find_strongest_bridge(test.components)
            self.assertEqual(result, test.expected)

    def test_find_longest_bridge(self):
        Test = namedtuple('Test', ['components', 'expected'])
        tests = [
            Test(expected=([(0, 2), (2, 2), (2, 3), (3, 5)], 19),
                 components=[(2, 0), (2, 2), (2, 3), (3, 4),
                             (3, 5), (0, 1), (10, 1), (9, 10)])
        ]

        for test in tests:
            result = find_longest_bridge(test.components)
            self.assertEqual(result, test.expected)


if __name__ == '__main__':
    unittest.main()
