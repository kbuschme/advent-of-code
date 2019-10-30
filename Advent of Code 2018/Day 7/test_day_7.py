import unittest
from collections import namedtuple
from day_7 import order_steps, assemble_sleigh

class TestSleighAssembly(unittest.TestCase):
    """Test functions to assemble Santa's sleigh."""

    def test_order_steps(self):
        Test = namedtuple('Test', ['steps', 'expected'])
        tests = [Test(expected="CABDFE", steps=[
            "Step C must be finished before step A can begin.",
            "Step C must be finished before step F can begin.",
            "Step A must be finished before step B can begin.",
            "Step A must be finished before step D can begin.",
            "Step B must be finished before step E can begin.",
            "Step D must be finished before step E can begin.",
            "Step F must be finished before step E can begin."])]

        for test in tests:
            result = order_steps(test.steps)
            self.assertEqual(result, test.expected)

    def test_assemble_sleigh(self):
        Test = namedtuple('Test',
                          ['steps', 'n_workers', 'default_time', 'expected'])
        tests = [Test(expected=15, n_workers=2, default_time=0, steps=[
            "Step C must be finished before step A can begin.",
            "Step C must be finished before step F can begin.",
            "Step A must be finished before step B can begin.",
            "Step A must be finished before step D can begin.",
            "Step B must be finished before step E can begin.",
            "Step D must be finished before step E can begin.",
            "Step F must be finished before step E can begin."])]

        for test in tests:
            result = assemble_sleigh(test.steps, n_workers=test.n_workers,
                                     default_time=test.default_time)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
