from timeit import default_timer as timer
import numpy as np
"""
Advent of Code 2018

https://adventofcode.com/2018/day/11

--- Day 11: Chronal Charge ---

You watch the Elves and their sleigh fade into the distance as they head
toward the North Pole.

Actually, you're the one fading. The falling sensation returns.

The low fuel warning light is illuminated on your wrist-mounted device.
Tapping it once causes it to project a hologram of the situation: a 300x300
grid of fuel cells and their current power levels, some negative. You're not
sure what negative power means in the context of time travel, but it can't
be good.

Each fuel cell has a coordinate ranging from 1 to 300 in both the X
(horizontal) and Y (vertical) direction. In X,Y notation, the top-left cell
is 1,1, and the top-right cell is 300,1.

The interface lets you select any 3x3 square of fuel cells. To increase your
chances of getting to your destination, you decide to choose the 3x3 square
with the largest total power.

The power level in a given fuel cell can be found through the following process:

  * Find the fuel cell's rack ID, which is its X coordinate plus 10.
  * Begin with a power level of the rack ID times the Y coordinate.
  * Increase the power level by the value of the grid serial number (your
    puzzle input).
  * Set the power level to itself multiplied by the rack ID.
  * Keep only the hundreds digit of the power level (so 12345 becomes 3;
    numbers with no hundreds digit become 0).
  * Subtract 5 from the power level.

For example, to find the power level of the fuel cell at 3,5 in a grid with
serial number 8:

  * The rack ID is 3 + 10 = 13.
  * The power level starts at 13 * 5 = 65.
  * Adding the serial number produces 65 + 8 = 73.
  * Multiplying by the rack ID produces 73 * 13 = 949.
  * The hundreds digit of 949 is 9.
  * Subtracting 5 produces 9 - 5 = 4.

So, the power level of this fuel cell is 4.

Here are some more example power levels:

  * Fuel cell at  122,79, grid serial number 57: power level -5.
  * Fuel cell at 217,196, grid serial number 39: power level  0.
  * Fuel cell at 101,153, grid serial number 71: power level  4.

Your goal is to find the 3x3 square which has the largest total power.
The square must be entirely within the 300x300 grid. Identify this square
using the X,Y coordinate of its top-left fuel cell. For example:

For grid serial number 18, the largest total 3x3 square has a top-left
corner of 33,45 (with a total power of 29); these fuel cells appear
in the middle of this 5x5 region:

-2  -4   4   4   4
-4   4   4   4  -5
 4   3   3   4  -4
 1   1   2   4  -3
-1   0   2  -5  -2

For grid serial number 42, the largest 3x3 square's top-left is 21,61 (with a
total power of 30); they are in the middle of this region:

-3   4   2   2   2
-4   4   3   3   4
-5   3   3   4  -4
 4   3   3   4  -3
 3   3   3  -5  -1

What is the X,Y coordinate of the top-left fuel cell of the 3x3 square with
the largest total power?

Your puzzle input is 2866.

Your puzzle answer was 20,50.


--- Part Two ---

You discover a dial on the side of the device; it seems to let you select a
square of any size, not just 3x3. Sizes from 1x1 to 300x300 are supported.

Realizing this, you now must find the square of any size with the largest total
power. Identify this square by including its size as a third parameter after
the top-left coordinate: a 9x9 square with a top-left corner of 3,5 is
identified as 3,5,9.

For example:

  * For grid serial number 18, the largest total square (with a total power
    of 113) is 16x16 and has a top-left corner of 90,269, so its identifier
    is 90,269,16.
  * For grid serial number 42, the largest total square (with a total power
    of 119) is 12x12 and has a top-left corner of 232,251, so its identifier
    is 232,251,12.

What is the X,Y,size identifier of the square with the largest total power?

Your puzzle answer was 238,278,9.
"""

def calc_power_level(coordinates, serial_number):
    x, y = coordinates
    rack_id = x + 10
    power_level = (rack_id * y + serial_number) * rack_id
    power_level = (power_level // 100) % 10
    power_level = power_level - 5
    return power_level

def generate_grid(serial_number, grid_size=300):
    grid = np.zeros((grid_size, grid_size))
    for y in range(grid_size):
        for x in range(grid_size):
            grid[y, x] = calc_power_level((x, y), serial_number)
    return grid

def find_max_power_naive(serial_number, square_size=3, grid_size=300,
                         grid=None):
    if grid is None:
        grid = generate_grid(serial_number, grid_size=grid_size)
    max_power_level = None
    for x in range(0, grid_size-square_size+1):
        for y in range(0, grid_size-square_size+1):
            square_power_level = np.sum(grid[y:y+square_size, x:x+square_size])
            if (max_power_level is None or
                    square_power_level > max_power_level[1]):
                max_power_level = ((x, y), square_power_level)
    return max_power_level

def calculate_summed_area_table(grid):
    # See Summed-area table: https://en.wikipedia.org/wiki/Summed-area_table
    x_max, y_max = grid.shape
    table = np.zeros(grid.shape)
    for y in range(y_max):
        for x in range(x_max):
            if y == 0 and x == 0:
                table[y,x] = grid[y,x]
            elif y == 0 and x != 0:
                table[y,x] = grid[y,x]+table[y,x-1]
            elif y != 0 and x == 0:
                table[y,x] = grid[y,x]+table[y-1,x]
            else:
                table[y,x] = grid[y,x]+table[y,x-1]+table[y-1,x]-table[y-1,x-1]
    return table

def find_max_power(serial_number, square_size=3, grid_size=300,
                   grid=None, table=None):
    if grid is None:
        grid = generate_grid(serial_number, grid_size=grid_size)
    if table is None:
        table = calculate_summed_area_table(grid)
    max_power_level = None
    # Note: x, y refer to the bottom right corner of the square
    for x in range(square_size-1, grid_size):
        for y in range(square_size-1, grid_size):
            square_power_level = table[y, x]
            if x > square_size-1:
                square_power_level -= table[y, x-square_size]
            if y > square_size-1:
                square_power_level -= table[y-square_size, x]
            if x > square_size-1 and y > square_size-1:
                square_power_level += table[y-square_size, x-square_size]

            if (max_power_level is None or
                    square_power_level > max_power_level[1]):
                # Return top-left corner
                max_power_level = ((x-square_size+1, y-square_size+1),
                                   square_power_level)
    return max_power_level

def find_max_power_any_square_size(serial_number, grid_size=300, naive=False):
    power_levels = {}
    grid = generate_grid(serial_number, grid_size=grid_size)
    table = calculate_summed_area_table(grid)
    for square_size in range(1, grid_size+1):
        if naive:
            power_levels[square_size] = find_max_power_naive(
                serial_number, square_size=square_size, grid=grid)
        else:
            power_levels[square_size] = find_max_power(
                serial_number, square_size=square_size, grid=grid, table=table)
    max_power_level = max(power_levels.items(), key=lambda level: level[1][1])
    square_size, ((x, y), power_level) = max_power_level
    return (x, y), square_size

def main():
    serial_number = 2866

    print("--- Solution using a summed-area table ---")
    start = timer()
    max_square, power = find_max_power(serial_number)
    end = timer()
    print(f"3x3 square with maximum total power: {max_square}, {power}")
    print(f"Time elapsed: {end - start}s")

    start = timer()
    max_square, power = find_max_power_any_square_size(serial_number)
    end = timer()
    print(f"nxn square with maximum total power: {max_square}, {power}")
    print(f"Time elapsed: {end - start}s")

    print("\n--- Naive solution ---")
    start = timer()
    max_square, power = find_max_power_naive(serial_number)
    end = timer()
    print(f"3x3 square with maximum total power: {max_square}, {power}")
    print(f"Time elapsed: {end - start}s")

    start = timer()
    max_square, power = find_max_power_any_square_size(
        serial_number, naive=True)
    end = timer()
    print(f"nxn square with maximum total power: {max_square}, {power}")
    print(f"Time elapsed: {end - start}s")

if __name__ == '__main__':
    main()
