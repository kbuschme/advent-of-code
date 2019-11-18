import unittest
from collections import namedtuple
from day_16 import Sample, find_samples_with_n_plus_opcodes


class TestOpcodeExecution(unittest.TestCase):
    """Test the execution of the instructions."""

    def test_find_samples_with_n_plus_opcodes(self):
        Test = namedtuple('Test', ['input', 'expected'])
        tests = [Test(input=[Sample(before=[3, 2, 1, 1],
                                    instruction=[9, 2, 1, 2],
                                    after=[3, 2, 2, 1])],
                      expected=1)]

        for test in tests:
            result = find_samples_with_n_plus_opcodes(test.input)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
