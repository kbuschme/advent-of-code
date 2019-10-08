import unittest
from collections import namedtuple
from day_5 import react, shortest_polymer_minus_unit

class TestPolymerReaction(unittest.TestCase):
    """Test reaction of the polymer"""

    def test_react(self):
        Test = namedtuple('Test', ['polymer', 'expected'])
        tests = [
            Test(polymer="aA", expected=""),
            Test(polymer="abBA", expected=""),
            Test(polymer="abAB", expected="abAB"),
            Test(polymer="aabAAB", expected="aabAAB"),
            Test(polymer="dabAcCaCBAcCcaDA", expected="dabCBAcaDA")]

        for test in tests:
            result = react(test.polymer)
            self.assertEqual(result, test.expected)

    def test_shortest_polymer_minus_unit(self):
        Test = namedtuple('Test', ['polymer', 'expected'])
        tests = [
            Test(polymer="dabAcCaCBAcCcaDA", expected=4)]

        for test in tests:
            result = shortest_polymer_minus_unit(test.polymer)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
