import unittest
from collections import namedtuple
from day_15 import generate, count_matches, count_matches

class TestDuelingGenerators(unittest.TestCase):
    """Test Dueling Generators."""

    def test_generate(self):
        Test = namedtuple('Test', ['previous', 'factor','expected'])
        tests = [
            Test(previous=65,         factor=16807, expected=1092455),
            Test(previous=1092455,    factor=16807, expected=1181022009),
            Test(previous=1181022009, factor=16807, expected=245556042),
            Test(previous=245556042,  factor=16807, expected=1744312007),
            Test(previous=1744312007, factor=16807, expected=1352636452),
            Test(previous=8921,       factor=48271, expected=430625591),
            Test(previous=430625591,  factor=48271, expected=1233683848),
            Test(previous=1233683848, factor=48271, expected=1431495498),
            Test(previous=1431495498, factor=48271, expected=137874439),
            Test(previous=137874439,  factor=48271, expected=285222916),
        ]

        for test in tests:
            result = generate(test.previous, test.factor)
            self.assertEqual(result, test.expected)

    def test_count_matches(self):
        Test = namedtuple('Test', ['starting_values', 'factors', 'expected'])
        tests = [Test(starting_values={'A': 65, 'B': 8921},
                      factors={'A': 16807, 'B': 48271},
                      expected=588)]

        for test in tests:
            result = count_matches(test.starting_values, test.factors)
            self.assertEqual(result, test.expected)

    def test_count_matches_multiple(self):
        Test = namedtuple('Test',
            ['starting_values', 'factors', 'multiples', 'expected'])
        tests = [Test(starting_values={'A': 65, 'B': 8921},
                      factors={'A': 16807, 'B': 48271},
                      multiples={'A': 4, 'B': 8},
                      expected=309)]

        for test in tests:
            result = count_matches(test.starting_values, test.factors,
                trials=5_000_000, multiples=test.multiples)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
