import unittest
from collections import namedtuple
from day_25 import find_constellations

class TestConstellation(unittest.TestCase):
    """Test Constellation."""

    def test_find_constellations(self):
        Test = namedtuple('Test', ['fixed_points', 'expected'])
        tests = [
            Test(
                fixed_points=([
                    ( 0, 0, 0, 0),
                    ( 3, 0, 0, 0),
                    ( 0, 3, 0, 0),
                    ( 0, 0, 3, 0),
                    ( 0, 0, 0, 3),
                    ( 0, 0, 0, 6),
                    ( 9, 0, 0, 0),
                    (12, 0, 0, 0)]),
                expected=2),
            Test(
                fixed_points=([
                    ( 0, 0, 0, 0),
                    ( 3, 0, 0, 0),
                    ( 0, 3, 0, 0),
                    ( 0, 0, 3, 0),
                    ( 0, 0, 0, 3),
                    ( 0, 0, 0, 6),
                    ( 9, 0, 0, 0),
                    (12, 0, 0, 0),
                    (6, 0, 0, 0)]),
                expected=1),
            Test(
                fixed_points=([
                    (-1, 2, 2, 0),
                    ( 0, 0, 2,-2),
                    ( 0, 0, 0,-2),
                    (-1, 2, 0, 0),
                    (-2,-2,-2, 2),
                    ( 3, 0, 2,-1),
                    (-1, 3, 2, 2),
                    (-1, 0,-1, 0),
                    ( 0, 2, 1,-2),
                    ( 3, 0, 0, 0)]),
                expected=4),
            Test(
                fixed_points=([
                    (-1, 2, 2, 0),
                    ( 0, 0, 2,-2),
                    ( 0, 0, 0,-2),
                    (-1, 2, 0, 0),
                    (-2,-2,-2, 2),
                    ( 3, 0, 2,-1),
                    (-1, 3, 2, 2),
                    (-1, 0,-1, 0),
                    ( 0, 2, 1,-2),
                    ( 3, 0, 0, 0)]),
                expected=4),
            Test(
                fixed_points=([
                    ( 1,-1, 0, 1),
                    ( 2, 0,-1, 0),
                    ( 3, 2,-1, 0),
                    ( 0, 0, 3, 1),
                    ( 0, 0,-1,-1),
                    ( 2, 3,-2, 0),
                    (-2, 2, 0, 0),
                    ( 2,-2, 0,-1),
                    ( 1,-1, 0,-1),
                    ( 3, 2, 0, 2)]),
                expected=3),
            Test(
                fixed_points=([
                    ( 1,-1,-1,-2),
                    (-2,-2, 0, 1),
                    ( 0, 2, 1, 3),
                    (-2, 3,-2, 1),
                    ( 0, 2, 3,-2),
                    (-1,-1, 1,-2),
                    ( 0,-2,-1, 0),
                    (-2, 2, 3,-1),
                    ( 1, 2, 2, 0),
                    (-1,-2, 0,-2)]),
                expected=8),
        ]

        for test in tests:
            result = find_constellations(test.fixed_points)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
