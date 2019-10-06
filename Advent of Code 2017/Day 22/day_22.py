"""
Advent of Code

https://adventofcode.com/2017/day/22

--- Day 22: Sporifica Virus ---

Diagnostics indicate that the local grid computing cluster has been
contaminated with the Sporifica Virus. The grid computing cluster is a
seemingly-infinite two-dimensional grid of compute nodes. Each node is either
clean or infected by the virus.

To prevent overloading the nodes (which would render them useless to the
virus) or detection by system administrators, exactly one virus carrier
moves through the network, infecting or cleaning nodes as it moves.
The virus carrier is always located on a single node in the network (the current node) and keeps track of the direction it is facing.

To avoid detection, the virus carrier works in bursts; in each burst, it wakes
up, does some work, and goes back to sleep. The following steps are all
executed in order one time each burst:

  * If the current node is infected, it turns to its right. Otherwise, it
    turns to its left. (Turning is done in-place; the current node does not
    change.)
  * If the current node is clean, it becomes infected. Otherwise,
    it becomes cleaned. (This is done after the node is considered for the
    purposes of changing direction.)
  * The virus carrier moves forward one node in the direction it is facing.

Diagnostics have also provided a map of the node infection status (your
puzzle input). Clean nodes are shown as .; infected nodes are shown as #.
This map only shows the center of the grid; there are many more nodes beyond
those shown, but none of them are currently infected.

The virus carrier begins in the middle of the map facing up.

For example, suppose you are given a map like this:

..#
#..
...

Then, the middle of the infinite grid looks like this, with the virus
carrier's position marked with [ ]:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . . #[.]. . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

The virus carrier is on a clean node, so it turns left, infects the node,
and moves left:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . .[#]# . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

The virus carrier is on an infected node, so it turns right, cleans the node,
and moves up:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . .[.]. # . . .
. . . . # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

Four times in a row, the virus carrier finds a clean, infects it, turns left,
and moves forward, ending in the same place and still facing up:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . #[#]. # . . .
. . # # # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

Now on the same node as before, it sees an infection, which causes it to turn
right, clean the node, and move forward:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . # .[.]# . . .
. . # # # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

After the above actions, a total of 7 bursts of activity had taken place.
Of them, 5 bursts of activity caused an infection.

After a total of 70, the grid looks like this, with the virus carrier facing
up:

. . . . . # # . .
. . . . # . . # .
. . . # . . . . #
. . # . #[.]. . #
. . # . # . . # .
. . . . . # # . .
. . . . . . . . .
. . . . . . . . .

By this time, 41 bursts of activity caused an infection (though most of those
nodes have since been cleaned).

After a total of 10000 bursts of activity, 5587 bursts will have caused an
infection.

Given your actual map, after 10000 bursts of activity, how many bursts cause
a node to become infected? (Do not count nodes that begin infected.)

Your puzzle answer was 5330.


--- Part Two ---

As you go to remove the virus from the infected nodes, it evolves to resist
your attempt.

Now, before it infects a clean node, it will weaken it to disable your
defenses. If it encounters an infected node, it will instead flag the node
to be cleaned in the future. So:

  * Clean nodes become weakened.
  * Weakened nodes become infected.
  * Infected nodes become flagged.
  * Flagged nodes become clean.

Every node is always in exactly one of the above states.

The virus carrier still functions in a similar way, but now uses the
following logic during its bursts of action:

  * Decide which way to turn based on the current node:
      * If it is clean, it turns left.
      * If it is weakened, it does not turn, and will continue moving in the
        same direction.
      * If it is infected, it turns right.
      * If it is flagged, it reverses direction, and will go back the way
        it came.
  * Modify the state of the current node, as described above.
  * The virus carrier moves forward one node in the direction it is facing.

Start with the same map (still using . for clean and # for infected) and still
with the virus carrier starting in the middle and facing up.

Using the same initial state as the previous example, and drawing weakened
as W and flagged as F, the middle of the infinite grid looks like this,
with the virus carrier's position again marked with [ ]:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . . #[.]. . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

This is the same as before, since no initial nodes are weakened or flagged.
The virus carrier is on a clean node, so it still turns left, instead weakens
the node, and moves left:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . .[#]W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

The virus carrier is on an infected node, so it still turns right, instead
flags the node, and moves up:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . .[.]. # . . .
. . . F W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

This process repeats three more times, ending on the previously-flagged node
and facing right:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . W W . # . . .
. . W[F]W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

Finding a flagged node, it reverses direction and cleans the node:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . W W . # . . .
. .[W]. W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

The weakened node becomes infected, and it continues in the same direction:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . W W . # . . .
.[.]# . W . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

Of the first 100 bursts, 26 will result in infection. Unfortunately, another
feature of this evolved virus is speed; of the first 10000000 bursts, 2511944
will result in infection.

Given your actual map, after 10000000 bursts of activity, how many bursts
cause a node to become infected? (Do not count nodes that begin infected.)

Your puzzle answer was 2512103.
"""

def parse_status_map(status):
    """Return a list of infected nodes from a list of status strings."""
    max_rows = len(status)
    max_cols = len(status[0])
    row_offset = max_rows // 2
    col_offset = max_cols // 2
    infected = '#'

    infected_nodes = []
    for i_row, row in enumerate(status):
        for i_col, col in enumerate(row):
            if col == infected:
                # Add infected nodes centred about the middle of the map
                infected_nodes.append((i_row - row_offset,
                                       i_col - col_offset))

    return infected_nodes


def turn_left(direction):
    if direction == 'north':
        return 'west'
    elif direction == 'east':
        return 'north'
    elif direction == 'south':
        return 'east'
    elif direction == 'west':
        return 'south'

def turn_right(direction):
    if direction == 'north':
        return 'east'
    elif direction == 'east':
        return 'south'
    elif direction =='south':
        return 'west'
    elif direction == 'west':
        return 'north'

def turn_around(direction):
    if direction == 'north':
        return 'south'
    elif direction == 'south':
        return 'north'
    elif direction =='west':
        return 'east'
    elif direction == 'east':
        return 'west'

def move(position, direction):
    x, y = position
    if direction == 'north':
        x = x - 1
    elif direction == 'south':
        x = x + 1
    elif direction == 'west':
        y = y - 1
    elif direction == 'east':
        y = y + 1
    return (x, y)

def wake_up(status_map, steps=10_000, verbose=False):
    """The virus carrier wakes up and takes steps."""
    new_infections = 0

    virus_position = (0, 0)
    virus_direction = 'north'

    for _ in range(steps):
        if virus_position in status_map:
            virus_direction = turn_right(virus_direction)
            status_map.remove(virus_position)
        else:
            virus_direction = turn_left(virus_direction)
            status_map.append(virus_position)
            new_infections = new_infections + 1
        virus_position = move(virus_position, virus_direction)

    return status_map, new_infections

def wake_up_modified(status_map, steps=10_000, verbose=False):
    """The virus carrier wakes up and takes steps."""
    infected = set(status_map)
    weakened = set()
    flagged = set()

    virus_position = (0, 0)
    virus_direction = 'north'

    new_infections = 0
    for _ in range(steps):
        if virus_position in infected:
            infected.remove(virus_position)
            flagged.add(virus_position)
            virus_direction = turn_right(virus_direction)
        elif virus_position in weakened:
            weakened.remove(virus_position)
            infected.add(virus_position)
            new_infections = new_infections + 1
        elif virus_position in flagged:
            flagged.remove(virus_position)
            virus_direction = turn_around(virus_direction)
        else:
            weakened.add(virus_position)
            virus_direction = turn_left(virus_direction)
        virus_position = move(virus_position, virus_direction)

    # draw_map(infected, weakened, flagged)
    return infected, weakened, flagged, new_infections

def count_newly_infected_nodes(status_map, steps=10_000):
    status_map = parse_status_map(status_map)
    before = status_map.copy()
    after, new_infections = wake_up(status_map, steps=steps)

    for each in before:
        if each in after:
            after.remove(each)

    return new_infections

def count_newly_infected_nodes_modified(status_map, steps=10_000_000):
    status_map = parse_status_map(status_map)
    _, _, _, new_infections = wake_up_modified(status_map, steps=steps)
    return new_infections

def draw_map(infected, weakened, flagged):
    not_clean = infected.union(weakened, flagged)
    max_distance_x = max(not_clean, key=lambda x: x[0])[0]
    max_distance_y = max(not_clean, key=lambda x: x[1])[1]
    max_distance = abs(max(max_distance_x, max_distance_y))
    size = 2*max_distance + 1
    grid = [[" . "]*size for _ in range(size)]
    for x, y in infected:
        grid[y][x] = " # "
    for x, y in weakened:
        grid[y][x] = " W "
    for x, y in flagged:
        grid[y][x] = " F "
    for row in grid:
        print("".join(row))

def main():
    infection_status = []
    with open("day_22_status_map.txt", 'r') as status_file:
        infection_status = status_file.read().splitlines()

    steps = 10_000
    print(f"Nodes becoming infected after {steps} steps:",
          f"{count_newly_infected_nodes(infection_status, steps=steps)}")

    steps = 10_000_000
    newly_infected_nodes = count_newly_infected_nodes_modified(
        infection_status, steps=steps)
    print(f"Nodes becoming infected after {steps} steps:",
          f"{newly_infected_nodes}")

if __name__ == '__main__':
    main()
