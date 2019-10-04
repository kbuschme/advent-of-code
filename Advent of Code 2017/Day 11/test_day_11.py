import unittest
from collections import namedtuple
from day_11 import caluclate_distance

class TestHexEd(unittest.TestCase):
    """Test Hex Ed."""

    def test_caluclate_distance(self):
        Test = namedtuple('Test', ['path', 'expected'])
        tests = [
            Test(path=['ne','ne','ne'], expected=3),
            Test(path=['ne','ne','sw','sw'], expected=0),
            Test(path=['ne','ne','s','s'], expected=2),
            Test(path=['se','sw','se','sw','sw'], expected=3)]

        for test in tests:
            result = caluclate_distance(test.path)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
