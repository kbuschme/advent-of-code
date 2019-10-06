import unittest
from collections import namedtuple
from day_21 import count_pixels

class TestFractalArt(unittest.TestCase):
    """Test Fractal Art."""

    def test_count_pixels(self):
        Test = namedtuple('Test', ['rules', 'iterations', 'expected'])
        tests = [
            Test(iterations=2, expected=12, rules=[
                "../.# => ##./#../...",
                ".#./..#/### => #..#/..../..../#..#"])]

        for test in tests:
            result = count_pixels(test.rules, iterations=test.iterations)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
