import unittest
from collections import namedtuple
from day_19 import find_path

class TestPackagePath(unittest.TestCase):
    """Test finding package's path."""

    def test_find_path(self):
        Test = namedtuple('Test', ['tubes', 'expected'])
        tests = [Test(expected="ABCDEF", tubes=["     |          ",
                                                "     |  +--+    ",
                                                "     A  |  C    ",
                                                " F---|----E|--+ ",
                                                "     |  |  |  D ",
                                                "     +B-+  +--+ "])]

        for test in tests:
            result, _ = find_path(test.tubes)
            self.assertEqual("".join(result), test.expected)

    def test_find_path_steps(self):
        Test = namedtuple('Test', ['tubes', 'expected'])
        tests = [Test(expected=38, tubes=["     |          ",
                                          "     |  +--+    ",
                                          "     A  |  C    ",
                                          " F---|----E|--+ ",
                                          "     |  |  |  D ",
                                          "     +B-+  +--+ "])]

        for test in tests:
            _, result = find_path(test.tubes)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
