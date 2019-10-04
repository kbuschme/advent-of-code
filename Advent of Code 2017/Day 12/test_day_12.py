import unittest
from collections import namedtuple
from day_12 import count_group_members, count_groups

class TestGroupMembers(unittest.TestCase):
    """Test group members."""

    def test_count_group_members(self):
        Test = namedtuple('Test', ['pipe_list', 'expected'])
        tests = [
            Test(pipe_list=["0 <-> 2",
                            "1 <-> 1",
                            "2 <-> 0, 3, 4",
                            "3 <-> 2, 4",
                            "4 <-> 2, 3, 6",
                            "5 <-> 6",
                            "6 <-> 4, 5"],
                expected={0, 2, 3, 4, 5, 6})]

        for test in tests:
            result = count_group_members(test.pipe_list)
            self.assertEqual(result, test.expected)

    def test_count_groups(self):
        Test = namedtuple('Test', ['pipe_list', 'expected'])
        tests = [
            Test(pipe_list=["0 <-> 2",
                            "1 <-> 1",
                            "2 <-> 0, 3, 4",
                            "3 <-> 2, 4",
                            "4 <-> 2, 3, 6",
                            "5 <-> 6",
                            "6 <-> 4, 5"],
                expected=2)]

        for test in tests:
            result = count_groups(test.pipe_list)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
