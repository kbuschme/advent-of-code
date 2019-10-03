import numpy as np

"""
Advent of Code 2017

https://adventofcode.com/2017/day/3

--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite
two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a
location marked 1 and then counting up while spiraling outward. For example,
the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data
must be carried back to square 1 (the location of the only access port for
this memory system) by programs that can only move up, down, left, or right.
They always take the shortest path: the Manhattan Distance between the
location of the data and square 1.

For example:

  * Data from square 1 is carried 0 steps, since it's at the access port.
  * Data from square 12 is carried 3 steps, such as: down, left, left.
  * Data from square 23 is carried only 2 steps: up twice.
  * Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in
your puzzle input all the way to the access port?

Your puzzle answer was 475.


--- Part Two ---

As a stress test on the system, the programs here clear the grid and then
store the value 1 in square 1. Then, in the same allocation order as shown
above, they store the sum of the values in all adjacent squares, including
diagonals.

So, the first few squares' values are chosen as follows:

  * Square 1 starts with the value 1.
  * Square 2 has only one adjacent filled square (with value 1), so it
    also stores 1.
  * Square 3 has both of the above squares as neighbors and stores the sum
    of their values, 2.
  * Square 4 has all three of the aforementioned squares as neighbors and
    stores the sum of their values, 4.
  * Square 5 only has the first and fourth squares as neighbors, so it gets
    the value 5.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?

Your puzzle answer was 279138.
"""

def distance_from_spiral_origin(identified_square, verbose=False):
    """Calculate the Manhattan distance from the identified square
    to the origin."""
    spiral_edge_size = 1

    # 1. Inward steps
    inward_steps = 0
    maximum_position = spiral_edge_size**2
    while maximum_position < identified_square:
        spiral_edge_size = spiral_edge_size + 2
        inward_steps = inward_steps + 1
        maximum_position = spiral_edge_size**2

    if verbose:
        print("Inward steps:", inward_steps)
        print("Maximum position:", maximum_position)

    # 2. Side steps
    # maximum_position is in the lower right corner, which needs
    # inward_steps steps to go inside
    # maximum - before_maximum / 4

    if identified_square == 1:
        side_steps = 0
    else:
        side_steps = inward_steps - 1

    position = (spiral_edge_size - 2)**2 + 1
    if verbose:
        print("Position", position)
    decrease = True
    while position < identified_square:
        position = position + 1
        if decrease:
            side_steps = side_steps - 1
        else:
            side_steps = side_steps + 1

        if side_steps == 0:
            decrease = False
        elif side_steps == inward_steps:
            decrease = True

    if verbose:
        print("Side steps:", side_steps)

    steps = inward_steps + side_steps
    return steps


def find_sum_of_spiral_neighbours_larger_than(limit, verbose=False):
    """
    Find the sum of neighbours in the spiral which is larger than limit.

    Note:
      * Hack: requires specification of spiral width to create a large enough
        NumPy array. Here set to 15.
      * x and y are switched since they do not correspond to NumPy's rows
        and cols. The resulting spiral is thus rotated.
    """
    spiral_width = 15
    spiral = np.zeros((spiral_width, spiral_width))

    # Set origin to 1
    x, y = spiral_width//2, spiral_width//2
    spiral[x, y] = 1
    x_increase, y_increase = True, True
    x_step_max, y_step_max = 1, 1
    x_step_counter, y_step_counter = 0, 0
    x_direction = False

    # Fill Spiral, set starting position
    for i in range(2, (spiral_width-2)**2+1):
        if verbose:
            print(spiral)
        if x_direction:
            if x_increase:
                x = x + 1
            else:
                x = x - 1
            x_step_counter = x_step_counter + 1
            if x_step_counter == x_step_max:
                x_step_max = x_step_max + 1
                x_step_counter = 0
                x_increase = not x_increase
                x_direction = not x_direction
        else:
            if y_increase:
                y = y + 1
            else:
                y = y - 1
            y_step_counter = y_step_counter + 1
            if y_step_counter == y_step_max:
                y_step_max = y_step_max + 1
                y_step_counter = 0
                y_increase = not y_increase
                x_direction = not x_direction

        neighbor_sum = sum([spiral[x, y-1], spiral[x, y+1],
                            spiral[x-1, y], spiral[x+1, y],
                            spiral[x-1, y-1], spiral[x-1, y+1],
                            spiral[x+1, y-1], spiral[x+1, y+1]])
        spiral[x, y] = neighbor_sum

        if neighbor_sum > limit:
            return int(spiral[x,y])

def main():
    identified_square = 277678
    limit = identified_square
    print(f"Steps to origin: {distance_from_spiral_origin(identified_square)}")
    print(f"Sum of neighbours larger than {limit}:",
          find_sum_of_spiral_neighbours_larger_than(limit))

if __name__ == '__main__':
    main()
