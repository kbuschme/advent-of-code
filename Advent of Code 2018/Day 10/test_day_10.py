import unittest
from collections import namedtuple
from day_10 import parse_star_config, align_stars, format_message

class TestStarAlignment(unittest.TestCase):
    """Test alignment of the stars."""

    def test_align_stars_message(self):
        Test = namedtuple('Test', ['stars', 'expected'])
        tests = [Test(
            stars=['position=< 9,  1> velocity=< 0,  2>',
                   'position=< 7,  0> velocity=<-1,  0>',
                   'position=< 3, -2> velocity=<-1,  1>',
                   'position=< 6, 10> velocity=<-2, -1>',
                   'position=< 2, -4> velocity=< 2,  2>',
                   'position=<-6, 10> velocity=< 2, -2>',
                   'position=< 1,  8> velocity=< 1, -1>',
                   'position=< 1,  7> velocity=< 1,  0>',
                   'position=<-3, 11> velocity=< 1, -2>',
                   'position=< 7,  6> velocity=<-1, -1>',
                   'position=<-2,  3> velocity=< 1,  0>',
                   'position=<-4,  3> velocity=< 2,  0>',
                   'position=<10, -3> velocity=<-1,  1>',
                   'position=< 5, 11> velocity=< 1, -2>',
                   'position=< 4,  7> velocity=< 0, -1>',
                   'position=< 8, -2> velocity=< 0,  1>',
                   'position=<15,  0> velocity=<-2,  0>',
                   'position=< 1,  6> velocity=< 1,  0>',
                   'position=< 8,  9> velocity=< 0, -1>',
                   'position=< 3,  3> velocity=<-1,  1>',
                   'position=< 0,  5> velocity=< 0, -1>',
                   'position=<-2,  2> velocity=< 2,  0>',
                   'position=< 5, -2> velocity=< 1,  2>',
                   'position=< 1,  4> velocity=< 2,  1>',
                   'position=<-2,  7> velocity=< 2, -2>',
                   'position=< 3,  6> velocity=<-1, -1>',
                   'position=< 5,  0> velocity=< 1,  0>',
                   'position=<-6,  0> velocity=< 2,  0>',
                   'position=< 5,  9> velocity=< 1, -2>',
                   'position=<14,  7> velocity=<-2,  0>',
                   'position=<-3,  6> velocity=< 2, -1>'],
            expected="\n".join(['*   *  ***',
                                '*   *   * ',
                                '*   *   * ',
                                '*****   * ',
                                '*   *   * ',
                                '*   *   * ',
                                '*   *   * ',
                                '*   *  ***']))]

        for test in tests:
            stars, seconds = align_stars(parse_star_config(test.stars))
            result = format_message(stars)
            self.assertEqual(result, test.expected)

    def test_align_stars_time(self):
        Test = namedtuple('Test', ['stars', 'expected'])
        tests = [Test(
            stars=['position=< 9,  1> velocity=< 0,  2>',
                   'position=< 7,  0> velocity=<-1,  0>',
                   'position=< 3, -2> velocity=<-1,  1>',
                   'position=< 6, 10> velocity=<-2, -1>',
                   'position=< 2, -4> velocity=< 2,  2>',
                   'position=<-6, 10> velocity=< 2, -2>',
                   'position=< 1,  8> velocity=< 1, -1>',
                   'position=< 1,  7> velocity=< 1,  0>',
                   'position=<-3, 11> velocity=< 1, -2>',
                   'position=< 7,  6> velocity=<-1, -1>',
                   'position=<-2,  3> velocity=< 1,  0>',
                   'position=<-4,  3> velocity=< 2,  0>',
                   'position=<10, -3> velocity=<-1,  1>',
                   'position=< 5, 11> velocity=< 1, -2>',
                   'position=< 4,  7> velocity=< 0, -1>',
                   'position=< 8, -2> velocity=< 0,  1>',
                   'position=<15,  0> velocity=<-2,  0>',
                   'position=< 1,  6> velocity=< 1,  0>',
                   'position=< 8,  9> velocity=< 0, -1>',
                   'position=< 3,  3> velocity=<-1,  1>',
                   'position=< 0,  5> velocity=< 0, -1>',
                   'position=<-2,  2> velocity=< 2,  0>',
                   'position=< 5, -2> velocity=< 1,  2>',
                   'position=< 1,  4> velocity=< 2,  1>',
                   'position=<-2,  7> velocity=< 2, -2>',
                   'position=< 3,  6> velocity=<-1, -1>',
                   'position=< 5,  0> velocity=< 1,  0>',
                   'position=<-6,  0> velocity=< 2,  0>',
                   'position=< 5,  9> velocity=< 1, -2>',
                   'position=<14,  7> velocity=<-2,  0>',
                   'position=<-3,  6> velocity=< 2, -1>'],
            expected=3)]

        for test in tests:
            stars, seconds = align_stars(parse_star_config(test.stars))
            result = seconds
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
