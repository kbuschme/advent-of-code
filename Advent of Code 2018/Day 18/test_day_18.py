import unittest
from collections import namedtuple
from day_18 import change_area, count_resource_value

class TestConstructionProject(unittest.TestCase):
    """Test Construction Project."""

    def test_change_area(self):
        Test = namedtuple('Test', ['start_area', 'expected'])
        tests = [Test(
            start_area=[
                list(".#.#...|#."),
                list(".....#|##|"),
                list(".|..|...#."),
                list("..|#.....#"),
                list("#.#|||#|#|"),
                list("...#.||..."),
                list(".|....|..."),
                list("||...#|.#|"),
                list("|.||||..|."),
                list("...#.|..|.")],
            expected=[
                list(".......##."),
                list("......|###"),
                list(".|..|...#."),
                list("..|#||...#"),
                list("..##||.|#|"),
                list("...#||||.."),
                list("||...|||.."),
                list("|||||.||.|"),
                list("||||||||||"),
                list("....||..|.")])
        ]
        for test in tests:
            result = change_area(test.start_area)
            self.assertEqual(result, test.expected)

    def test_count_resource_value(self):
        Test = namedtuple('Test', ['start_area', 'minutes', 'expected'])
        tests = [Test(
            start_area=[
                list(".#.#...|#."),
                list(".....#|##|"),
                list(".|..|...#."),
                list("..|#.....#"),
                list("#.#|||#|#|"),
                list("...#.||..."),
                list(".|....|..."),
                list("||...#|.#|"),
                list("|.||||..|."),
                list("...#.|..|.")],
            minutes=10,

            expected=1147)
        ]
        for test in tests:
            result = count_resource_value(test.start_area)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
