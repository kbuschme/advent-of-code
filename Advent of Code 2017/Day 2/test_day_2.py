import unittest
from collections import namedtuple
from day_2 import max_min_difference_checksum, evenly_divisible_checksum

class TestChecksums(unittest.TestCase):
    """Test checksums."""

    def test_max_min_difference_checksum_checksum(self):
        Test = namedtuple('Test', ['spreadsheet', 'expected'])
        tests = [Test(spreadsheet=[[5,1,9,5], [7,5,3], [2,4,6,8]],
                      expected=18)]

        for test in tests:
            result = max_min_difference_checksum(test.spreadsheet)
            self.assertEqual(result, test.expected)

    def test_evenly_divisible_checksum(self):
        Test = namedtuple('Test', ['spreadsheet', 'expected'])
        tests = [Test(spreadsheet=[[5,9,2,8], [9,4,7,3], [3,8,6,5]],
                      expected=9)]

        for test in tests:
            result = evenly_divisible_checksum(test.spreadsheet)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
