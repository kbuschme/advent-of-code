import unittest
from collections import namedtuple
from day_22 import parse_status_map, count_newly_infected_nodes
from day_22 import count_newly_infected_nodes_modified

class TestVirusActivity(unittest.TestCase):
    """Test virus activity."""

    def test_count_newly_infected_nodes(self):
        Test = namedtuple('Test', ['status', 'steps', 'expected'])
        tests = [
            Test(steps=7, expected=5, status=["..#", "#..", "..."]),
            Test(steps=70, expected=41, status=["..#", "#..", "..."]),
            Test(steps=10_000, expected=5_587, status=["..#", "#..", "..."])]

        for test in tests:
            result = count_newly_infected_nodes(test.status, steps=test.steps)
            self.assertEqual(result, test.expected)

    def test_count_newly_infected_nodes_modified(self):
        Test = namedtuple('Test', ['status', 'steps', 'expected'])
        tests = [
            Test(steps=100, expected=26,
                 status=["..#", "#..", "..."]),
            Test(steps=10_000_000, expected=2511944,
                 status=["..#", "#..", "..."])]

        for test in tests:
            result = count_newly_infected_nodes_modified(
                test.status, steps=test.steps)
            self.assertEqual(result, test.expected)

    def test_parse_status_map(self):
        Test = namedtuple('Test', ['status', 'expected'])
        tests = [
            Test(status=["..#", "#..", "..."],
                 expected=[(-1, 1), (0, -1)]),]

        for test in tests:
            result = parse_status_map(test.status)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
