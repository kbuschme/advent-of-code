import unittest
from collections import namedtuple
from day_8 import generate_all_trees, sum_metadata_entries, find_node_value

class TestLisenceFile(unittest.TestCase):
    """Test the navigation system's license file."""

    def test_sum_metadata_entries(self):
        Test = namedtuple('Test', ['license', 'expected'])
        tests = [
            Test(license=[2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2],
                 expected=138)]

        for test in tests:
            tree = generate_all_trees(test.license)
            result = sum_metadata_entries(tree)
            self.assertEqual(result, test.expected)

    def test_find_root_node_value(self):
        Test = namedtuple('Test', ['license', 'expected'])
        tests = [
            Test(license=[2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2],
                 expected=66)]

        for test in tests:
            tree = generate_all_trees(test.license)
            result = find_node_value(tree)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
