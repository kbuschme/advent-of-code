from collections import defaultdict

"""
Advent of Code 2017

https://adventofcode.com/2017/day/19

--- Day 19: A Series of Tubes ---

Somehow, a network packet got lost and ended up here. It's trying to follow
a routing diagram (your puzzle input), but it's confused about where to go.

Its starting point is just off the top of the diagram. Lines (drawn with
|, -, and +) show the path it needs to take, starting by going down onto
the only line connected to the top of the diagram. It needs to follow this
path until it reaches the end (located somewhere within the diagram) and
stop there.

Sometimes, the lines cross over each other; in these cases, it needs to
continue going the same direction, and only turn left or right when there's
no other option. In addition, someone has left letters on the line; these
also don't change its direction, but it can use them to keep track of where
it's been. For example:

     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+

Given this diagram, the packet needs to take the following path:

  * Starting at the only line touching the top of the diagram, it must go down,
    pass through A, and continue onward to the first +.
  * Travel right, up, and right, passing through B in the process.
  * Continue down (collecting C), right, and up (collecting D).
  * Finally, go all the way left through E and stopping at F.

Following the path to the end, the letters it sees on its path are ABCDEF.

The little packet looks up at you, hoping you can help it find the way.
What letters will it see (in the order it would see them) if it follows
the path? (The routing diagram is very wide; make sure you view it without
line wrapping.)

Your puzzle answer was PVBSCMEQHY.


--- Part Two ---

The packet is curious how many steps it needs to go.

For example, using the same routing diagram from the example above...

     |
     |  +--+
     A  |  C
 F---|--|-E---+
     |  |  |  D
     +B-+  +--+

...the packet would go:

  * 6 steps down (including the first line at the top of the diagram).
  * 3 steps right.
  * 4 steps up.
  * 3 steps right.
  * 4 steps down.
  * 3 steps right.
  * 2 steps up.
  * 13 steps left (including the F it stops on).

This would result in a total of 38 steps.

How many steps does the packet need to go?

Your puzzle answer was 17736.
"""

def find_path(tubes, verbose=False):
    """Find the path through the labyrinth.

    Inputs
    -------
    tubes: list
        List of strings containing the labyrinth.

    Returns
    -------
    collected_letters: list
        List containing the collected letters.
    """
    collected_letters = []
    steps = 0

    # Find starting position
    direction = 'south'
    position_x, position_y = 0, 0
    position_x = tubes[position_y].find("|")
    sign = tubes[position_y][position_x]

    # From starting position follow tubes
    while not sign == " ":
        if verbose:
            print(f"{position_x}, {position_y}, {direction}: {sign}")
        if sign in "|-":
            if direction == 'north':
                position_y = position_y - 1
            elif direction == 'south':
                position_y = position_y + 1
            elif direction == 'west':
                position_x = position_x - 1
            elif direction == 'east':
                position_x = position_x + 1
        elif sign == "+":
            if direction in ['north', 'south']:
                if not tubes[position_y][position_x-1] == " ":
                    position_x = position_x - 1
                    direction = 'west'
                elif not tubes[position_y][position_x+1] == " ":
                    position_x = position_x + 1
                    direction = 'east'
            elif direction in ['west', 'east']:
                if not tubes[position_y-1][position_x] == " ":
                    position_y = position_y - 1
                    direction = 'north'
                elif not tubes[position_y+1][position_x] == " ":
                    position_y = position_y + 1
                    direction = 'south'
        else:
            collected_letters.append(sign)
            if direction == 'north':
                position_y = position_y - 1
            elif direction == 'south':
                position_y = position_y + 1
            elif direction == 'west':
                position_x = position_x - 1
            elif direction == 'east':
                position_x = position_x + 1

        sign = tubes[position_y][position_x]
        steps = steps + 1

    return collected_letters, steps

def main():
    tubes = ""
    with open("day_19_tubes.txt", 'r') as tubes_file:
        tubes = tubes_file.readlines()

    letters, steps = find_path(tubes, verbose=False)
    print(f"Letters: {''.join(letters)}\nSteps: {steps}")

if __name__ == '__main__':
    main()
