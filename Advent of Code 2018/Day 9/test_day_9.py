import unittest
from collections import namedtuple
from day_9 import calculate_highest_score

class TestMarbleMania(unittest.TestCase):
    """Test Marble Mania"""

    def test_calculate_highest_score(self):
        Test = namedtuple('Test', ['players', 'last_marble', 'expected'])
        tests = [
            Test(players=9,  last_marble=25,   expected=32),
            Test(players=10, last_marble=1618, expected=8317),
            Test(players=13, last_marble=7999, expected=146373),
            Test(players=17, last_marble=1104, expected=2764),
            Test(players=21, last_marble=6111, expected=54718),
            Test(players=30, last_marble=5807, expected=37305),
        ]

        for test in tests:
            result = calculate_highest_score(test.players, test.last_marble)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
