from collections import Counter
"""
Advent of Code 2018

https://adventofcode.com/2018/day/12

--- Day 12: Subterranean Sustainability ---

The year 518 is significantly more underground than your history books implied.
Either that, or you've arrived in a vast cavern network under the North Pole.

After exploring a little, you discover a long tunnel that contains a row of
small pots as far as you can see to your left and right. A few of them contain
plants - someone is trying to grow things in these geothermally-heated caves.

The pots are numbered, with 0 in front of you. To the left, the pots are
numbered -1, -2, -3, and so on; to the right, 1, 2, 3.... Your puzzle input
contains a list of pots from 0 to the right and whether they do (#) or do not
(.) currently contain a plant, the initial state. (No other pots currently
contain plants.) For example, an initial state of #..##.... indicates that pots
0, 3, and 4 currently contain plants.

Your puzzle input also contains some notes you find on a nearby table: someone
has been trying to figure out how these plants spread to nearby pots. Based on
the notes, for each generation of plants, a given pot has or does not have a
plant based on whether that pot (and the two pots on either side of it) had a
plant in the last generation. These are written as LLCRR => N, where L are
pots to the left, C is the current pot being considered, R are the pots to
the right, and N is whether the current pot will have a plant in the next
generation. For example:

  * A note like ..#.. => . means that a pot that contains a plant but with no
    plants within two pots of it will not have a plant in it during the next
    generation.
  * A note like ##.## => . means that an empty pot with two plants on each side
    of it will remain empty in the next generation.
  * A note like .##.# => # means that a pot has a plant in a given generation
    if, in the previous generation, there were plants in that pot, the one
    immediately to the left, and the one two pots to the right, but not in
    the ones immediately to the right and two to the left.

It's not clear what these plants are for, but you're sure it's important, so
you'd like to make sure the current configuration of plants is sustainable by
determining what will happen after 20 generations.

For example, given the following input:

initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #

For brevity, in this example, only the combinations which do produce a plant
are listed. (Your input includes all possible combinations.) Then, the next 20
generations will look like this:

                 1         2         3
       0         0         0         0
 0: ...#..#.#..##......###...###...........
 1: ...#...#....#.....#..#..#..#...........
 2: ...##..##...##....#..#..#..##..........
 3: ..#.#...#..#.#....#..#..#...#..........
 4: ...#.#..#...#.#...#..#..##..##.........
 5: ....#...##...#.#..#..#...#...#.........
 6: ....##.#.#....#...#..##..##..##........
 7: ...#..###.#...##..#...#...#...#........
 8: ...#....##.#.#.#..##..##..##..##.......
 9: ...##..#..#####....#...#...#...#.......
10: ..#.#..#...#.##....##..##..##..##......
11: ...#...##...#.#...#.#...#...#...#......
12: ...##.#.#....#.#...#.#..##..##..##.....
13: ..#..###.#....#.#...#....#...#...#.....
14: ..#....##.#....#.#..##...##..##..##....
15: ..##..#..#.#....#....#..#.#...#...#....
16: .#.#..#...#.#...##...#...#.#..##..##...
17: ..#...##...#.#.#.#...##...#....#...#...
18: ..##.#.#....#####.#.#.#...##...##..##..
19: .#..###.#..#.#.#######.#.#.#..#.#...#..
20: .#....##....#####...#######....#.#..##.

The generation is shown along the left, where 0 is the initial state. The pot
numbers are shown along the top, where 0 labels the center pot,
negative-numbered pots extend to the left, and positive pots extend toward
the right. Remember, the initial state begins at pot 0, which is not
the leftmost pot used in this example.

After one generation, only seven plants remain. The one in pot 0 matched
the rule looking for ..#.., the one in pot 4 matched the rule looking for
.#.#., pot 9 matched .##.., and so on.

In this example, after 20 generations, the pots shown as # contain plants,
the furthest left of which is pot -2, and the furthest right of which is
pot 34. Adding up all the numbers of plant-containing pots after the 20th
generation produces 325.

After 20 generations, what is the sum of the numbers of all pots which contain
a plant?

Your puzzle answer was 3217.


--- Part Two ---

You realize that 20 generations aren't enough. After all, these plants will
need to last another 1500 years to even reach your timeline, not to mention
your future.

After fifty billion (50000000000) generations, what is the sum of the numbers
of all pots which contain a plant?

Your puzzle answer was 4000000000866.
"""

def grow(state, rules):
    """Grow the plants in the pots for one generation."""
    lookahead = 2
    start = min(state) - lookahead
    stop = max(state) + lookahead
    pots_growing_plants = []

    next_state = set()
    for i in range(start, stop):
        pots = ["#" if j in state else "."
                for j in range(i-lookahead, i+lookahead+1)]
        if "".join(pots) in rules:
            if rules["".join(pots)] == "#":
                next_state.add(i)
                pots_growing_plants.append("".join(pots))
    return next_state, pots_growing_plants

def sum_of_pot_indices(pots_with_plants, rules, generations=20, verbose=False):
    applied_rules_log = {}
    for i in range(1, generations + 1):
        pots_with_plants, applied_rules = grow(pots_with_plants, rules)
        if tuple(applied_rules) in applied_rules_log.keys():
            loop_start = list(applied_rules_log.keys()).index(
                tuple(applied_rules)) + 1
            loop_start_pots_with_plants = list(
                applied_rules_log.values())[loop_start - 1]
            loop_start_sum_of_pot_indices = sum(loop_start_pots_with_plants)

            sum_of_pot_indices = sum(pots_with_plants)
            loop_change = sum_of_pot_indices - loop_start_sum_of_pot_indices

            if verbose:
                print(f"Loop detected! Generation: {loop_start} to {i}")
                print(f"Generation {loop_start} - Pots with plants: ",
                      f"{len(loop_start_pots_with_plants)}\n",
                      f"{loop_start_pots_with_plants}\n",
                      f"Sum of pot indices: {loop_start_sum_of_pot_indices}",
                      sep='')

                print(f"Generation {i} - Pots with plants: ",
                      f"{len(pots_with_plants)}\n",
                      f"{pots_with_plants}\n",
                      f"Sum of pot indices: {sum_of_pot_indices}",
                      sep='')
                print(f"Loop length: {i - loop_start}, change: {loop_change}")

            # Note: Only works for loops of length 1!
            final_sum_of_pot_indices = (sum_of_pot_indices
                                        + (generations - i) * loop_change)
            return final_sum_of_pot_indices
        else:
            applied_rules_log[tuple(applied_rules)] = pots_with_plants

    return sum(pots_with_plants)

def parse_rules(rules_as_strings):
    rules = {}
    for rule in rules_as_strings:
        pattern, result = rule.split(' => ')
        rules[pattern] = result
    return rules

def generate_state_from_string(initial_state_as_string):
    return set([i for i, pot in enumerate(initial_state_as_string)
                if pot == "#"])

def main():
    rows = []
    with open('day_12_pots.txt', 'r') as pots_file:
        rows = pots_file.read().splitlines()
    initial_state = generate_state_from_string(rows[0][15:])
    rules = parse_rules(rows[2:])

    n_plants = sum_of_pot_indices(initial_state, rules, generations=20)
    print(f"Sum of pot numbers with plants (20 generations): {n_plants}")

    g = 50_000_000_000
    n_plants = sum_of_pot_indices(initial_state, rules, generations=g)
    print(f"Sum of pot numbers with plants ({g} generations): {n_plants}")

if __name__ == '__main__':
    main()
