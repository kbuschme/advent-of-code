import unittest
from collections import namedtuple
from day_3 import parse_claims
from day_3 import find_overlapping_square_inches, find_not_overlapping_claim

class TestFabricClaims(unittest.TestCase):
    """Test claims on the special fabric."""

    def test_prase_claims(self):
        Test = namedtuple('Test', ['claims_as_strings', 'expected'])
        Claim = namedtuple('Claim', ['id', 'pos', 'size'])
        tests = [Test(claims_as_strings=["#1 @ 1,3: 4x4",
                                         "#2 @ 3,1: 4x4",
                                         "#3 @ 5,5: 2x2"],
                      expected=[Claim(id=1, pos=(1, 3), size=(4, 4)),
                                Claim(id=2, pos=(3, 1), size=(4, 4)),
                                Claim(id=3, pos=(5, 5), size=(2, 2))])]

        for test in tests:
            result = parse_claims(test.claims_as_strings)
            self.assertEqual(result, test.expected)

    def test_find_overlapping_square_inches(self):
        Test = namedtuple('Test', ['claims', 'expected'])
        tests = [
            Test(expected=4,
                 claims=["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"])]

        for test in tests:
            result = find_overlapping_square_inches(test.claims)
            self.assertEqual(result, test.expected)

    def test_find_not_overlapping_claim(self):
        Test = namedtuple('Test', ['claims', 'expected'])
        tests = [
            Test(expected=3,
                 claims=["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"])]

        for test in tests:
            result = find_not_overlapping_claim(test.claims)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
