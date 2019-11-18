"""
Advent of Code 2018

https://adventofcode.com/2018/day/17

--- Day 17: Reservoir Research ---

You arrive in the year 18. If it weren't for the coat you got in 1018, you
would be very cold: the North Pole base hasn't even been constructed.

Rather, it hasn't been constructed yet. The Elves are making a little progress,
but there's not a lot of liquid water in this climate, so they're getting
very dehydrated. Maybe there's more underground?

You scan a two-dimensional vertical slice of the ground nearby and discover
that it is mostly sand with veins of clay. The scan only provides data with
a granularity of square meters, but it should be good enough to determine how
much water is trapped there. In the scan, x represents the distance to the
right, and y represents the distance down. There is also a spring of water
near the surface at x=500, y=0. The scan identifies which square meters are
clay (your puzzle input).

For example, suppose your scan shows the following veins of clay:

x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504

Rendering clay as #, sand as ., and the water spring as +, and with x
increasing to the right and y increasing downward, this becomes:

   44444455555555
   99999900000000
   45678901234567
 0 ......+.......
 1 ............#.
 2 .#..#.......#.
 3 .#..#..#......
 4 .#..#..#......
 5 .#.....#......
 6 .#.....#......
 7 .#######......
 8 ..............
 9 ..............
10 ....#.....#...
11 ....#.....#...
12 ....#.....#...
13 ....#######...

The spring of water will produce water forever. Water can move through sand,
but is blocked by clay. Water always moves down when possible, and spreads to
the left and right otherwise, filling space that has clay on both sides and
falling out otherwise.

For example, if five squares of water are created, they will flow downward
until they reach the clay and settle there. Water that has come to rest is
shown here as ~, while sand through which water has passed (but which is now
dry again) is shown as |:

......+.......
......|.....#.
.#..#.|.....#.
.#..#.|#......
.#..#.|#......
.#....|#......
.#~~~~~#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######...

Two squares of water can't occupy the same location. If another five squares
of water are created, they will settle on the first five, filling the clay
reservoir a little more:

......+.......
......|.....#.
.#..#.|.....#.
.#..#.|#......
.#..#.|#......
.#~~~~~#......
.#~~~~~#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######...

Water pressure does not apply in this scenario. If another four squares of
water are created, they will stay on the right side of the barrier, and no
water will reach the left side:

......+.......
......|.....#.
.#..#.|.....#.
.#..#~~#......
.#..#~~#......
.#~~~~~#......
.#~~~~~#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######...

At this point, the top reservoir overflows. While water can reach the tiles
above the surface of the water, it cannot settle there, and so the next five
squares of water settle like this:

......+.......
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
........|.....
....#...|.#...
....#...|.#...
....#~~~~~#...
....#######...

Note especially the leftmost |: the new squares of water can reach this tile,
but cannot stop there. Instead, eventually, they all fall to the right and
settle in the reservoir below.

After 10 more squares of water, the bottom reservoir is also full:

......+.......
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
........|.....
....#~~~~~#...
....#~~~~~#...
....#~~~~~#...
....#######...

Finally, while there is nowhere left for the water to settle, it can reach a
few more tiles before overflowing beyond the bottom of the scanned data:

......+.......    (line not counted: above minimum y value)
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
...|||||||||..
...|#~~~~~#|..
...|#~~~~~#|..
...|#~~~~~#|..
...|#######|..
...|.......|..    (line not counted: below maximum y value)
...|.......|..    (line not counted: below maximum y value)
...|.......|..    (line not counted: below maximum y value)

How many tiles can be reached by the water? To prevent counting forever,
ignore tiles with a y coordinate smaller than the smallest y coordinate in
your scan data or larger than the largest one. Any x coordinate is valid.
In this example, the lowest y coordinate given is 1, and the highest is 13,
causing the water spring (in row 0) and the water falling off the bottom of
the render (in rows 14 through infinity) to be ignored.

So, in the example above, counting both water at rest (~) and other sand tiles
the water can hypothetically reach (|), the total number of tiles the water
can reach is 57.

How many tiles can the water reach within the range of y values in your scan?

Your puzzle answer was 35707.

--- Part Two ---

After a very long time, the water spring will run dry. How much water will
be retained?

In the example above, water that won't eventually drain out is shown as ~,
a total of 29 tiles.

How many water tiles are left after the water spring stops producing water
and all remaining water not at rest has drained?

Your puzzle answer was 29293.
"""
def clay_from_scan(scan):
    clay = []
    for each in scan:
        coordinate_1, coordinate_2 = each.split(", ")
        if coordinate_1[0] == 'y':
            coordinate_1, coordinate_2 = coordinate_2, coordinate_1

        x = coordinate_1.split("=")[1]
        if ".." in x:
            x_start, x_end = [int(each) for each in x.split("..")]
        else:
            x_start, x_end = int(x), int(x)

        y = coordinate_2.split("=")[1]
        if ".." in y:
            y_start, y_end = [int(each) for each in y.split("..")]
        else:
            y_start, y_end = int(y), int(y)

        for x in range(x_start, x_end+1):
            for y in range(y_start, y_end+1):
                clay.append((x, y))
    return clay

def print_ground(clay, spring, wet_sand, water, verbose=False):
    clay = set(clay)
    wet_sand = set(wet_sand)
    water = set(water)
    x_min, x_max = min([x for x, _ in clay]), max([x for x, _ in clay])
    y_min, y_max = min([y for _, y in clay]), max([y for _, y in clay])

    if verbose:
        print(x_min, x_max, y_min, y_max)
        for each in clay:
            print(each)
        print(f"Spring: {spring}")

    for y in range(0, y_max+1):
        row = []
        for x in range(x_min, x_max+1):
            if (x, y) == spring:
                row.append("+")
            elif (x, y) in clay:
                row.append("#")
            elif (x, y) in wet_sand:
                row.append("|")
            elif (x, y) in water:
                row.append("~")
            else:
                row.append(".")
        print("".join(row))

def flow_left(x, y, clay, wet_sand, water, verbose=False):
    closed = True
    new_wet_sand = set()
    while (x-1, y) not in clay and (x-1, y) not in water and closed:
        new_wet_sand.add((x-1, y))
        if (x-1, y+1) not in clay and (x-1, y+1) not in water:
            closed = False
        x = x - 1
    if verbose:
        print(f"Flow Left: {new_wet_sand}")
    return closed, new_wet_sand

def flow_right(x, y, clay, wet_sand, water, verbose=False):
    closed = True
    new_wet_sand = set()
    while (x+1, y) not in clay and (x+1, y) not in water and closed:
        new_wet_sand.add((x+1, y))
        if (x+1, y+1) not in clay and (x+1, y+1) not in water:
            closed = False
        x = x + 1
    if verbose:
        print(f"Flow right: {new_wet_sand}")
    return closed, new_wet_sand

def wet_tiles(scan, spring=(500, 0), verbose=False):
    def dry_sand(x, y):
        return ((x, y) not in wet_sand
            and (x, y) not in clay
            and (x, y) not in water)

    def clay_or_water(x, y):
        return (x, y) in clay or (x, y) in water

    clay = set(clay_from_scan(scan))
    y_min_clay = min(clay, key=lambda c: c[1])[1]
    y_max_clay = max(clay, key=lambda c: c[1])[1]

    water_vein_tips = {spring}
    wet_sand = {spring}
    water = set()

    while len(water_vein_tips) != 0:
        x, y = water_vein_tips.pop()

        if dry_sand(x, y+1):
            wet_sand.add((x, y+1))
            water_vein_tips.add((x, y+1))
        elif clay_or_water(x, y+1):
            closed_left, wet_sand_left = flow_left(
                x, y, clay, wet_sand, water)
            closed_right, wet_sand_right = flow_right(
                x, y, clay, wet_sand, water)
            if closed_left and closed_right:
                water.update(wet_sand_left)
                water.update(wet_sand_right)
                water.add((x, y))
                wet_sand.remove((x, y))
                wet_sand.add((x, y-1))
                water_vein_tips.add((x, y-1))
            else:
                wet_sand.update(wet_sand_left)
                wet_sand.update(wet_sand_right)
                if not closed_left:
                    leftmost_wet_sand = min(wet_sand_left,
                                            key=lambda c: c[0])
                    water_vein_tips.add(leftmost_wet_sand)
                if not closed_right:
                    rightmost_wet_sand = max(wet_sand_right,
                                             key=lambda c: c[0])
                    water_vein_tips.add(rightmost_wet_sand)

        # Remove tiles that are lower than the lowest clay tile
        water_vein_tips = {(x,y) for (x,y) in water_vein_tips
                                 if y < y_max_clay}

    if verbose:
        print_ground(clay, spring, wet_sand, water)

    water_and_wet_sand = {(x,y) for (x, y) in wet_sand.union(water)
                                if y >= y_min_clay}
    return len(water_and_wet_sand), len(water)

def main():
    filename = 'day_17_scan.txt'
    with open(filename, 'r') as scan_file:
        scan = scan_file.read().splitlines()
    spring = (500, 0)
    tiles, water = wet_tiles(scan)
    print(f"Number of wet tiles: {tiles}")
    print(f"Number of water tiles: {water}")

if __name__ == '__main__':
    main()
