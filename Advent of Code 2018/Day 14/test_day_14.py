import unittest
from collections import namedtuple
from day_14 import create_n_recipes, create_recipes_until_score_sequence

class TestChocolateRecipe(unittest.TestCase):
    """Test the creation of chocolate recipes"""
    def test_create_recipes(self):
        Test = namedtuple('Test', ['n_recipes', 'expected'])
        tests = [
            Test(n_recipes=9, expected=[5,1,5,8,9,1,6,7,7,9]),
            Test(n_recipes=5, expected=[0,1,2,4,5,1,5,8,9,1]),
            Test(n_recipes=18, expected=[9,2,5,1,0,7,1,0,8,5]),
            Test(n_recipes=2018, expected=[5,9,4,1,4,2,9,8,8,2])
        ]
        for test in tests:
            result = create_n_recipes(test.n_recipes)
            self.assertEqual(result, test.expected)

    def test_create_recipes_until_score_sequence(self):
        Test = namedtuple('Test', ['score_sequence', 'expected'])
        tests = [
            Test(score_sequence=[5,1,5,8,9], expected=9),
            Test(score_sequence=[0,1,2,4,5], expected=5),
            Test(score_sequence=[9,2,5,1,0], expected=18),
            Test(score_sequence=[5,9,4,1,4], expected=2018)
        ]
        for test in tests:
            result = create_recipes_until_score_sequence(test.score_sequence)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
