import unittest
from collections import namedtuple
from day_23 import coprocessor_instructions_in_python
from day_23 import coprocessor_instructions_in_python_optimised_step_1
from day_23 import coprocessor_instructions_in_python_optimised_step_2

class CoprocessorInstructions(unittest.TestCase):
    """Test coprocessor instructions in python."""

    def test_count_newly_infected_nodes(self):
        Test = namedtuple('Test', ['registers', 'expected'])
        tests = [
            Test(expected=6241, registers={
                'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0
            })]

        for test in tests:
            _, mul_counter = coprocessor_instructions_in_python(test.registers)
            self.assertEqual(mul_counter, test.expected)

    def test_coprocessor_instructions_in_python_optimised_step_1(self):
        Test = namedtuple('Test', ['registers', 'expected'])
        tests = [
            Test(expected=6241, registers={
                'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0
            })]

        for test in tests:
            _, mul_counter = coprocessor_instructions_in_python_optimised_step_1(test.registers)
            self.assertEqual(mul_counter, test.expected)

    def test_coprocessor_instructions_in_python_optimised_step_2(self):
        Test = namedtuple('Test', ['registers', 'expected'])
        tests = [
            Test(expected=6241, registers={
                'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0
            })]

        for test in tests:
            _, mul_counter = coprocessor_instructions_in_python_optimised_step_2(test.registers)
            self.assertEqual(mul_counter, test.expected)

if __name__ == '__main__':
    unittest.main()
