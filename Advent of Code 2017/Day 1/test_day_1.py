import unittest
from collections import namedtuple
from day_1 import inverse_captcha_next_digit, inverse_captcha_half_through

class TestInverseCaptcha(unittest.TestCase):
    """Test inverse captcha."""

    def test_inverse_captcha_next_digit(self):
        Test = namedtuple('Test', ['sequence', 'expected'])
        tests = [Test(sequence='1122', expected=3),
                 Test(sequence='1111', expected=4),
                 Test(sequence='1234', expected=0),
                 Test(sequence='91212129', expected=9)]

        for test in tests:
            result = inverse_captcha_next_digit(test.sequence)
            self.assertEqual(result, test.expected)

    def test_inverse_captcha_half_through(self):
        Test = namedtuple('Test', ['sequence', 'expected'])
        tests = [Test(sequence='1212', expected=6),
                 Test(sequence='1221', expected=0),
                 Test(sequence='123425', expected=4),
                 Test(sequence='123123', expected=12),
                 Test(sequence='12131415', expected=4)]

        for test in tests:
            result = inverse_captcha_half_through(test.sequence)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
