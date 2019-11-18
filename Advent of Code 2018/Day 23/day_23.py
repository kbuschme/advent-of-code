from collections import defaultdict
from itertools import combinations
"""
Advent of Code 2018

https://adventofcode.com/2018/day/23

--- Day 23: Experimental Emergency Teleportation ---

Using your torch to search the darkness of the rocky cavern, you finally
locate the man's friend: a small reindeer.

You're not sure how it got so far in this cave. It looks sick - too sick to
walk - and too heavy for you to carry all the way back. Sleighs won't be
invented for another 1500 years, of course.

The only option is experimental emergency teleportation.

You hit the "experimental emergency teleportation" button on the device and
push I accept the risk on no fewer than 18 different warning messages.
Immediately, the device deploys hundreds of tiny nanobots which fly around the
cavern, apparently assembling themselves into a very specific formation.
The device lists the X,Y,Z position (pos) for each nanobot as well as its
signal radius (r) on its tiny screen (your puzzle input).

Each nanobot can transmit signals to any integer coordinate which is
a distance away from it less than or equal to its signal radius (as measured
by Manhattan distance). Coordinates a distance away of less than or equal to
a nanobot's signal radius are said to be in range of that nanobot.

Before you start the teleportation process, you should determine which nanobot
is the strongest (that is, which has the largest signal radius) and then,
for that nanobot, the total number of nanobots that are in range of it,
including itself.

For example, given the following nanobots:

pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1

The strongest nanobot is the first one (position 0,0,0) because its signal
radius, 4 is the largest. Using that nanobot's location and signal radius,
the following nanobots are in or out of range:

  * The nanobot at 0,0,0 is distance 0 away, and so it is in range.
  * The nanobot at 1,0,0 is distance 1 away, and so it is in range.
  * The nanobot at 4,0,0 is distance 4 away, and so it is in range.
  * The nanobot at 0,2,0 is distance 2 away, and so it is in range.
  * The nanobot at 0,5,0 is distance 5 away, and so it is not in range.
  * The nanobot at 0,0,3 is distance 3 away, and so it is in range.
  * The nanobot at 1,1,1 is distance 3 away, and so it is in range.
  * The nanobot at 1,1,2 is distance 4 away, and so it is in range.
  * The nanobot at 1,3,1 is distance 5 away, and so it is not in range.

In this example, in total, 7 nanobots are in range of the nanobot with
the largest signal radius.

Find the nanobot with the largest signal radius. How many nanobots are
in range of its signals?

Your puzzle answer was 383.


--- Part Two ---

Now, you just need to figure out where to position yourself so that you're
actually teleported when the nanobots activate.

To increase the probability of success, you need to find the coordinate which
puts you in range of the largest number of nanobots. If there are multiple,
choose one closest to your position (0,0,0, measured by manhattan distance).

For example, given the following nanobot formation:

pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5

Many coordinates are in range of some of the nanobots in this formation.
However, only the coordinate 12,12,12 is in range of the most nanobots:
it is in range of the first five, but is not in range of the nanobot at
10,10,10. (All other coordinates are in range of fewer than five nanobots.)
This coordinate's distance from 0,0,0 is 36.

Find the coordinates that are in range of the largest number of nanobots.
What is the shortest manhattan distance between any of those points and 0,0,0?

Your puzzle answer was 100474026.
"""
def parse_bot_positions(positions_as_strings):
    positions = {}
    for pos in positions_as_strings:
        position, radius = pos.split(", ")
        x, y, z = tuple([int(coord) for coord in position[5:-1].split(",")])
        radius = int(radius[2:])
        positions[(x, y, z)] = radius
    return positions

def distance(position_1, position_2):
    return sum([abs(coord_1 - coord_2)
                for coord_1, coord_2 in zip(position_1, position_2)])

def find_nanobots_in_range(nanobots):
    strongest_bot = max(nanobots.items(), key=lambda bot: bot[1])
    strongest_bot_pos, strongest_bot_range = strongest_bot

    bots_in_range = {pos: radius
                     for pos, radius in nanobots.items()
                     if distance(pos, strongest_bot_pos) <= strongest_bot_range}
    return len(bots_in_range)

def find_maximum_cliques(nodes, neighbors):
    """Find maximum cliques using the Bron–Kerbosch Algorithm with pivoting."""

    def bron_kerbosch_algorithm(neighbors, P, R=None, X=None):
        """Bron–Kerbosch Algorithm with pivoting.

        Parameters
        ----------
        neighbors: dict
            A dict containing nodes as keys and lists of the node's neighbors
            as values.
        P: set
            A set containing all (potential) nodes that have not yet been
            considered. Initially, it contains all nodes of the graph.
        R: set (optional)
            A set containing nodes that form a clique. The clique gets expanded
            and it is a maximum clique, if P and X are both empty. Initially
            it is empty.
        X: set (optional)
            A set containing all (excluded) nodes that have already been considered but are not part of the clique. Initially it is empty.

        Returns
        -------
        maximum_cliques: list
            A list of sets which represent maximum cliques.
        """
        if R is None:
            R = set()
        if X is None:
            X = set()
        maximum_cliques = []

        if len(P) == 0 and len(X) == 0:
            return [R]

        # Pivoting: Exclude all neighbors of the node with the maximum neighbors
        bot_in_P_and_X_most_neighbors = max(
            [(bot, len(neighbors[bot])) for bot in P.union(X)],
            key=lambda b: b[1])[0]
        P_without_most_neighbors = P.copy().difference(
            neighbors[bot_in_P_and_X_most_neighbors])

        for vertex in P_without_most_neighbors:
            new_R = R.union({vertex})
            new_P = P.intersection(neighbors[vertex])
            new_X = X.intersection(neighbors[vertex])
            maximum_cliques.extend(bron_kerbosch_algorithm(neighbors, new_P,
                R=new_R, X=new_X))
            P.remove(vertex)
            X.add(vertex)

        return maximum_cliques

    return bron_kerbosch_algorithm(neighbors, P=set(nodes), R=None, X=None)

def find_shortest_distance(nanobots, origin=(0,0,0)):
    nanobots = list(nanobots.items())

    neighbors = defaultdict(set)
    for bot_1_index, bot_2_index in combinations(range(len(nanobots[:])), 2):
        bot_1_pos, bot_1_radius = nanobots[bot_1_index]
        bot_2_pos, bot_2_radius = nanobots[bot_2_index]
        if distance(bot_1_pos, bot_2_pos) <= bot_1_radius + bot_2_radius:
            neighbors[bot_2_index].add(bot_1_index)
            neighbors[bot_1_index].add(bot_2_index)

    maximum_cliques = find_maximum_cliques(neighbors.keys(), neighbors)

    origin_to_bot_radius_distances = []
    for bot_index in max(maximum_cliques, key=lambda c: len(c)):
        bot_position, bot_radius = nanobots[bot_index]
        origin_to_bot_radius_distances.append(
            distance(origin, bot_position) - bot_radius)

    return max(origin_to_bot_radius_distances)

def main():
    bot_positions = []
    with open('day_23_positions.txt', 'r') as positions_file:
        bot_positions = positions_file.read().splitlines()

    nanobots = parse_bot_positions(bot_positions)
    number_of_nanobots = find_nanobots_in_range(nanobots)
    print(f"Nanobots in range: {number_of_nanobots}")

    origin = (0, 0, 0)
    shortest_distance = find_shortest_distance(nanobots, origin=origin)
    print(f"Shortest distance to position: {shortest_distance}")

if __name__ == '__main__':
    main()
