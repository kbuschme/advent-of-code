import unittest
from collections import namedtuple
from day_4 import find_most_minutes_most_frequent_minute
from day_4 import find_most_frequent_minute

class TestSleepiestMinute(unittest.TestCase):
    """Test functions finding the minutes guards sleep most frequently."""

    def test_find_most_minutes_most_frequent_minute(self):
        Test = namedtuple('Test', ['guard_logs', 'expected'])
        tests = [Test(expected=240, guard_logs=[
            "[1518-11-01 00:00] Guard #10 begins shift",
            "[1518-11-01 00:05] falls asleep",
            "[1518-11-01 00:25] wakes up",
            "[1518-11-01 00:30] falls asleep",
            "[1518-11-01 00:55] wakes up",
            "[1518-11-01 23:58] Guard #99 begins shift",
            "[1518-11-02 00:40] falls asleep",
            "[1518-11-02 00:50] wakes up",
            "[1518-11-03 00:05] Guard #10 begins shift",
            "[1518-11-03 00:24] falls asleep",
            "[1518-11-03 00:29] wakes up",
            "[1518-11-04 00:02] Guard #99 begins shift",
            "[1518-11-04 00:36] falls asleep",
            "[1518-11-04 00:46] wakes up",
            "[1518-11-05 00:03] Guard #99 begins shift",
            "[1518-11-05 00:45] falls asleep",
            "[1518-11-05 00:55] wakes up"])]

        for test in tests:
            result = find_most_minutes_most_frequent_minute(test.guard_logs)
            self.assertEqual(result, test.expected)

    def test_find_most_frequent_minute(self):
        Test = namedtuple('Test', ['guard_logs', 'expected'])
        tests = [Test(expected=4455, guard_logs=[
            "[1518-11-01 00:00] Guard #10 begins shift",
            "[1518-11-01 00:05] falls asleep",
            "[1518-11-01 00:25] wakes up",
            "[1518-11-01 00:30] falls asleep",
            "[1518-11-01 00:55] wakes up",
            "[1518-11-01 23:58] Guard #99 begins shift",
            "[1518-11-02 00:40] falls asleep",
            "[1518-11-02 00:50] wakes up",
            "[1518-11-03 00:05] Guard #10 begins shift",
            "[1518-11-03 00:24] falls asleep",
            "[1518-11-03 00:29] wakes up",
            "[1518-11-04 00:02] Guard #99 begins shift",
            "[1518-11-04 00:36] falls asleep",
            "[1518-11-04 00:46] wakes up",
            "[1518-11-05 00:03] Guard #99 begins shift",
            "[1518-11-05 00:45] falls asleep",
            "[1518-11-05 00:55] wakes up"])]

        for test in tests:
            result = find_most_frequent_minute(test.guard_logs)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
