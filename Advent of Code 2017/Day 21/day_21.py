import numpy as np

"""
Advent of Code 2017

https://adventofcode.com/2017/day/21

--- Day 21: Fractal Art ---

You find a program trying to generate some art. It uses a strange process that
involves repeatedly enhancing the detail of an image through a set of rules.

The image consists of a two-dimensional square grid of pixels that are either
on (#) or off (.). The program always begins with this pattern:

.#.
..#
###

Because the pattern is both 3 pixels wide and 3 pixels tall, it is said
to have a size of 3.

Then, the program repeats the following process:

  * If the size is evenly divisible by 2, break the pixels up into 2x2 squares,
    and convert each 2x2 square into a 3x3 square by following the
    corresponding enhancement rule.
  * Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3
    squares, and convert each 3x3 square into a 4x4 square by following the
    corresponding enhancement rule.

Because each square of pixels is replaced by a larger one, the image gains
pixels and so its size increases.

The artist's book of enhancement rules is nearby (your puzzle input); however,
it seems to be missing rules. The artist explains that sometimes, one must
rotate or flip the input pattern to find a match. (Never rotate or flip the
output pattern, though.) Each pattern is written concisely: rows are listed
as single units, ordered top-down, and separated by slashes. For example,
the following rules correspond to the adjacent patterns:

../.#  =  ..
          .#

                .#.
.#./..#/###  =  ..#
                ###

                        #..#
#..#/..../#..#/.##.  =  ....
                        #..#
                        .##.

When searching for a rule to use, rotate and flip the pattern as necessary.
For example, all of the following patterns match the same rule:

.#.   .#.   #..   ###
..#   #..   #.#   ..#
###   ###   ##.   .#.

Suppose the book contained the following two rules:

../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#

As before, the program begins with this pattern:

.#.
..#
###

The size of the grid (3) is not divisible by 2, but it is divisible by 3.
It divides evenly into a single square; the square matches the second rule,
which produces:

#..#
....
....
#..#

The size of this enhanced grid (4) is evenly divisible by 2, so that rule
is used. It divides evenly into four squares:

#.|.#
..|..
--+--
..|..
#.|.#

Each of these squares matches the same rule (../.# => ##./#../...), three of
which require some flipping and rotation to line up with the rule. The output
for the rule is the same in all four cases:

##.|##.
#..|#..
...|...
---+---
##.|##.
#..|#..
...|...

Finally, the squares are joined into a new grid:

##.##.
#..#..
......
##.##.
#..#..
......

Thus, after 2 iterations, the grid contains 12 pixels that are on.

How many pixels stay on after 5 iterations?

Your puzzle answer was 123.


--- Part Two ---

How many pixels stay on after 18 iterations?

Your puzzle answer was 1984683.
"""

def grid_to_pattern(grid):
    pattern = ["".join(["#" if col == 1 else "." for col in row])
               for row in grid]
    return "/".join(pattern)

def pattern_to_grid(pattern):
    pattern = pattern.split("/")
    starting_grid_dims = (len(pattern), len(pattern[0]))
    grid = np.zeros(starting_grid_dims)
    for row_i, row in enumerate(pattern):
        for col_i, col in enumerate(row):
            if col == "#":
                grid[row_i, col_i] = 1
    return grid

def parse_rules(rules, verbose=False):
    """Parse the rules from the rulebook."""
    parsed_rules = []
    for rule in rules:
        pattern, result = rule.split(" => ")
        parsed_rules.append((pattern_to_grid(pattern),
                             pattern_to_grid(result)))
    extended_rules = extend_rules(parsed_rules)
    if verbose:
        print(f"Rules (extended): {len(extended_rules)}")
    return extended_rules

def extend_rules(rules):
    rules = set([(grid_to_pattern(pattern), grid_to_pattern(result))
             for pattern, result in rules])
    new_rules = True
    while new_rules:
        n_rules = len(rules)
        additional_rules = set()
        for pattern, result in list(rules):
            pattern_rot_90 = grid_to_pattern(np.rot90(pattern_to_grid(pattern)))
            pattern_rot_180 = grid_to_pattern(np.rot90(
                pattern_to_grid(pattern), k=2))
            pattern_rot_270 = grid_to_pattern(np.rot90(
                pattern_to_grid(pattern), k=3))
            pattern_flip_lr = grid_to_pattern(np.fliplr(
                pattern_to_grid(pattern)))
            pattern_flip_ud = grid_to_pattern(np.flipud(
                pattern_to_grid(pattern)))
            rules.add((pattern_rot_90, result))
            rules.add((pattern_rot_180, result))
            rules.add((pattern_rot_270, result))
            rules.add((pattern_flip_lr, result))
            rules.add((pattern_flip_ud, result))
        if len(rules) == n_rules:
            new_rules = False
    return {pattern: pattern_to_grid(result)
            for pattern, result in rules}

def count_pixels(rules, iterations=5, verbose=False):
    """Count the number of 'on' pixels after iterations"""
    starting_pattern = """.#./..#/###"""
    grid = pattern_to_grid(starting_pattern)
    rules = parse_rules(rules)

    for i in range(iterations):
        if verbose:
            print(f"Iteration: {i}")
        grid = enhance_grid(grid, rules)
    return len([char for char in grid_to_pattern(grid) if char == "#"])

def apply_rule(grid, rules):
    for pattern, result in rules:
        if grid_to_pattern(pattern) == grid_to_pattern(grid):
            return result

def enhance_grid(grid, rules, verbose=False):
    """Enhance the grid according to the rules."""
    if len(grid) % 2 == 0:
        divider = 2
    else:
        divider = 3

    if verbose:
        print(f"Divider: {divider}")
        print(f"Grid:\n{grid}")

    splits = len(grid) // divider
    enhanced_grid_dims = ((divider+1)*splits, (divider+1)*splits)
    enhanced_grid = np.zeros(enhanced_grid_dims)
    if verbose:
        print("Subgrids:")
    for i, k in zip(range(0, len(grid), divider),
                 range(0, len(enhanced_grid), divider+1)):
        for j, l in zip(range(0, len(grid), divider),
                        range(0, len(enhanced_grid), divider+1)):
            subgrid = grid[i:i+divider, j:j+divider]
            if verbose:
                print(subgrid)
            enhanced_grid[k:k+divider+1, l:l+divider+1] = rules[
                grid_to_pattern(subgrid)]
    if verbose:
        print(f"Enhanced:\n{enhanced_grid}")

    return enhanced_grid

def main():
    rules = []
    with open("day_21_rules.txt", 'r') as rules_file:
        rules = rules_file.read().splitlines()
    print(f"Rules: {len(rules)}")

    iterations = 5
    print(f"Pixel 'on' after {iterations} iterations:",
          f"{count_pixels(rules, iterations=iterations)}")

    iterations = 18
    print(f"Pixel 'on' after {iterations} iterations:",
          f"{count_pixels(rules, iterations=iterations)}")

if __name__ == '__main__':
    main()
