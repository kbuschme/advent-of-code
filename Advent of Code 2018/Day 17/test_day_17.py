import unittest
from collections import namedtuple
from day_17 import wet_tiles, wet_tiles

class TestReservoirs(unittest.TestCase):
    """Test Reservoirs."""

    def test_wet_tiles(self):
        Test = namedtuple('Test', ['scan', 'expected'])
        tests = [Test(scan=["x=495, y=2..7",
                            "y=7, x=495..501",
                            "x=501, y=3..7",
                            "x=498, y=2..4",
                            "x=506, y=1..2",
                            "x=498, y=10..13",
                            "x=504, y=10..13",
                            "y=13, x=498..504"],
                      expected=57)]

        for test in tests:
            result, _ = wet_tiles(test.scan)
            self.assertEqual(result, test.expected)

    def test_water_tiles(self):
        Test = namedtuple('Test', ['scan', 'expected'])
        tests = [Test(scan=["x=495, y=2..7",
                            "y=7, x=495..501",
                            "x=501, y=3..7",
                            "x=498, y=2..4",
                            "x=506, y=1..2",
                            "x=498, y=10..13",
                            "x=504, y=10..13",
                            "y=13, x=498..504"],
                      expected=29)]

        for test in tests:
            _, result = wet_tiles(test.scan)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
