from collections import Counter
"""
Advent of Code

https://adventofcode.com/2017/day/7

--- Day 7: Recursive Circus ---

Wandering further through the circuits of the computer, you come upon a tower
of programs that have gotten themselves into a bit of trouble. A recursive
algorithm has gotten out of hand, and now they're balanced precariously in a
large tower.

One program at the bottom supports the entire tower. It's holding a large disc,
and on the disc are balanced several more sub-towers. At the bottom of these
sub-towers, standing on the bottom disc, are other programs, each holding their
own disc, and so on. At the very tops of these sub-sub-sub-...-towers, many
programs stand simply keeping the disc below them balanced but with no disc of
their own.

You offer to help, but first you need to understand the structure of these
towers. You ask each program to yell out their name, their weight, and (if
they're holding a disc) the names of the programs immediately above them
balancing on that disc. You write this information down (your puzzle input).
Unfortunately, in their panic, they don't do this in an orderly fashion; by
the time you're done, you're not sure which program gave which information.

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)

...then you would be able to recreate the structure of the towers
that looks like this:

                gyxo
              /
         ugml - ebii
       /      \
      |         jptl
      |
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |
      |         ktlj
       \      /
         fwft - cntj
              \
                xhth

In this example, tknk is at the bottom of the tower (the bottom program), and
is holding up ugml, padx, and fwft. Those programs are, in turn, holding up
other programs; in this example, none of those programs are holding up any
other programs, and are all the tops of their own towers. (The actual tower
balancing in front of you is much larger.)

Before you're ready to help them, you need to make sure your information
is correct. What is the name of the bottom program?

Your puzzle answer was cyrupz.


--- Part Two ---

The programs explain the situation: they can't get down. Rather, they could
get down, if they weren't expending all of their energy trying to keep the
tower balanced. Apparently, one program has the wrong weight, and until it's
fixed, they're stuck here.

For any program holding a disc, each program standing on that disc forms a
sub-tower. Each of those sub-towers are supposed to be the same weight, or
the disc itself isn't balanced. The weight of a tower is the sum of the
weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo,
ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc
and all programs above it must each match. This means that the following
sums must all be the same:

  * ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
  * padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
  * fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243

As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the
other two. Even though the nodes above ugml are balanced, ugml itself is too
heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the
towers balanced. If this change were made, its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight
need to be to balance the entire tower?

Your puzzle answer was 193.
"""

def origin(tower):
    tower = parse_tower(tower)

    segment = list(tower.keys())[0]
    while True:
        # print("Segment:", segment)
        if 'parent' in tower[segment]:
            # print(segment, tower[segment])
            segment = tower[segment]['parent']
        else:
            # print(segment, tower[segment])
            return segment

def find_adjustment(tower, verbose=False):
    root = origin(tower)
    tower = parse_tower(tower)
    tower, adjustments = balance_tower(tower, root)
    if verbose:
        print(f"Adjustments: {adjustments}")

    first_adjustment = adjustments[0]
    return first_adjustment

def balance_tower(tower, segment, adjustments=[], verbose=False):
    if 'children' in tower[segment]:
        for child in tower[segment]['children']:
            tower, adjustments = balance_tower(tower, child, adjustments)

        childrens_weights = [tower[child]['total_weight']
                             for child in tower[segment]['children']]
        counter = Counter(childrens_weights)
        # If children's weights are unbalanced, adjust them
        if len(counter) > 1:
            if verbose:
                print("Imbalance:", childrens_weights)
            odd_weight = [w for w, count in counter.items() if count == 1][0]
            target_weight = [w for w, count in counter.items() if count > 1][0]
            imbalanced_child = [child
                for child in tower[segment]['children']
                if tower[child]['total_weight'] == odd_weight][0]

            # Update the weight of the imbalanced child
            difference = (odd_weight - tower[imbalanced_child]['weight'])
            new_weight = target_weight - difference
            tower[imbalanced_child]['weight'] = new_weight

            # Update the total weight of the imbalanced child
            tower[imbalanced_child]['total_weight'] -= difference

            adjustments.append((imbalanced_child, new_weight))
            if verbose:
                print("New weight:", new_weight, imbalanced_child, "\n\n")

        # Set total weight of segment:
        adjusted_childrens_weights = sum([
            tower[child]['total_weight']
            for child in tower[segment]['children']])

        total_weight = tower[segment]['weight'] + adjusted_childrens_weights
    else:
        total_weight = tower[segment]['weight']

    tower[segment]['total_weight'] = total_weight
    return tower, adjustments

def parse_tower(raw_tower):
    """
    Returns tower from raw input.

    The resulting tower is a dictionary of program names and their details.
    The details are dictionaries themselves and contain the following:
      * the programs own weight
      * a list of children, i.e. all programs immediately above the it
    """
    tower = dict()
    for each in raw_tower:
        each = each.strip().replace(' ', '')
        each = each.split('->')
        name, weight = each[0].replace(')', '').split('(')
        if name not in tower:
            tower[name] = {'weight': int(weight)}
        else:
            tower[name]['weight'] = int(weight)
        if len(each) > 1:
            children = each[1].split(',')
            tower[name]['children'] = children
            for child in children:
                if child not in tower:
                    tower[child] = dict()
                tower[child]['parent'] = name

    return tower

def main():
    filename = "day_7_tower.txt"
    with open(filename, 'r') as tower_file:
        tower = tower_file.readlines()

    print(f"Bottom program: {origin(tower)}")
    program, new_weight = find_adjustment(tower)
    print(f"Required weight for program {program}: {new_weight}")

if __name__ == '__main__':
    main()
