import unittest
from collections import namedtuple
from day_22 import build_cave, cave_to_string, assess_total_risk, find_friend

class TestMaze(unittest.TestCase):
    """Test Maze."""

    def test_build_cave(self):
        Test = namedtuple('Test', ['depth', 'target', 'expected'])
        tests = [Test(depth=510, target=(10, 10), expected="\n".join([
            'M=.|=.|.|=.',
            '.|=|=|||..|',
            '.==|....||=',
            '=.|....|.==',
            '=|..==...=.',
            '=||.=.=||=|',
            '|.=.===|||.',
            '|..==||=.|=',
            '.=..===..=|',
            '.======|||=',
            '.===|=|===T']))
        ]
        for test in tests:
            result = cave_to_string(build_cave(test.depth, test.target))
            self.assertEqual(result, test.expected)

    def test_assess_total_risk(self):
        Test = namedtuple('Test', ['depth', 'target', 'expected'])
        tests = [Test(depth=510, target=(10, 10), expected=114)]
        for test in tests:
            cave = build_cave(test.depth, test.target)
            result = assess_total_risk(cave)
            self.assertEqual(result, test.expected)

    def test_find_friend(self):
        Test = namedtuple('Test', ['depth', 'target', 'expected'])
        tests = [
            Test(depth=510, target=(10, 10), expected=45)
        ]
        for test in tests:
            x_max, y_max = test.target[0] + 10, test.target[1] + 10
            cave = build_cave(test.depth, test.target,
                x_max=x_max, y_max=y_max)
            result = find_friend(cave, test.target)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
