import unittest
from collections import namedtuple
from day_25 import small_turing_machine

class TestTuringMachine(unittest.TestCase):
    """Test Turing Machine."""

    def test_small_turing_machine(self):
        Test = namedtuple('Test', ['max_steps', 'expected'])
        tests = [Test(max_steps=6, expected=3)]

        for test in tests:
            result = small_turing_machine(max_steps=test.max_steps)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
