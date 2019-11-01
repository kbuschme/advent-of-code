import unittest
from collections import namedtuple
from day_13 import parse_mine, drive_until_crash
from day_13 import drive_until_crash_remove_carts

class TestMineCarts(unittest.TestCase):
    """Test mine carts."""

    def test_parse_mine(self):
        Test = namedtuple('Test', ['mine', 'expected'])
        tests = [Test(expected=(44, 2), mine="""/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   """)]
        for test in tests:
            tracks, carts = parse_mine(test.mine)
            result = (len(tracks), len(carts))
            self.assertEqual(result, test.expected)

    def test_drive_until_crash(self):
        Test = namedtuple('Test', ['mine', 'expected'])
        tests = [Test(expected=(7,3), mine=["/->-\\        ",
                                            "|   |  /----\\",
                                            "| /-+--+-\\  |",
                                            "| | |  | v  |",
                                            "\\-+-/  \\-+--/",
                                            "  \\------/   "])]
        for test in tests:
            tracks, carts = parse_mine(test.mine)
            result = drive_until_crash(tracks, carts)
            self.assertEqual(result, test.expected)

    def test_drive_until_crash_remove_carts(self):
        Test = namedtuple('Test', ['mine', 'expected'])
        tests = [Test(expected=(6,4), mine=["/>-<\\  ",
                                            "|   |  ",
                                            "| /<+-\\",
                                            "| | | v",
                                            "\\>+</ |",
                                            "  |   ^",
                                            "  \\<->/"])]
        for test in tests:
            tracks, carts = parse_mine(test.mine)
            result = drive_until_crash_remove_carts(tracks, carts)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
