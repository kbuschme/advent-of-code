from itertools import combinations
import numpy as np
"""
Advent of Code 2018

https://adventofcode.com/2018/day/10

--- Day 10: The Stars Align ---

It's no use; your navigation system simply isn't capable of providing walking
directions in the arctic circle, and certainly not in 1018.

The Elves suggest an alternative. In times like these, North Pole rescue
operations will arrange points of light in the sky to guide missing Elves back
to base. Unfortunately, the message is easy to miss: the points move slowly
enough that it takes hours to align them, but have so much momentum that they
only stay aligned for a second. If you blink at the wrong time, it might be
hours before another message appears.

You can see these points of light floating in the distance, and record their
position in the sky and their velocity, the relative change in position per
second (your puzzle input). The coordinates are all given from your
perspective; given enough time, those positions and velocities will move the
points into a cohesive message!

Rather than wait, you decide to fast-forward the process and calculate what
the points will eventually spell.

For example, suppose you note the following points:

position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>

Each line represents one point. Positions are given as <X, Y> pairs:
X represents how far left (negative) or right (positive) the point appears,
while Y represents how far up (negative) or down (positive) the point appears.

At 0 seconds, each point has the position given. Each second, each point's
velocity is added to its position. So, a point with velocity <1, -2> is moving
to the right, but is moving upward twice as quickly. If this point's initial
position were <3, 9>, after 3 seconds, its position would become <6, 3>.

Over time, the points listed above would move like this:

Initially:
........#.............
................#.....
.........#.#..#.......
......................
#..........#.#.......#
...............#......
....#.................
..#.#....#............
.......#..............
......#...............
...#...#.#...#........
....#..#..#.........#.
.......#..............
...........#..#.......
#...........#.........
...#.......#..........

After 1 second:
......................
......................
..........#....#......
........#.....#.......
..#.........#......#..
......................
......#...............
....##.........#......
......#.#.............
.....##.##..#.........
........#.#...........
........#...#.....#...
..#...........#.......
....#.....#.#.........
......................
......................

After 2 seconds:
......................
......................
......................
..............#.......
....#..#...####..#....
......................
........#....#........
......#.#.............
.......#...#..........
.......#..#..#.#......
....#....#.#..........
.....#...#...##.#.....
........#.............
......................
......................
......................

After 3 seconds:
......................
......................
......................
......................
......#...#..###......
......#...#...#.......
......#...#...#.......
......#####...#.......
......#...#...#.......
......#...#...#.......
......#...#...#.......
......#...#..###......
......................
......................
......................
......................

After 4 seconds:
......................
......................
......................
............#.........
........##...#.#......
......#.....#..#......
.....#..##.##.#.......
.......##.#....#......
...........#....#.....
..............#.......
....#......#...#......
.....#.....##.........
...............#......
...............#......
......................
......................

After 3 seconds, the message appeared briefly: HI. Of course, your message will
be much longer and will take many more seconds to appear.

What message will eventually appear in the sky?

Your puzzle answer was HRPHBRKG.


--- Part Two ---

Good thing you didn't have to wait, because that would have taken a long time -
much longer than the 3 seconds in the example above.

Impressed by your sub-hour communication capabilities, the Elves are curious:
exactly how many seconds would they have needed to wait for that message to
appear?

Your puzzle answer was 10355.
"""

def move(stars):
    stars[:,:2] = stars[:,:2] + stars[:,2:]
    return stars

def total_distances(stars):
    total = 0
    for i, j in combinations(range(len(stars)), 2):
        total = total + sum(abs(stars[i][0] - stars[j][0]))
    return total

def min_max_distance(stars, verbose=False):
    total = 0
    x_min = min(stars[:,0])
    x_max = max(stars[:,0])
    y_min = min(stars[:,1])
    y_max = max(stars[:,1])
    if verbose:
        print(x_min, x_max, abs(x_min - x_max))
        print(y_min, y_max, abs(y_min - y_max))
    return abs(x_min - x_max) + abs(y_min - y_max)

def align_stars(stars, verbose=False):
    seconds = 10
    prev_distance = None
    current_distance = None
    iteration = 0
    while prev_distance is None or current_distance < prev_distance:
        iteration = iteration + 1
        if current_distance is not None:
            prev_distance = current_distance

        stars = move(stars)
        current_distance = min_max_distance(stars)

        if verbose and iteration % 1000 == 0:
            print(f"Iteration: {iteration} {current_distance}")

    # Reverse last iteration
    stars[:,:2] = stars[:,:2] - stars[:,2:]
    iteration = iteration - 1

    return stars, iteration

def format_message(stars, verbose=False):
    x_min = min(stars[:,0])
    y_min = min(stars[:,1])
    stars[:,0] = stars[:,0] - x_min
    stars[:,1] = stars[:,1] - y_min
    n_cols = max(stars[:,0]) + 1
    n_rows = max(stars[:,1]) + 1
    if verbose:
        print(f"Grid: {n_rows}x{n_cols}")
    grid = [[" " for _ in range(n_cols)] for _ in range(n_rows)]

    for col, row, _, _ in stars:
        grid[row][col] = "*"

    return "\n".join(["".join(row) for row in grid])

def parse_star_config(star_configs):
    stars = []
    for star_config in star_configs:
        pos, vel = star_config[10:-1].split("> velocity=<")
        x, y = pos.split(",")
        x_vel, y_vel = vel.split(",")
        stars.append([
            int(x.strip()),
            int(y.strip()),
            int(x_vel.strip()),
            int(y_vel.strip())])
    stars = np.array(stars)
    return stars

def main():
    stars = []
    star_configs = []
    with open('day_10_stars.txt', 'r') as stars_file:
        star_configs = stars_file.read().splitlines()
    stars = parse_star_config(star_configs)

    stars, seconds = align_stars(stars)
    print("Message:", format_message(stars), sep="\n")
    print(f"Seconds before message appears: {seconds}")

if __name__ == '__main__':
    main()
