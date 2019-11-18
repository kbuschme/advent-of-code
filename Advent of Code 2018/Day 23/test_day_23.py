import unittest
from collections import namedtuple
from day_23 import parse_bot_positions
from day_23 import find_nanobots_in_range, find_shortest_distance

class TestNanobots(unittest.TestCase):
    """Test nanobots."""

    def test_parse_bot_positions(self):
        Test = namedtuple('Test', ['bot_positions', 'expected'])
        tests = [
            Test(bot_positions=["pos=<0,0,0>, r=4",
                                "pos=<1,0,0>, r=1",
                                "pos=<4,0,0>, r=3",
                                "pos=<0,2,0>, r=1",
                                "pos=<0,5,0>, r=3",
                                "pos=<0,0,3>, r=1",
                                "pos=<1,1,1>, r=1",
                                "pos=<1,1,2>, r=1",
                                "pos=<1,3,1>, r=1"],
                 expected={(0,0,0) :4,
                           (1,0,0) :1,
                           (4,0,0) :3,
                           (0,2,0) :1,
                           (0,5,0) :3,
                           (0,0,3) :1,
                           (1,1,1) :1,
                           (1,1,2) :1,
                           (1,3,1) :1})]

        for test in tests:
            result = parse_bot_positions(test.bot_positions)
            self.assertEqual(result, test.expected)

    def test_find_nanobots_in_range(self):
        Test = namedtuple('Test', ['bot_positions', 'expected'])
        tests = [
            Test(expected=7,
                 bot_positions=["pos=<0,0,0>, r=4",
                                "pos=<1,0,0>, r=1",
                                "pos=<4,0,0>, r=3",
                                "pos=<0,2,0>, r=1",
                                "pos=<0,5,0>, r=3",
                                "pos=<0,0,3>, r=1",
                                "pos=<1,1,1>, r=1",
                                "pos=<1,1,2>, r=1",
                                "pos=<1,3,1>, r=1"])]

        for test in tests:
            nanobots = parse_bot_positions(test.bot_positions)
            result = find_nanobots_in_range(nanobots)
            self.assertEqual(result, test.expected)

    def test_find_shortest_distance(self):
        Test = namedtuple('Test', ['bot_positions', 'expected'])
        tests = [
            Test(expected=36,
                 bot_positions=["pos=<10,12,12>, r=2",
                                "pos=<12,14,12>, r=2",
                                "pos=<16,12,12>, r=4",
                                "pos=<14,14,14>, r=6",
                                "pos=<50,50,50>, r=200",
                                "pos=<10,10,10>, r=5",])]

        for test in tests:
            nanobots = parse_bot_positions(test.bot_positions)
            result = find_shortest_distance(nanobots)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
