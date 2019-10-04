import unittest
from collections import namedtuple
from day_8 import find_largest_register_value, find_largest_register_value_ever

class TestRegisterInstructions(unittest.TestCase):
    """Test Register Instructions."""

    def test_find_largest_register_value(self):
        Test = namedtuple('Test', ['instructions', 'expected'])
        tests = [
            Test(instructions=[
                'b inc 5 if a > 1',
                'a inc 1 if b < 5',
                'c dec -10 if a >= 1',
                'c inc -20 if c == 10'],
            expected=1)]

        for test in tests:
            result = find_largest_register_value(test.instructions)
            self.assertEqual(result, test.expected)

    def test_find_largest_register_value_ever(self):
        Test = namedtuple('Test', ['instructions', 'expected'])
        tests = [
            Test(instructions=[
                'b inc 5 if a > 1',
                'a inc 1 if b < 5',
                'c dec -10 if a >= 1',
                'c inc -20 if c == 10'],
            expected=10)]

        for test in tests:
            result = find_largest_register_value_ever(test.instructions)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
