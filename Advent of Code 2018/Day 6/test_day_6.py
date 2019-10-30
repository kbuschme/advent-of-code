import unittest
from collections import namedtuple
from day_6 import find_largest_area, find_suitable_region

class TestChronalCoordinates(unittest.TestCase):
    """Test chronal coordinates."""

    def test_find_largest_area(self):
        Test = namedtuple('Test', ['coordinates', 'expected'])
        tests = [
            Test(coordinates=[(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)],
                 expected=17)]

        for test in tests:
            result = find_largest_area(test.coordinates)
            self.assertEqual(result, test.expected)

    def test_find_suitable_region(self):
        Test = namedtuple('Test',
                          ['coordinates', 'max_total_distance', 'expected'])
        tests = [
            Test(coordinates=[(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)],
                 max_total_distance=32,
                 expected=16)]

        for test in tests:
            result = find_suitable_region(
                test.coordinates, max_total_distance=test.max_total_distance)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
