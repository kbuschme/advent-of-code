import unittest
from collections import namedtuple
from day_19 import parse_program
from day_19 import execute_program, execute_translated_program
from day_19 import main_loop, main_loop_pythonic, main_loop_optimised

class TestFlowControl(unittest.TestCase):
    """Test Flow Control."""

    def test_execute_program(self):
        Test = namedtuple('Test', ['program', 'expected'])
        tests = [Test(
            program=[
                "#ip 0",
                "seti 5 0 1",
                "seti 6 0 2",
                "addi 0 1 0",
                "addr 1 2 3",
                "setr 1 0 0",
                "seti 8 0 4",
                "seti 9 0 5"],
            expected=[
                ("ip=0", [0, 0, 0, 0, 0, 0], "seti 5 0 1", [0, 5, 0, 0, 0, 0]),
                ("ip=1", [1, 5, 0, 0, 0, 0], "seti 6 0 2", [1, 5, 6, 0, 0, 0]),
                ("ip=2", [2, 5, 6, 0, 0, 0], "addi 0 1 0", [3, 5, 6, 0, 0, 0]),
                ("ip=4", [4, 5, 6, 0, 0, 0], "setr 1 0 0", [5, 5, 6, 0, 0, 0]),
                ("ip=6", [6, 5, 6, 0, 0, 0], "seti 9 0 5", [6, 5, 6, 0, 0, 9])]
        )]
        for test in tests:
            program, ip_register = parse_program(test.program)
            result = execute_program(program, ip_register, verbose=True)
            self.assertEqual(result, test.expected)

    def test_execute_translated_program(self):
        Test = namedtuple('Test', ['registers', 'main_loop_fun', 'expected'])
        tests = [
            Test(registers=[0, 0, 0, 0, 0, 0],
                main_loop_fun=main_loop,
                expected=[1848, 860, 861, 861, 257, 1]),
            Test(registers=[0, 0, 0, 0, 0, 0],
                main_loop_fun=main_loop_pythonic,
                expected=[1848, 860, 861, 861, 257, 1]),
            Test(registers=[0, 0, 0, 0, 0, 0],
                main_loop_fun=main_loop_optimised,
                expected=[1848, 860, 861, 861, 257, 1])
        ]
        for test in tests:
            result = execute_translated_program(test.registers,
                main_loop_fun=test.main_loop_fun)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
