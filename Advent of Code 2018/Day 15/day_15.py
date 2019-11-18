import time
from copy import deepcopy
import heapq
from pprint import pprint
"""
Advent of Code 2018

https://adventofcode.com/2018/day/15

--- Day 15: Beverage Bandits ---

Having perfected their hot chocolate, the Elves have a new problem: the Goblins
that live in these caves will do anything to steal it. Looks like they're here
for a fight.

You scan the area, generating a map of the walls (#), open cavern (.), and
starting position of every Goblin (G) and Elf (E) (your puzzle input).

Combat proceeds in rounds; in each round, each unit that is still alive takes
a turn, resolving all of its actions before the next unit's turn begins.
On each unit's turn, it tries to move into range of an enemy (if it isn't
already) and then attack (if it is in range).

All units are very disciplined and always follow very strict combat rules.
Units never move or attack diagonally, as doing so would be dishonorable.
When multiple choices are equally valid, ties are broken in reading order:
top-to-bottom, then left-to-right. For instance, the order in which units take
their turns within a round is the reading order of their starting positions in
that round, regardless of the type of unit or whether other units have moved
after the round started. For example:

                 would take their
These units:   turns in this order:
  #######           #######
  #.G.E.#           #.1.2.#
  #E.G.E#           #3.4.5#
  #.G.E.#           #.6.7.#
  #######           #######

Each unit begins its turn by identifying all possible targets (enemy units).
If no targets remain, combat ends.

Then, the unit identifies all of the open squares (.) that are in range of each
target; these are the squares which are adjacent (immediately up, down, left,
or right) to any target and which aren't already occupied by a wall or another
unit. Alternatively, the unit might already be in range of a target. If the
unit is not already in range of a target, and there are no open squares which
are in range of a target, the unit ends its turn.

If the unit is already in range of a target, it does not move, but continues
its turn with an attack. Otherwise, since it is not in range of a target, it
moves.

To move, the unit first considers the squares that are in range and determines
which of those squares it could reach in the fewest steps. A step is a single
movement to any adjacent (immediately up, down, left, or right) open (.)
square. Units cannot move into walls or other units. The unit does this while
considering the current positions of units and does not do any prediction about
where units will be later. If the unit cannot reach (find an open path to) any
of the squares that are in range, it ends its turn. If multiple squares are in
range and tied for being reachable in the fewest steps, the step which is first
in reading order is chosen. For example:

Targets:      In range:     Reachable:    Nearest:      Chosen:
#######       #######       #######       #######       #######
#E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
#...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
#.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
#######       #######       #######       #######       #######

In the above scenario, the Elf has three targets (the three Goblins):

  * Each of the Goblins has open, adjacent squares which are in range (marked
    with a ? on the map).
  * Of those squares, four are reachable (marked @); the other two (on the
    right) would require moving through a wall or unit to reach.
  * Three of these reachable squares are nearest, requiring the fewest steps
    (only 2) to reach (marked !).
  * Of those, the square which is first in reading order is chosen (+).

The unit then takes a single step toward the chosen square along the shortest
path to that square. If multiple steps would put the unit equally closer to
its destination, the unit chooses the step which is first in reading order.
(This requires knowing when there is more than one shortest path so that you
can consider the first step of each such path.) For example:

In range:     Nearest:      Chosen:       Distance:     Step:
#######       #######       #######       #######       #######
#.E...#       #.E...#       #.E...#       #4E212#       #..E..#
#...?.#  -->  #...!.#  -->  #...+.#  -->  #32101#  -->  #.....#
#..?G?#       #..!G.#       #...G.#       #432G2#       #...G.#
#######       #######       #######       #######       #######

The Elf sees three squares in range of a target (?), two of which are nearest
(!), and so the first in reading order is chosen (+). Under "Distance", each
open square is marked with its distance from the destination square; the two
squares to which the Elf could move on this turn (down and to the right) are
both equally good moves and would leave the Elf 2 steps from being in range of
the Goblin. Because the step which is first in reading order is chosen,
the Elf moves right one square.

Here's a larger example of movement:

Initially:
#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########

After 1 round:
#########
#.G...G.#
#...G...#
#...E..G#
#.G.....#
#.......#
#G..G..G#
#.......#
#########

After 2 rounds:
#########
#..G.G..#
#...G...#
#.G.E.G.#
#.......#
#G..G..G#
#.......#
#.......#
#########

After 3 rounds:
#########
#.......#
#..GGG..#
#..GEG..#
#G..G...#
#......G#
#.......#
#.......#
#########

Once the Goblins and Elf reach the positions above, they all are either in
range of a target or cannot find any square in range of a target, and so none
of the units can move until a unit dies.

After moving (or if the unit began its turn in range of a target), the unit
attacks.

To attack, the unit first determines all of the targets that are in range of
it by being immediately adjacent to it. If there are no such targets, the unit
ends its turn. Otherwise, the adjacent target with the fewest hit points is
selected; in a tie, the adjacent target with the fewest hit points which is
first in reading order is selected.

The unit deals damage equal to its attack power to the selected target,
reducing its hit points by that amount. If this reduces its hit points to 0
or fewer, the selected target dies: its square becomes . and it takes no
further turns.

Each unit, either Goblin or Elf, has 3 attack power and starts with 200 hit
points.

For example, suppose the only Elf is about to attack:

       HP:            HP:
G....  9       G....  9
..G..  4       ..G..  4
..EG.  2  -->  ..E..
..G..  2       ..G..  2
...G.  1       ...G.  1

The "HP" column shows the hit points of the Goblin to the left in the
corresponding row. The Elf is in range of three targets: the Goblin above it
(with 4 hit points), the Goblin to its right (with 2 hit points), and the
Goblin below it (also with 2 hit points). Because three targets are in range,
the ones with the lowest hit points are selected: the two Goblins with 2 hit
points each (one to the right of the Elf and one below the Elf). Of those,
the Goblin first in reading order (the one to the right of the Elf) is
selected. The selected Goblin's hit points (2) are reduced by the Elf's attack
power (3), reducing its hit points to -1, killing it.

After attacking, the unit's turn ends. Regardless of how the unit's turn ends,
the next unit in the round takes its turn. If all units have taken turns in
this round, the round ends, and a new round begins.

The Elves look quite outnumbered. You need to determine the outcome of the
battle: the number of full rounds that were completed (not counting the round
in which combat ends) multiplied by the sum of the hit points of all remaining
units at the moment combat ends. (Combat only ends when a unit finds no
targets during its turn.)

Below is an entire sample combat. Next to each map, each row's units' hit
points are listed from left to right.

Initially:
#######
#.G...#   G(200)
#...EG#   E(200), G(200)
#.#.#G#   G(200)
#..G#E#   G(200), E(200)
#.....#
#######

After 1 round:
#######
#..G..#   G(200)
#...EG#   E(197), G(197)
#.#G#G#   G(200), G(197)
#...#E#   E(197)
#.....#
#######

After 2 rounds:
#######
#...G.#   G(200)
#..GEG#   G(200), E(188), G(194)
#.#.#G#   G(194)
#...#E#   E(194)
#.....#
#######

Combat ensues; eventually, the top Elf dies:

After 23 rounds:
#######
#...G.#   G(200)
#..G.G#   G(200), G(131)
#.#.#G#   G(131)
#...#E#   E(131)
#.....#
#######

After 24 rounds:
#######
#..G..#   G(200)
#...G.#   G(131)
#.#G#G#   G(200), G(128)
#...#E#   E(128)
#.....#
#######

After 25 rounds:
#######
#.G...#   G(200)
#..G..#   G(131)
#.#.#G#   G(125)
#..G#E#   G(200), E(125)
#.....#
#######

After 26 rounds:
#######
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(122)
#...#E#   E(122)
#..G..#   G(200)
#######

After 27 rounds:
#######
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(119)
#...#E#   E(119)
#...G.#   G(200)
#######

After 28 rounds:
#######
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(116)
#...#E#   E(113)
#....G#   G(200)
#######

More combat ensues; eventually, the bottom Elf dies:

After 47 rounds:
#######
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(59)
#...#.#
#....G#   G(200)
#######

Before the 48th round can finish, the top-left Goblin finds that there are no
targets remaining, and so combat ends. So, the number of full rounds that were
completed is 47, and the sum of the hit points of all remaining units is
200+131+59+200 = 590. From these, the outcome of the battle is
47 * 590 = 27730.

Here are a few example summarized combats:

#######       #######
#G..#E#       #...#E#   E(200)
#E#E.E#       #E#...#   E(197)
#G.##.#  -->  #.E##.#   E(185)
#...#E#       #E..#E#   E(200), E(200)
#...E.#       #.....#
#######       #######

Combat ends after 37 full rounds
Elves win with 982 total hit points left
Outcome: 37 * 982 = 36334

#######       #######
#E..EG#       #.E.E.#   E(164), E(197)
#.#G.E#       #.#E..#   E(200)
#E.##E#  -->  #E.##.#   E(98)
#G..#.#       #.E.#.#   E(200)
#..E#.#       #...#.#
#######       #######

Combat ends after 46 full rounds
Elves win with 859 total hit points left
Outcome: 46 * 859 = 39514

#######       #######
#E.G#.#       #G.G#.#   G(200), G(98)
#.#G..#       #.#G..#   G(200)
#G.#.G#  -->  #..#..#
#G..#.#       #...#G#   G(95)
#...E.#       #...G.#   G(200)
#######       #######

Combat ends after 35 full rounds
Goblins win with 793 total hit points left
Outcome: 35 * 793 = 27755

#######       #######
#.E...#       #.....#
#.#..G#       #.#G..#   G(200)
#.###.#  -->  #.###.#
#E#G#G#       #.#.#.#
#...#G#       #G.G#G#   G(98), G(38), G(200)
#######       #######

Combat ends after 54 full rounds
Goblins win with 536 total hit points left
Outcome: 54 * 536 = 28944

#########       #########
#G......#       #.G.....#   G(137)
#.E.#...#       #G.G#...#   G(200), G(200)
#..##..G#       #.G##...#   G(200)
#...##..#  -->  #...##..#
#...#...#       #.G.#...#   G(200)
#.G...G.#       #.......#
#.....G.#       #.......#
#########       #########

Combat ends after 20 full rounds
Goblins win with 937 total hit points left
Outcome: 20 * 937 = 18740

What is the outcome of the combat described in your puzzle input?

Your puzzle answer was 201123.

--- Part Two ---

According to your calculations, the Elves are going to lose badly. Surely,
you won't mess up the timeline too much if you give them just a little
advanced technology, right?

You need to make sure the Elves not only win, but also suffer no losses:
even the death of a single Elf is unacceptable.

However, you can't go too far: larger changes will be more likely to
permanently alter spacetime.

So, you need to find the outcome of the battle in which the Elves have
the lowest integer attack power (at least 4) that allows them to win without
a single death. The Goblins always have an attack power of 3.

In the first summarized example above, the lowest attack power the Elves need
to win without losses is 15:

#######       #######
#.G...#       #..E..#   E(158)
#...EG#       #...E.#   E(14)
#.#.#G#  -->  #.#.#.#
#..G#E#       #...#.#
#.....#       #.....#
#######       #######

Combat ends after 29 full rounds
Elves win with 172 total hit points left
Outcome: 29 * 172 = 4988


In the second example above, the Elves need only 4 attack power:

#######       #######
#E..EG#       #.E.E.#   E(200), E(23)
#.#G.E#       #.#E..#   E(200)
#E.##E#  -->  #E.##E#   E(125), E(200)
#G..#.#       #.E.#.#   E(200)
#..E#.#       #...#.#
#######       #######

Combat ends after 33 full rounds
Elves win with 948 total hit points left
Outcome: 33 * 948 = 31284


In the third example above, the Elves need 15 attack power:

#######       #######
#E.G#.#       #.E.#.#   E(8)
#.#G..#       #.#E..#   E(86)
#G.#.G#  -->  #..#..#
#G..#.#       #...#.#
#...E.#       #.....#
#######       #######

Combat ends after 37 full rounds
Elves win with 94 total hit points left
Outcome: 37 * 94 = 3478


In the fourth example above, the Elves need 12 attack power:

#######       #######
#.E...#       #...E.#   E(14)
#.#..G#       #.#..E#   E(152)
#.###.#  -->  #.###.#
#E#G#G#       #.#.#.#
#...#G#       #...#.#
#######       #######

Combat ends after 39 full rounds
Elves win with 166 total hit points left
Outcome: 39 * 166 = 6474


In the last example above, the lone Elf needs 34 attack power:

#########       #########
#G......#       #.......#
#.E.#...#       #.E.#...#   E(38)
#..##..G#       #..##...#
#...##..#  -->  #...##..#
#...#...#       #...#...#
#.G...G.#       #.......#
#.....G.#       #.......#
#########       #########

Combat ends after 30 full rounds
Elves win with 38 total hit points left
Outcome: 30 * 38 = 1140

After increasing the Elves' attack power until it is just barely enough for
them to win without any Elves dying, what is the outcome of the combat
described in your puzzle input?

Your puzzle answer was 54188.
"""
class Unit(object):
    """Unit"""
    def __init__(self, team, hit_points=200):
        super(Unit, self).__init__()
        self.team = team
        self.hit_points = hit_points

def load_cave(file_name='day_15_cave.txt', initial_hitpoints=200):
    with open(file_name, 'r') as cave_file:
        cave_as_string = cave_file.read().strip()
    return parse_cave_string(cave_as_string)

def parse_cave_string(cave_as_string, initial_hitpoints=200):
    cave = {}
    units = {}
    for y, row in enumerate(cave_as_string.split("\n")):
        for x, square in enumerate(row):
            if square == "#":
                cave[(x, y)] = 'wall'
            elif square == ".":
                cave[(x, y)] = 'empty'
            elif square == "G":
                cave[(x, y)] = ('goblin', initial_hitpoints)
                units[(x, y)] = ('goblin', initial_hitpoints)
            elif square == "E":
                cave[(x, y)] = ('elf', initial_hitpoints)
                units[(x, y)] = ('elf', initial_hitpoints)
    return cave, units

def print_cave(cave):
    x_low = min(cave.keys(), key=lambda pos: pos[0])[0]
    x_high = max(cave.keys(), key=lambda pos: pos[0])[0]
    y_low = min(cave.keys(), key=lambda pos: pos[1])[1]
    y_high = max(cave.keys(), key=lambda pos: pos[1])[1]
    for y in range(y_low, y_high+1):
        units = []
        cave_row = []
        for x in range(x_low, x_high+1):
            square = cave[x, y]
            if square == 'wall':
                cave_row.append("#")
            elif square == 'empty':
                cave_row.append(".")
            elif square[0] == 'goblin':
                cave_row.append("G")
                units.append(f"G({square[1]})")
            elif square[0] == 'elf':
                cave_row.append("E")
                units.append(f"E({square[1]})")
        print("".join(cave_row), ", ".join(units), sep=' '*3)

def neighbors(position, cave, x_min=None, x_max=None, y_min=None, y_max=None):
    """Note that the neighbors are returned in reading order."""
    x, y = position
    if x_min is None:
        x_min = min(cave.keys(), key=lambda pos: pos[0])[0]
    if x_max is None:
        x_max = max(cave.keys(), key=lambda pos: pos[0])[0]
    if y_min is None:
        y_min = min(cave.keys(), key=lambda pos: pos[1])[1]
    if y_max is None:
        y_max = max(cave.keys(), key=lambda pos: pos[1])[1]
    new_positions = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
    new_positions = [(x, y) for x, y in new_positions
                            if x_min <= x <= x_max and y_min <= y <= y_max]
    return new_positions

def move(position, units, cave, verbose=False):
    x_min = min(cave.keys(), key=lambda pos: pos[0])[0]
    x_max = max(cave.keys(), key=lambda pos: pos[0])[0]
    y_min = min(cave.keys(), key=lambda pos: pos[1])[1]
    y_max = max(cave.keys(), key=lambda pos: pos[1])[1]

    def empty_neighbors(position, cave):
        positions = [(x, y) for x, y in neighbors(position, cave)
                            if cave[(x, y)] == 'empty']
        return positions

    def positions_around_enemies(own_position, enemy_position, cave):
        positions = empty_neighbors(enemy_position, cave)
        own_x, own_y = own_position
        enemy_x, enemy_y = enemy_position
        if abs(own_x - enemy_x) + abs(own_y - enemy_y) <= 1:
            positions.append(own_position)
        return positions

    def dijkstra(cave, start, target_positions):
        """Find shortest path to target positions with Dijkstra's algorithm."""
        visited = set()
        distances = {}
        previous = {}
        for position, tile in cave.items():
            distances[position] = float('inf')
            previous[position] = None
        distances[start] = 0

        priority_queue = []
        heapq.heapify(priority_queue)
        queue_items = len(priority_queue)
        heapq.heappush(priority_queue,
                       (distances[start], queue_items, start))
        queue_items += 1

        while len(priority_queue) > 0:
            _, _, closest_tile = heapq.heappop(priority_queue)
            if closest_tile not in visited:
                for neighbor in empty_neighbors(closest_tile, cave):
                    if neighbor not in visited:
                        new_distance = distances[closest_tile] + 1
                        if (distances[neighbor] > new_distance):
                            distances[neighbor] = new_distance
                            previous[neighbor] = closest_tile
                            heapq.heappush(priority_queue, (new_distance,
                                queue_items, neighbor))
                            queue_items += 1
                visited.add(closest_tile)

            if closest_tile in target_positions:
                return distances, previous

        return distances, previous

    if verbose:
        print("Unit:", position, units[position])
    # 1. Identify enemies, their positions and tiles adjacent to them
    x, y = position
    unit = units[position]
    unit_type = unit[0]
    if unit_type == 'goblin':
        enemy_type = 'elf'
    elif unit_type == 'elf':
        enemy_type = 'goblin'
    enemies = {position: unit for position, unit in units.items()
                              if unit[0] == enemy_type}
    target_positions = []
    for enemy_position in enemies.keys():
        target_positions.extend(
            positions_around_enemies(position, enemy_position, cave))
    # 2. Calculate the shortest routes to target positions
    distances, previous = dijkstra(cave, position, target_positions)

    # 3. Choose closest target and generate route to it
    reachable_targets = {position: distance
                         for position, distance in distances.items()
                         if position in target_positions and
                            distance < float('inf')}
    best_routes = []
    if len(reachable_targets) != 0:
        # Break ties using reading order (top to bottom, left to right)
        closest_target = min(reachable_targets.items(),
                             key=lambda t: (t[1], t[0][1], t[0][0]))[0]
        current_step = closest_target
        while current_step != position:
            best_routes.insert(0, current_step)
            current_step = previous[current_step]

    # 4. If a route to an enemy exists, take a step on the shortest path
    if len(best_routes) > 0:
        next_step = best_routes[0]
        cave[position] = 'empty'
        cave[next_step] = unit
        if verbose:
            print(f"Move {unit}\tform {position} to {next_step}")
        units.pop(position)
        units[next_step] = unit
        position = next_step

    if verbose:
        print("Routes:")
        pprint(best_routes)

    return position, units, cave

def choose_enemy(position, units, cave):
    attacker = units[position]
    attacker_type = attacker[0]
    close_enemies = [(position, units[position][1])
                     for position in neighbors(position, cave)
                     if position in units and
                        units[position][0] != attacker_type]
    if len(close_enemies) != 0:
        return min(close_enemies, key=lambda e: (e[1], e[0][1], e[0][0]))[0]
    else:
        return None

def attack(attacker, defender, units, cave, attack_power):
    attacker_type, _ = units[attacker]
    defender_type, defender_hit_points = units[defender]
    damage = attack_power[attacker_type]
    remaining_hit_points = defender_hit_points - damage
    if remaining_hit_points > 0:
        units[defender] = defender_type, remaining_hit_points
        cave[defender] = defender_type, remaining_hit_points
    else:
        cave[defender] = 'empty'
        units.pop(defender)
    return units, cave

def fight(cave, units, attack_power=None, verbose=False):
    if attack_power is None:
        attack_power = {'elf': 3, 'goblin': 3}

    # Fight until one faction won
    full_rounds = 0
    fighting = True
    while fighting:

        if verbose:
            if full_rounds == 0:
                print(f"Initially")
            else:
                print(f"After round: {full_rounds}")
            print_cave(cave)
            print()

        for position in sorted(units.keys(), key=lambda pos: (pos[1], pos[0])):
            # 1. Check if fight is still ongoing
            goblins = {position: unit for position, unit in units.items()
                                      if unit[0] == 'goblin'}
            elves = {position: unit for position, unit in units.items()
                                    if unit[0] == 'elf'}
            if len(elves) == 0 or len(goblins) == 0:
                if len(elves) == 0:
                    remaining_hitpoints = sum([g[1] for g in goblins.values()
                                                    if g[1] > 0])
                elif len(goblins) == 0:
                    remaining_hitpoints = sum([e[1] for e in elves.values()
                                                    if e[1] > 0])
                if verbose:
                    print(f"Combat ends after {full_rounds} full rounds.")
                    print_cave(cave)
                    print()
                return full_rounds, remaining_hitpoints, units

            # 2. If the unit itself is still alive, move and attack
            if position in units:
                enemy_position = choose_enemy(position, units, cave)
                if enemy_position is None:
                    position, units, cave = move(position, units, cave)
                    enemy_position = choose_enemy(position, units, cave)

                if enemy_position is not None:
                    units, cave = attack(position, enemy_position, units,
                        cave, attack_power)

        full_rounds += 1

def find_minimum_elf_attack_power(cave, units, verbose=False):
    """Note: All rounds are played until one faction is defeated."""
    elves_losing = True
    elf_attack_power, goblin_attack_power = 3, 3
    attack_power = {
        'elf': elf_attack_power,
        'goblin': goblin_attack_power
    }
    while elves_losing:
        if verbose:
            print(f"Elf attack power: {elf_attack_power}")
        attack_power['elf'] = elf_attack_power
        elves = [unit for _, unit in units.items() if unit[0] == 'elf']
        full_rounds, remaining_hitpoints, remaining_units = fight(
            cave.copy(), units.copy(), attack_power)
        remaining_elves = [unit for _, unit in remaining_units.items()
                                if unit[0] == 'elf']
        if len(remaining_elves) == len(elves):
            return full_rounds, remaining_hitpoints, elf_attack_power
        elf_attack_power += 1

def main():
    cave, units = load_cave(file_name='day_15_cave.txt')

    # Solution: 81 * 2483 = 201123
    attack_power = {
        'elf': 3,
        'goblin': 3
    }
    start_time = time.time()
    rounds, hitpoints, winning_team = fight(cave.copy(), units.copy(),
        attack_power=attack_power)
    print(f"Combat outcome: {rounds} * {hitpoints} = {rounds * hitpoints}")
    print(f"Elapsed time: {(time.time() - start_time)}s")

    # Solution: 46 * 1178 = 54188
    print("Part 2: This might take a while...")
    start_time = time.time()
    rounds, hitpoints, attack_power = find_minimum_elf_attack_power(
        cave.copy(), units.copy())
    print(f"Combat outcome (elves win, attack power: {attack_power}):",
        f"{rounds} * {hitpoints} = {rounds * hitpoints}")
    print(f"Elapsed time: {(time.time() - start_time)}s")

if __name__ == '__main__':
    main()
