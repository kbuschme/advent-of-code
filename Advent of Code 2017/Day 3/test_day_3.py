import unittest
from collections import namedtuple
from day_3 import distance_from_spiral_origin
from day_3 import find_sum_of_spiral_neighbours_larger_than

class TestDistanceFromSpiralOrigin(unittest.TestCase):
    """Test spiral memory."""

    def test_distance_from_spiral_origin(self):
        Test = namedtuple('Test', ['identified_square', 'expected_steps'])
        tests = [Test(identified_square=1, expected_steps=0),
                 Test(identified_square=12, expected_steps=3),
                 Test(identified_square=13, expected_steps=4),
                 Test(identified_square=23, expected_steps=2),
                 Test(identified_square=25, expected_steps=4),
                 Test(identified_square=1024, expected_steps=31)]

        for test in tests:
            result = distance_from_spiral_origin(test.identified_square)
            self.assertEqual(result, test.expected_steps)

    def test_find_sum_of_spiral_neighbours_larger_than(self):
        # Test cases: previous largest sum is limit for next test case
        Test = namedtuple('Test', ['limit', 'next_larger_neighbour_sum'])
        tests = [
            Test(limit=0, next_larger_neighbour_sum=1),
            Test(limit=1, next_larger_neighbour_sum=2),
            Test(limit=2, next_larger_neighbour_sum=4),
            Test(limit=4, next_larger_neighbour_sum=5),
            Test(limit=5, next_larger_neighbour_sum=10),
            Test(limit=10, next_larger_neighbour_sum=11),
            Test(limit=11, next_larger_neighbour_sum=23),
            Test(limit=23, next_larger_neighbour_sum=25),
            Test(limit=25, next_larger_neighbour_sum=26),
            Test(limit=26, next_larger_neighbour_sum=54),
            Test(limit=54, next_larger_neighbour_sum=57),
            Test(limit=57, next_larger_neighbour_sum=59),
            Test(limit=59, next_larger_neighbour_sum=122),
            Test(limit=122, next_larger_neighbour_sum=133),
            Test(limit=133, next_larger_neighbour_sum=142),
            Test(limit=142, next_larger_neighbour_sum=147),
            Test(limit=147, next_larger_neighbour_sum=304),
            Test(limit=304, next_larger_neighbour_sum=330),
            Test(limit=330, next_larger_neighbour_sum=351),
            Test(limit=351, next_larger_neighbour_sum=362),
            Test(limit=362, next_larger_neighbour_sum=747),
            Test(limit=747, next_larger_neighbour_sum=806),
        ]

        for test in tests:
            result = find_sum_of_spiral_neighbours_larger_than(test.limit)
            self.assertEqual(result, test.next_larger_neighbour_sum)

if __name__ == '__main__':
    unittest.main()
