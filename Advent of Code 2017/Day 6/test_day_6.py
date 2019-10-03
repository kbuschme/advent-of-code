import unittest
from collections import namedtuple
from day_6 import redistribution_cycles, redistribution_cycle_length

class TestReallocation(unittest.TestCase):
    """Test memory reallocation."""

    def test_redistribution_cycles(self):
        Test = namedtuple('Test', ['memory_bank', 'expected'])
        tests = [Test(memory_bank=[0, 2, 7, 0], expected=5),]

        for test in tests:
            result = redistribution_cycles(test.memory_bank)
            self.assertEqual(result, test.expected)

    def test_redistribution_cycle_length(self):
        Test = namedtuple('Test', ['memory_bank', 'expected'])
        tests = [Test(memory_bank=[2, 4, 1, 2], expected=4),]

        for test in tests:
            result = redistribution_cycle_length(test.memory_bank)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
