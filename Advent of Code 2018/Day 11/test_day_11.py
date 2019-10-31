import unittest
from collections import namedtuple
import numpy as np
from day_11 import calc_power_level, generate_grid
from day_11 import calculate_summed_area_table
from day_11 import find_max_power, find_max_power_any_square_size

class TestFuelCell(unittest.TestCase):
    """Test fuel cells."""

    def test_calc_power_level(self):
        Test = namedtuple('Test', ['serial_number', 'coordinates', 'expected'])
        tests = [Test(coordinates=(3, 5), serial_number=8, expected=4)]

        for test in tests:
            result = calc_power_level(test.coordinates, test.serial_number)
            self.assertEqual(result, test.expected)

    def test_generate_grid(self):
        Test = namedtuple('Test', [
            'serial_number',
            'x_start', 'y_start', 'x_stop', 'y_stop',
            'expected'])
        tests = [
            Test(serial_number=18,
                 x_start=32, y_start=44, x_stop=37, y_stop=49,
                 expected=np.array([[-2, -4,  4,  4,  4],
                                    [-4,  4,  4,  4, -5],
                                    [ 4,  3,  3,  4, -4],
                                    [ 1,  1,  2,  4, -3],
                                    [-1,  0,  2, -5, -2]])),
            Test(serial_number=42,
                 x_start=20, y_start=60, x_stop=25, y_stop=65,
                 expected=np.array([[-3,  4,  2,  2,  2],
                                    [-4,  4,  3,  3,  4],
                                    [-5,  3,  3,  4, -4],
                                    [ 4,  3,  3,  4, -3],
                                    [ 3,  3,  3, -5, -1]]))
        ]
        for test in tests:
            grid = generate_grid(test.serial_number)
            result = grid[test.y_start:test.y_stop, test.x_start:test.x_stop]
            np.testing.assert_array_equal(result, test.expected)

    def test_calculate_summed_area_table(self):
        Test = namedtuple('Test', ['grid', 'expected'])
        tests = [
            Test(grid=np.array([[31,  2,  4, 33,  5, 36],
                                [12, 26,  9, 10, 29, 25],
                                [13, 17, 21, 22, 20, 18],
                                [24, 23, 15, 16, 14, 19],
                                [30,  8, 28, 27, 11,  7],
                                [ 1, 35, 34,  3, 32,  6]]),
                 expected=np.array([[ 31,  33,  37,  70,  75, 111],
                                    [ 43,  71,  84, 127, 161, 222],
                                    [ 56, 101, 135, 200, 254, 333],
                                    [ 80, 148, 197, 278, 346, 444],
                                    [110, 186, 263, 371, 450, 555],
                                    [111, 222, 333, 444, 555, 666]]))
        ]
        for test in tests:
            result = calculate_summed_area_table(test.grid)
            np.testing.assert_array_equal(result, test.expected)

    def test_find_max_power(self):
        Test = namedtuple('Test', ['serial_number', 'expected'])
        tests = [
            Test(serial_number=42, expected=((21, 61), 30.0)),
            Test(serial_number=18, expected=((33, 45), 29.0))
        ]
        for test in tests:
            result = find_max_power(test.serial_number)
            self.assertEqual(result, test.expected)

    def test_find_max_power_any_square_size(self):
        Test = namedtuple('Test', ['serial_number', 'expected'])
        tests = [
            Test(serial_number=18, expected=((90, 269), 16)),
            Test(serial_number=42, expected=((232, 251), 12))
        ]
        for test in tests:
            result = find_max_power_any_square_size(test.serial_number)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
