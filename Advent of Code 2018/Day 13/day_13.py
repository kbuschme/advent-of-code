from collections import Counter, namedtuple
"""
Advent of Code 2018

https://adventofcode.com/2018/day/13

--- Day 13: Mine Cart Madness ---

A crop of this size requires significant logistics to transport produce, soil,
fertilizer, and so on. The Elves are very busy pushing things around in carts
on some kind of rudimentary system of tracks they've come up with.

Seeing as how cart-and-track systems don't appear in recorded history for
another 1000 years, the Elves seem to be making this up as they go along.
They haven't even figured out how to avoid collisions yet.

You map out the tracks (your puzzle input) and see where you can help.

Tracks consist of straight paths (| and -), curves (/ and \), and
intersections (+). Curves connect exactly two perpendicular pieces of track;
for example, this is a closed loop:

/----\
|    |
|    |
\----/

Intersections occur when two perpendicular paths cross. At an intersection,
a cart is capable of turning left, turning right, or continuing straight.
Here are two loops connected by two intersections:

/-----\
|     |
|  /--+--\
|  |  |  |
\--+--/  |
   |     |
   \-----/

Several carts are also on the tracks. Carts always face either up (^),
down (v), left (<), or right (>). (On your initial map, the track under each
cart is a straight path matching the direction the cart is facing.)

Each time a cart has the option to turn (by arriving at any intersection), it
turns left the first time, goes straight the second time, turns right
the third time, and then repeats those directions starting again with left
the fourth time, straight the fifth time, and so on. This process is
independent of the particular intersection at which the cart has arrived -
that is, the cart has no per-intersection memory.

Carts all move at the same speed; they take turns moving a single step at a
time. They do this based on their current location: carts on the top row move
first (acting from left to right), then carts on the second row move (again
from left to right), then carts on the third row, and so on. Once each cart
has moved one step, the process repeats; each of these loops is called a tick.

For example, suppose there are two carts on a straight track:

|  |  |  |  |
v  |  |  |  |
|  v  v  |  |
|  |  |  v  X
|  |  ^  ^  |
^  ^  |  |  |
|  |  |  |  |

First, the top cart moves. It is facing down (v), so it moves down one square.
Second, the bottom cart moves. It is facing up (^), so it moves up one square.
Because all carts have moved, the first tick ends. Then, the process repeats,
starting with the first cart. The first cart moves down, then the second cart
moves up - right into the first cart, colliding with it! (The location of
the crash is marked with an X.) This ends the second and last tick.

Here is a longer example:

/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/

/-->\
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \->--/
  \------/

/---v
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+>-/
  \------/

/---\
|   v  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+->/
  \------/

/---\
|   |  /----\
| /->--+-\  |
| | |  | |  |
\-+-/  \-+--^
  \------/

/---\
|   |  /----\
| /-+>-+-\  |
| | |  | |  ^
\-+-/  \-+--/
  \------/

/---\
|   |  /----\
| /-+->+-\  ^
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /----<
| /-+-->-\  |
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /---<\
| /-+--+>\  |
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /--<-\
| /-+--+-v  |
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /-<--\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/

/---\
|   |  /<---\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-<--/
  \------/

/---\
|   |  v----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \<+--/
  \------/

/---\
|   |  /----\
| /-+--v-\  |
| | |  | |  |
\-+-/  ^-+--/
  \------/

/---\
|   |  /----\
| /-+--+-\  |
| | |  X |  |
\-+-/  \-+--/
  \------/

After following their respective paths for a while, the carts eventually crash.
To help prevent crashes, you'd like to know the location of the first crash.
Locations are given in X,Y coordinates, where the furthest left column is X=0
and the furthest top row is Y=0:

           111
 0123456789012
0/---\
1|   |  /----\
2| /-+--+-\  |
3| | |  X |  |
4\-+-/  \-+--/
5  \------/

In this example, the location of the first crash is 7,3.

Your puzzle answer was 8,3.


--- Part Two ---

There isn't much you can do to prevent crashes in this ridiculous system.
However, by predicting the crashes, the Elves know where to be in advance and
instantly remove the two crashing carts the moment any crash occurs.

They can proceed like this for a while, but eventually, they're going to run
out of carts. It could be useful to figure out where the last cart that hasn't
crashed will end up.

For example:

/>-<\
|   |
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/

/---\
|   |
| v-+-\
| | | |
\-+-/ |
  |   |
  ^---^

/---\
|   |
| /-+-\
| v | |
\-+-/ |
  ^   ^
  \---/

/---\
|   |
| /-+-\
| | | |
\-+-/ ^
  |   |
  \---/

After four very expensive crashes, a tick ends with only one cart remaining;
its final location is 6,4.

What is the location of the last cart at the end of the first tick where it is
the only cart left?

Your puzzle answer was 73,121.
"""

def turn_left(cart):
    if cart.direction == 'north':
        return 'west'
    elif cart.direction == 'west':
        return 'south'
    elif cart.direction == 'south':
        return 'east'
    elif cart.direction == 'east':
        return 'north'

def turn_right(cart):
    if cart.direction == 'north':
        return 'east'
    elif cart.direction == 'west':
        return 'north'
    elif cart.direction == 'south':
        return 'west'
    elif cart.direction == 'east':
        return 'south'

def go_straight(cart):
    return cart.direction

def drive_until_crash(tracks, carts):
    """Move from top to bottom, left to right."""
    Cart = namedtuple('Cart', ['x', 'y', 'direction', 'n_turns'])
    directions = ['left', 'straight', 'right']
    ticks = 0
    crash = False
    while not crash:
        ticks = ticks + 1
        crash_coordinates = 0, 0
        moved_carts = []
        carts = sorted(carts, key=lambda cart: (cart.y, cart.x))
        for i, cart in enumerate(carts):
            n_turns = cart.n_turns
            new_direction = cart.direction

            if cart.direction == 'north':
                new_x, new_y = cart.x, cart.y-1
            elif cart.direction == 'east':
                new_x, new_y = cart.x+1, cart.y
            elif cart.direction == 'south':
                new_x, new_y = cart.x, cart.y+1
            elif cart.direction == 'west':
                new_x, new_y = cart.x-1, cart.y

            if tracks[new_x, new_y] == "/":
                if cart.direction == 'north':
                    new_direction = 'east'
                elif cart.direction == 'east':
                    new_direction = 'north'
                elif cart.direction == 'south':
                    new_direction = 'west'
                elif cart.direction == 'west':
                    new_direction = 'south'
            elif tracks[new_x, new_y] == "\\":
                if cart.direction == 'north':
                    new_direction = 'west'
                elif cart.direction == 'east':
                    new_direction = 'south'
                elif cart.direction == 'south':
                    new_direction = 'east'
                elif cart.direction == 'west':
                    new_direction = 'north'
            elif tracks[new_x, new_y] == "+":
                n_turns = cart.n_turns + 1
                if n_turns == 3:
                    new_direction = turn_right(cart)
                    n_turns = 0
                elif n_turns == 2:
                    new_direction = go_straight(cart)
                elif n_turns == 1:
                    new_direction = turn_left(cart)

            # Check for collision
            if (new_x, new_y) in [(each.x, each.y) for each in carts[i+1:]]:
                return new_x, new_y
            if (new_x, new_y) in [(each.x, each.y) for each in moved_carts]:
                return new_x, new_y

            moved_carts.append(Cart(x=new_x, y=new_y,
                                    direction=new_direction,
                                    n_turns=n_turns))
        carts = moved_carts

    return crash_coordinates

def drive_until_crash_remove_carts(tracks, carts):
    """Move from top to bottom, left to right."""
    Cart = namedtuple('Cart', ['x', 'y', 'direction', 'n_turns'])
    directions = ['left', 'straight', 'right']
    ticks = 0
    crash = False
    carts_to_be_removed = []

    while len(carts) > 1:
        ticks = ticks + 1
        crash_coordinates = 0, 0
        moved_carts = []
        carts_to_be_removed = []
        carts = sorted(carts, key=lambda cart: (cart.y, cart.x))
        for i, cart in enumerate(carts):
            if (cart.x, cart.y) in carts_to_be_removed:
                continue
            n_turns = cart.n_turns
            new_direction = cart.direction

            if cart.direction == 'north':
                new_x, new_y = cart.x, cart.y-1
            elif cart.direction == 'east':
                new_x, new_y = cart.x+1, cart.y
            elif cart.direction == 'south':
                new_x, new_y = cart.x, cart.y+1
            elif cart.direction == 'west':
                new_x, new_y = cart.x-1, cart.y

            if tracks[new_x, new_y] == "/":
                if cart.direction == 'north':
                    new_direction = 'east'
                elif cart.direction == 'east':
                    new_direction = 'north'
                elif cart.direction == 'south':
                    new_direction = 'west'
                elif cart.direction == 'west':
                    new_direction = 'south'
            elif tracks[new_x, new_y] == "\\":
                if cart.direction == 'north':
                    new_direction = 'west'
                elif cart.direction == 'east':
                    new_direction = 'south'
                elif cart.direction == 'south':
                    new_direction = 'east'
                elif cart.direction == 'west':
                    new_direction = 'north'
            elif tracks[new_x, new_y] == "+":
                n_turns = cart.n_turns + 1
                if n_turns == 3:
                    new_direction = turn_right(cart)
                    n_turns = 0
                elif n_turns == 2:
                    new_direction = go_straight(cart)
                elif n_turns == 1:
                    new_direction = turn_left(cart)

            # Check for collision
            if (new_x, new_y) in [(each.x, each.y) for each in carts[i+1:]]:
                carts_to_be_removed.append((new_x, new_y))
            if (new_x, new_y) in [(each.x, each.y) for each in moved_carts]:
                carts_to_be_removed.append((new_x, new_y))

            moved_carts.append(Cart(x=new_x, y=new_y,
                                    direction=new_direction,
                                    n_turns=n_turns))

        carts = moved_carts
        carts = [cart for cart in carts
                 if (cart.x, cart.y) not in carts_to_be_removed]

    remaining_cart = carts.pop(0)
    return (remaining_cart.x, remaining_cart.y)

def parse_mine(mine):
    Cart = namedtuple('Cart', ['x', 'y', 'direction', 'n_turns'])
    tracks = {}
    carts = []
    for y, row in enumerate(mine):
        for x, tile in enumerate(row):
            if tile == '|':
                tracks[(x, y)] = '|'
            elif tile == '-':
                tracks[(x, y)] = '-'
            elif tile == '/':
                tracks[(x, y)] = '/'
            elif tile == '\\':
                tracks[(x, y)] = '\\'
            elif tile == '+':
                tracks[(x, y)] = '+'
            elif tile == '^':
                carts.append(Cart(x=x, y=y, direction='north', n_turns=0))
            elif tile == '>':
                carts.append(Cart(x=x, y=y, direction='east', n_turns=0))
            elif tile == 'v':
                carts.append(Cart(x=x, y=y, direction='south', n_turns=0))
            elif tile == '<':
                carts.append(Cart(x=x, y=y, direction='west', n_turns=0))

    north_south_tracks = ['|', '/', '\\', '+']
    east_west_tracks = ['-', '/', '\\', '+']
    for cart in carts:
        north = (cart.x, cart.y+1)
        east = (cart.x+1, cart.y)
        south = (cart.x, cart.y-1)
        west = (cart.x-1, cart.y)
        if all([each in tracks for each in [north, east, south, west]]):
            if (tracks[north] != '-' and tracks[south] != '-' and
                    tracks[east] != '|' and tracks[west] != '|'):
                tracks[(cart.x, cart.y)] = '+'
        if north in tracks and south in tracks:
            if (tracks[north] in north_south_tracks and
                    tracks[south] in north_south_tracks):
                tracks[(cart.x, cart.y)] = '|'
                continue
        if west in tracks and east in tracks:
            tracks[(cart.x, cart.y)] = '-'

    return tracks, carts

def print_carts(tracks, carts):
    for cart in carts:
        print(cart, tracks[cart.x, cart.y])
        if (cart.x, cart.y-1) in tracks:
            north = tracks[cart.x, cart.y-1]
        else:
            north = ' '
        if (cart.x+1, cart.y) in tracks:
            east = tracks[cart.x+1, cart.y]
        else:
            east = ' '
        if (cart.x, cart.y+1) in tracks:
            south = tracks[cart.x, cart.y+1]
        else:
            south = ' '
        if (cart.x-1, cart.y) in tracks:
            west = tracks[cart.x-1, cart.y]
        else:
            west = ' '
        print(f" {north} ")
        print(f"{west}{cart.direction[0]}{east}")
        print(f" {south} ")

def main():
    mine = []
    with open('day_13_cart_tracks.txt', 'r') as mine_file:
        mine = mine_file.read().splitlines()
    tracks, carts = parse_mine(mine)

    first_crash_coordinates = drive_until_crash(tracks, carts)
    print(f"First crash at position: {first_crash_coordinates}")

    last_cart_coordinates = drive_until_crash_remove_carts(tracks, carts)
    print(f"Last cart at position: {last_cart_coordinates}")

if __name__ == '__main__':
    main()
