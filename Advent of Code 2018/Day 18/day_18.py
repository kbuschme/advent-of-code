from collections import Counter
import numpy as np
"""
Advent of Code 2018

https://adventofcode.com/2018/day/18

--- Day 18: Settlers of The North Pole ---

On the outskirts of the North Pole base construction project, many Elves are
collecting lumber.

The lumber collection area is 50 acres by 50 acres; each acre can be either
open ground (.), trees (|), or a lumberyard (#). You take a scan of the area
(your puzzle input).

Strange magic is at work here: each minute, the landscape looks entirely
different. In exactly one minute, an open acre can fill with trees, a wooded
acre can be converted to a lumberyard, or a lumberyard can be cleared to open
ground (the lumber having been sent to other projects).

The change to each acre is based entirely on the contents of that acre as well
as the number of open, wooded, or lumberyard acres adjacent to it at the start
of each minute. Here, "adjacent" means any of the eight acres surrounding that
acre. (Acres on the edges of the lumber collection area might have fewer than
eight adjacent acres; the missing acres aren't counted.)

In particular:

  * An open acre will become filled with trees if three or more adjacent acres
    contained trees. Otherwise, nothing happens.
  * An acre filled with trees will become a lumberyard if three or more
    adjacent acres were lumberyards. Otherwise, nothing happens.
  * An acre containing a lumberyard will remain a lumberyard if it was
    adjacent to at least one other lumberyard and at least one acre containing
    trees. Otherwise, it becomes open.

These changes happen across all acres simultaneously, each of them using the
state of all acres at the beginning of the minute and changing to their new
form by the end of that same minute. Changes that happen during the minute
don't affect each other.

For example, suppose the lumber collection area is instead only 10 by 10 acres
with this initial configuration:

Initial state:
.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.

After 1 minute:
.......##.
......|###
.|..|...#.
..|#||...#
..##||.|#|
...#||||..
||...|||..
|||||.||.|
||||||||||
....||..|.

After 2 minutes:
.......#..
......|#..
.|.|||....
..##|||..#
..###|||#|
...#|||||.
|||||||||.
||||||||||
||||||||||
.|||||||||

After 3 minutes:
.......#..
....|||#..
.|.||||...
..###|||.#
...##|||#|
.||##|||||
||||||||||
||||||||||
||||||||||
||||||||||

After 4 minutes:
.....|.#..
...||||#..
.|.#||||..
..###||||#
...###||#|
|||##|||||
||||||||||
||||||||||
||||||||||
||||||||||

After 5 minutes:
....|||#..
...||||#..
.|.##||||.
..####|||#
.|.###||#|
|||###||||
||||||||||
||||||||||
||||||||||
||||||||||

After 6 minutes:
...||||#..
...||||#..
.|.###|||.
..#.##|||#
|||#.##|#|
|||###||||
||||#|||||
||||||||||
||||||||||
||||||||||

After 7 minutes:
...||||#..
..||#|##..
.|.####||.
||#..##||#
||##.##|#|
|||####|||
|||###||||
||||||||||
||||||||||
||||||||||

After 8 minutes:
..||||##..
..|#####..
|||#####|.
||#...##|#
||##..###|
||##.###||
|||####|||
||||#|||||
||||||||||
||||||||||

After 9 minutes:
..||###...
.||#####..
||##...##.
||#....###
|##....##|
||##..###|
||######||
|||###||||
||||||||||
||||||||||

After 10 minutes:
.||##.....
||###.....
||##......
|##.....##
|##.....##
|##....##|
||##.####|
||#####|||
||||#|||||
||||||||||

After 10 minutes, there are 37 wooded acres and 31 lumberyards. Multiplying
the number of wooded acres by the number of lumberyards gives the total
resource value after ten minutes: 37 * 31 = 1147.

What will the total resource value of the lumber collection area be after 10
minutes?

Your puzzle answer was 663502.

--- Part Two ---

This important natural resource will need to last for at least thousands
of years. Are the Elves collecting this lumber sustainably?

What will the total resource value of the lumber collection area be after
1000000000 minutes?

Your puzzle answer was 201341.
"""

def area_to_string(area):
    return "".join([acre for row in area for acre in row])

def change_area(area):
    open_ground, trees, lumberyard = '.', '|', '#'
    area = np.array(area)
    new_area = np.empty(area.shape, dtype=str)
    y_max, x_max = area.shape
    for y in range(y_max):
        for x in range(x_max):
            if x == 0:
                x_low, x_high = 0, x + 2
            elif x == len(area):
                x_low, x_high = x - 1, x
            else:
                x_low, x_high = x - 1, x + 2
            if y == 0:
                y_low, y_high = 0, y + 2
            elif y == len(area[0]):
                y_low, y_high = y - 1, y
            else:
                y_low, y_high = y - 1, y + 2
            centre = area[y][x]
            surrounding = area[y_low:y_high, x_low:x_high]
            surrounding = Counter(surrounding.flatten())
            surrounding[centre] -= 1 # remove centre from counter
            if centre == open_ground:
                if surrounding[trees] >= 3:
                    new_area[y,x] = trees
                else:
                    new_area[y,x] = open_ground
            elif centre == trees:
                if surrounding[lumberyard] >= 3:
                    new_area[y,x] = lumberyard
                else:
                    new_area[y,x] = trees
            elif centre == lumberyard:
                if surrounding[lumberyard] >= 1 and surrounding[trees] >= 1:
                    new_area[y,x] = lumberyard
                else:
                    new_area[y,x] = open_ground
    return new_area.tolist()

def count_resource_value(area, minutes=10):
    open_ground, trees, lumberyard = '.', '|', '#'
    area_history = [area_to_string(area)]
    for minute in range(1, minutes+1):
        area = change_area(area)
        area_as_string = area_to_string(area)
        if area_as_string not in area_history:
            area_history.append(area_as_string)
        else:
            previous = area_history.index(area_as_string)
            loop_size = minute - previous
            target_area_index = previous + ((minutes - previous) % loop_size)
            target_area = area_history[target_area_index]
            acre_count = Counter(area_to_string(target_area))
            resource_value = acre_count[trees] * acre_count[lumberyard]
            return resource_value

    acre_count = Counter(area_to_string(area))
    resource_value = acre_count[trees] * acre_count[lumberyard]
    return resource_value

def main():
    with open('day_18_landscape.txt', 'r') as area_file:
        area = area_file.read().splitlines()
        area = [list(row) for row in area]

    minutes = 10
    resource_value = count_resource_value(area, minutes=minutes)
    print(f"Resource value (wooded acres x lumberyards) after {minutes} min:",
          f"{resource_value}")

    minutes = 1_000_000_000
    resource_value = count_resource_value(area, minutes=minutes)
    print(f"Resource value (wooded acres x lumberyards) after {minutes} min:",
          f"{resource_value}")

if __name__ == '__main__':
    main()
