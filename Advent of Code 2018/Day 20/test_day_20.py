import unittest
from collections import namedtuple
from day_20 import min_doors_to_furthest_room

class TestRegularMap(unittest.TestCase):
    """Test Regular Map"""

    def test_min_number_of_doors(self):
        Test = namedtuple('Test', ['directions', 'expected'])
        tests = [
            Test(directions="^WNE$",
                 expected=3),
            Test(directions="^ENWWW(NEEE|SSE(EE|N))$",
                 expected=10),
            Test(directions="^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$",
                 expected=18),
            Test(directions=
                "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$",
                 expected=23),
            Test(directions=
                "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$",
                 expected=31)
        ]

        for test in tests:
            result = min_doors_to_furthest_room(test.directions)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
