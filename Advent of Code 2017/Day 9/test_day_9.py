import unittest
from collections import namedtuple
from day_9 import score, count_garbage

class TestStreamProcessing(unittest.TestCase):
    """Test Stream Processing."""

    def test_score(self):
        Test = namedtuple('Test', ['stream', 'expected'])
        tests = [
            Test(stream='{}', expected=1),
            Test(stream='{{{}}}', expected=6),
            Test(stream='{{},{}}', expected=5),
            Test(stream='{{{},{},{{}}}}', expected=16),
            Test(stream='{<a>,<a>,<a>,<a>}', expected=1),
            Test(stream='{{<ab>},{<ab>},{<ab>},{<ab>}}', expected=9),
            Test(stream='{{<!!>},{<!!>},{<!!>},{<!!>}}', expected=9),
            Test(stream='{{<a!>},{<a!>},{<a!>},{<ab>}}', expected=3)
        ]

        for test in tests:
            result = score(test.stream)
            self.assertEqual(result, test.expected)

    def test_count_garbage(self):
        Test = namedtuple('Test', ['stream', 'expected'])
        tests = [
            Test(stream='<>', expected=0),
            Test(stream='<random characters>', expected=17),
            Test(stream='<<<<>', expected=3),
            Test(stream='<{!>}>', expected=2),
            Test(stream='<!!>', expected=0),
            Test(stream='<!!!>>', expected=0),
            Test(stream='<{o"i!a,<{i<a>', expected=10)
        ]

        for test in tests:
            result = count_garbage(test.stream)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
