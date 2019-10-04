import unittest
from collections import namedtuple
from day_13 import calculate_severity, calculate_delay

class TestFirewall(unittest.TestCase):
    """Test firewall."""

    def test_calculate_severity(self):
        Test = namedtuple('Test', ['firewall', 'expected'])
        tests = [Test(firewall={0: 3, 1: 2, 4: 4, 6: 4}, expected=24)]

        for test in tests:
            result = calculate_severity(test.firewall)
            self.assertEqual(result, test.expected)

    def test_calculate_delay(self):
        Test = namedtuple('Test', ['firewall', 'expected'])
        tests = [Test(firewall={0: 3, 1: 2, 4: 4, 6: 4}, expected=10)]

        for test in tests:
            result = calculate_delay(test.firewall)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
