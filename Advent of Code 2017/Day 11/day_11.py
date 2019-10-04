"""
Advent of Code 2017

https://adventofcode.com/2017/day/11

--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when
a program comes up to you, clearly in distress. "It's my child process," she
says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can
be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you need
to determine the fewest number of steps required to reach him. (A "step"
means to move from the hex you are in to any adjacent hex.)

For example:

  * ne,ne,ne is 3 steps away.
  * ne,ne,sw,sw is 0 steps away (back where you started).
  * ne,ne,s,s is 2 steps away (se,se).
  * se,sw,se,sw,sw is 3 steps away (s,s,sw).

Your puzzle answer was 698.


--- Part Two ---

How many steps away is the furthest he ever got from his starting position?

Although it hasn't changed, you can still get your puzzle input.

Your puzzle answer was 1435.
"""

def cancel_out_steps(direction, opposite_direction):
    if direction > opposite_direction:
        direction = direction - opposite_direction
        opposite_direction = 0
    elif direction < opposite_direction:
        opposite_direction = opposite_direction - direction
        direction = 0
    else:
        direction = 0
        opposite_direction = 0

    return direction, opposite_direction

def merge_two_steps(direction_1, direction_2, merged_direction):
    if direction_1 > direction_2:
        merged_direction = merged_direction + direction_2
        direction_1 = direction_1 - direction_2
        direction_2 = 0
    elif direction_1 < direction_2:
        merged_direction = merged_direction + direction_1
        direction_2 = direction_2 - direction_1
        direction_1 = 0
    else:
        merged_direction = merged_direction + direction_2
        direction_1 = 0
        direction_2 = 0

    return direction_1, direction_2, merged_direction

def caluclate_distance(path):
    hexes = len(path)

    north_steps = sum([1 for step in path if step == 'n'])
    north_east_steps = sum([1 for step in path if step == 'ne'])
    north_west_steps = sum([1 for step in path if step == 'nw'])
    south_steps = sum([1 for step in path if step == 's'])
    south_east_steps = sum([1 for step in path if step == 'se'])
    south_west_steps = sum([1 for step in path if step == 'sw'])

    total = 0
    new_total = -1
    while not new_total == total:
        total = new_total

        # Replace
        north_steps, south_steps = cancel_out_steps(north_steps, south_steps)
        north_west_steps, south_east_steps = cancel_out_steps(
            north_west_steps, south_east_steps)
        north_east_steps, south_west_steps = cancel_out_steps(
            north_east_steps, south_west_steps)

        # Merge
        north_east_steps, south_steps, south_east_steps = merge_two_steps(
            north_east_steps, south_steps, south_east_steps)
        south_east_steps, north_steps, north_east_steps = merge_two_steps(
            south_east_steps, north_steps, north_east_steps)
        north_west_steps, south_steps, south_west_steps = merge_two_steps(
            north_west_steps, south_steps, south_west_steps)
        south_west_steps, north_steps, north_west_steps = merge_two_steps(
            south_west_steps, north_steps, north_west_steps)
        north_east_steps, north_west_steps, north_steps = merge_two_steps(
            north_east_steps, north_west_steps, north_steps)
        south_east_steps, south_west_steps, south_steps = merge_two_steps(
            south_east_steps, south_west_steps, south_steps)

        new_total = sum([north_steps,
                         north_east_steps,
                         north_west_steps,
                         south_steps,
                         south_east_steps,
                         south_west_steps,])
    return total

def farthest_distance(path):
    return max([caluclate_distance(path[:i+1]) for i in range(len(path))])

def main():
    filename = 'day_11_path.txt'
    with open(filename, 'r') as path_file:
        path = path_file.read().strip().split(',')
    print("Shortest distance:", caluclate_distance(path))
    print("Farthest distance:", farthest_distance(path))

if __name__ == '__main__':
    main()
