from sys import path as sys_path
from os.path import abspath
sys_path.append(abspath('../Day 10'))
from day_10 import full_knot_hash
from collections import Counter

"""
Advent of Code 2017

https://adventofcode.com/2017/day/14

--- Day 14: Disk Defragmentation ---

Suddenly, a scheduled job activates the system's disk defragmenter. Were the
situation different, you might sit and watch it for a while, but today, you
just don't have that kind of time. It's soaking up valuable system resources
that are needed elsewhere, and so the only option is to help it finish its
task as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid is
either free or used. On this disk, the state of the grid is tracked by the
bits in a sequence of knot hashes.

A total of 128 knot hashes are calculated, each corresponding to a single row
in the grid; each hash contains 128 bits which correspond to individual grid
squares. Each bit of a hash indicates whether that square is free (0) or used
(1).

The hash inputs are a key string (your puzzle input), a dash, and a number
from 0 to 127 corresponding to the row. For example, if your key string were
flqrgnkx, then the first row would be given by the bits of the knot hash of
flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and
so on until the last row, flqrgnkx-127.

The output of a knot hash is traditionally represented by 32 hexadecimal
digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128
bits. To convert to bits, turn each hexadecimal digit to its equivalent binary
value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f
becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal
would begin with 10100000110000100000000101110000... in binary.

Continuing this process, the first 8 rows and columns for key flqrgnkx appear
as follows, using # to denote used squares, and . to denote free ones:

##.#.#..-->
.#.#.#.#
....#.#.
#.#.##.#
.##.#...
##..#..#
.#...#..
##.#.##.-->
|      |
V      V

In this example, 8108 squares are used across the entire 128x128 grid.

Given your actual key string, how many squares are used?

Your puzzle input is vbqugkhl.

Your puzzle answer was 8148.


--- Part Two ---

Now, all the defragmenter needs to know is the number of regions. A region is
a group of used squares that are all adjacent, not including diagonals. Every
used square is in exactly one region: lone used squares form their own
isolated regions, while several adjacent squares all count as a single region.

In the example above, the following nine regions are visible, each marked
with a distinct digit:

11.2.3..-->
.1.2.3.4
....5.6.
7.8.55.9
.88.5...
88..5..8
.8...8..
88.8.88.-->
|      |
V      V

Of particular interest is the region marked 8; while it does not appear
contiguous in this small view, all of the squares marked 8 are connected when
considering the whole 128x128 grid. In total, in this example, 1242 regions
are present.

How many regions are present given your key string?

Your puzzle input is still vbqugkhl.
"""

def calculate_regions(key, verbose=False):
    disk = []
    for row_n in range(128):
        knot_hash = full_knot_hash("{key}-{row_n}".format(key=key, row_n=row_n))
        binary_hash = ''
        for char in knot_hash:
            binary_hash = binary_hash + format(int(char, base=16), '04b')
        disk.append(list(binary_hash.replace('0', '.').replace('1', '#')))


    region_count = 0
    for i in range(128):
        for j in range(128):
            if disk[i][j] == '#':
                region_count = region_count + 1
                disk[i][j] = str(region_count)
                mark_neighbours(disk, i, j, str(region_count))

    if verbose:
        for row in disk:
            print(row)

    return region_count


def mark_neighbours(disk, i, j, mark, free='.', used='#', max_i=128, max_j=128):
    neighbours = []
    if (i-1) >= 0:
        neighbours.append((i-1, j))
    if (i+1) < 128:
        neighbours.append((i+1, j))
    if (j-1) >= 0:
        neighbours.append((i, j-1))
    if (j+1) < 128:
        neighbours.append((i, j+1))

    for i, j in neighbours:
        if disk[i][j] == used:
            disk[i][j] = mark
            mark_neighbours(disk, i, j, mark)


def calculate_used_squares(key):
    disk = ''
    for row in range(128):
        knot_hash = full_knot_hash("{key}-{row}".format(key=key, row=row))
        for char in knot_hash:
            disk = disk + format(int(char, base=16), '04b')
    return Counter(disk)['1']

def main():
    puzzle_input = 'vbqugkhl'
    print("Used squares:", calculate_used_squares(puzzle_input))
    print("Regions:", calculate_regions(puzzle_input))

if __name__ == '__main__':
    main()
