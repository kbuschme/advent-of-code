import unittest
from collections import namedtuple
from day_10 import knot_hash, full_knot_hash, make_dense_hash

class TestKnotHash(unittest.TestCase):
    """Test knot hash."""

    def test_knot_hash(self):
        Test = namedtuple('Test', ['circle', 'lengths', 'expected'])
        tests = [Test(circle=[0, 1, 2, 3, 4],
                      lengths=[3, 4, 1, 5],
                      expected=[3, 4, 2, 1, 0])]

        for test in tests:
            result, _, _ = knot_hash(test.circle, test.lengths)
            self.assertEqual(result, test.expected)

    def test_full_knot_hash(self):
        Test = namedtuple('Test', ['sequence', 'expected'])
        tests = [
            Test(sequence="",
                 expected="a2582a3a0e66e6e86e3812dcb672a272"),
            Test(sequence="AoC 2017",
                 expected="33efeb34ea91902bb2f59c9920caa6cd"),
            Test(sequence="1,2,3",
                 expected="3efbe78a8d82f29979031a4aa0b16a9d"),
            Test(sequence="1,2,4",
                 expected="63960835bcdc130f0b66d7ff4f6a5a8e"),]

        for test in tests:
            result = full_knot_hash(test.sequence)
            self.assertEqual(result, test.expected)

    def test_make_dense_hash(self):
        Test = namedtuple('Test', ['block', 'expected'])
        tests = [
            Test(block=[65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22],
                 expected=64)]

        for test in tests:
            result = make_dense_hash(test.block)[0]
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
