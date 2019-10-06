import unittest
from collections import namedtuple
from day_14 import calculate_used_squares, calculate_regions

class TestDiskDefragmentation(unittest.TestCase):
    """Test Disk Defragmentation."""

    def test_calculate_used_squares(self):
        Test = namedtuple('Test', ['key', 'expected'])
        tests = [Test(key='flqrgnkx', expected=8108),]

        for test in tests:
            result = calculate_used_squares(test.key)
            self.assertEqual(result, test.expected)

    def test_calculate_regions(self):
        Test = namedtuple('Test', ['key', 'expected'])
        tests = [Test(key='flqrgnkx', expected=1242),]

        for test in tests:
            result = calculate_regions(test.key)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
