import unittest
from collections import namedtuple

from day_12 import parse_rules, generate_state_from_string
from day_12 import sum_of_pot_indices

class TestPlants(unittest.TestCase):
    """Test growth of plants in pots."""

    def test_sum_of_pot_indices(self):
        Test = namedtuple('Test', ['initial_state', 'rules', 'expected'])
        tests = [
            Test(initial_state="#..#.#..##......###...###",
                 rules=["...## => #",
                        "..#.. => #",
                        ".#... => #",
                        ".#.#. => #",
                        ".#.## => #",
                        ".##.. => #",
                        ".#### => #",
                        "#.#.# => #",
                        "#.### => #",
                        "##.#. => #",
                        "##.## => #",
                        "###.. => #",
                        "###.# => #",
                        "####. => #"],
                 expected=325)
        ]
        for test in tests:
            initial_state = generate_state_from_string(test.initial_state)
            rules = parse_rules(test.rules)
            result = sum_of_pot_indices(initial_state, rules)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
