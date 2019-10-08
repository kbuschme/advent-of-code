import unittest
from collections import namedtuple
from day_2 import calculate_checksum, find_common_letters

class TestInventoryManagementSystem(unittest.TestCase):
    """Test functions on the inventory management system."""

    def test_calculate_checksum(self):
        Test = namedtuple('Test', ['box_ids', 'expected'])
        tests = [Test(expected=12, box_ids=[
            "abcdef",
            "bababc",
            "abbcde",
            "abcccd",
            "aabcdd",
            "abcdee",
            "ababab"])]

        for test in tests:
            result = calculate_checksum(test.box_ids)
            self.assertEqual(result, test.expected)

    def test_find_common_letters(self):
        Test = namedtuple('Test', ['box_ids', 'expected'])
        tests = [Test(expected="fgij", box_ids=[
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "fguij",
            "axcye",
            "wvxyz"])]

        for test in tests:
            result = find_common_letters(test.box_ids)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()




