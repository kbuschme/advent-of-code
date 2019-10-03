import unittest
from collections import namedtuple
from day_5 import number_of_instruction_steps
from day_5 import number_of_instruction_steps_strange

class TestNumberOfInstructionSteps(unittest.TestCase):
    """Test number of steps required to escape the instruction loop."""

    def test_number_of_instruction_steps(self):
        Test = namedtuple('Test', ['instructions', 'expected'])
        tests = [Test(instructions=[0, 3, 0, 1, -3], expected=5),
                 Test(instructions=[2, 0, 1], expected=2)]

        for test in tests:
            result = number_of_instruction_steps(test.instructions)
            self.assertEqual(result, test.expected)

    def test_number_of_instruction_steps_variant(self):
        Test = namedtuple('Test', ['instructions', 'expected'])
        tests = [Test(instructions=[0, 3, 0, 1, -3], expected=10),]

        for test in tests:
            result = number_of_instruction_steps_strange(test.instructions)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
