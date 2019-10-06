import unittest
from collections import namedtuple
from day_16 import dance, dance_repeatedly

class Test(unittest.TestCase):
    """Test dance moves."""

    def test_dance(self):
        Test = namedtuple('Test', ['dancers', 'moves', 'expected'])
        tests = [
            Test(dancers='abcde', moves=['s1'],   expected='eabcd'),
            Test(dancers='eabcd', moves=['x3/4'], expected='eabdc'),
            Test(dancers='eabdc', moves=['pe/b'], expected='baedc'),
            Test(dancers='baedc', moves=['s1'],   expected='cbaed'),
            Test(dancers='cbaed', moves=['x3/4'], expected='cbade'),
            Test(dancers='cbade', moves=['pe/b'], expected='ceadb')]

        for test in tests:
            result = dance(test.dancers, test.moves)
            self.assertEqual(result, test.expected)

    def test_dance_repeatedly(self):
        Test = namedtuple('Test',
                          ['dancers', 'moves', 'repetitions', 'expected'])
        tests = [Test(dancers='abcde', moves=['s1', 'x3/4', 'pe/b'],
                     repetitions=2, expected='ceadb')]
        for test in tests:
            result = dance_repeatedly(test.dancers, test.moves,
                                      repetitions=test.repetitions)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
