import unittest
from collections import namedtuple
from day_7 import origin, find_adjustment

class TestTower(unittest.TestCase):
    """Test Tower of programs."""

    def test_origin(self):
        Test = namedtuple('Test', ['tower', 'expected'])
        tests = [
            Test(tower=['pbga (66)',
                        'xhth (57)',
                        'ebii (61)',
                        'havc (66)',
                        'ktlj (57)',
                        'fwft (72) -> ktlj, cntj, xhth',
                        'qoyq (66)',
                        'padx (45) -> pbga, havc, qoyq',
                        'tknk (41) -> ugml, padx, fwft',
                        'jptl (61)',
                        'ugml (68) -> gyxo, ebii, jptl',
                        'gyxo (61)',
                        'cntj (57)'],
                 expected='tknk')]

        for test in tests:
            result = origin(test.tower)
            self.assertEqual(result, test.expected)

    def test_find_adjustment(self):
        Test = namedtuple('Test', ['tower', 'expected'])
        tests = [
            Test(tower=['pbga (66)',
                        'xhth (57)',
                        'ebii (61)',
                        'havc (66)',
                        'ktlj (57)',
                        'fwft (72) -> ktlj, cntj, xhth',
                        'qoyq (66)',
                        'padx (45) -> pbga, havc, qoyq',
                        'tknk (41) -> ugml, padx, fwft',
                        'jptl (61)',
                        'ugml (68) -> gyxo, ebii, jptl',
                        'gyxo (61)',
                        'cntj (57)'],
                 expected=('ugml', 60))]

        for test in tests:
            result = find_adjustment(test.tower)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
