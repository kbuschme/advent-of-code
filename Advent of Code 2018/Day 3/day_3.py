from collections import namedtuple
"""
Advent of Code 2018

https://adventofcode.com/2018/day/3

--- Day 3: No Matter How You Slice It ---

The Elves managed to locate the chimney-squeeze prototype fabric for Santa's
suit (thanks to someone who helpfully wrote its box IDs on the wall of the
warehouse in the middle of the night). Unfortunately, anomalies are still
affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least
1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's
suit. All claims have an ID and consist of a single rectangle with edges
parallel to the edges of the fabric. Each claim's rectangle is defined as
follows:

  * The number of inches between the left edge of the fabric and the left
    edge of the rectangle.
  * The number of inches between the top edge of the fabric and the top
    edge of the rectangle.
  * The width of the rectangle in inches.
  * The height of the rectangle in inches.

A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle
3 inches from the left edge, 2 inches from the top edge, 5 inches wide,
and 4 inches tall. Visually, it claims the square inches of fabric
represented by # (and ignores the square inches of fabric represented by .)
in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........

The problem is that many of the claims overlap, causing two or more claims to
cover part of the same areas. For example, consider the following claims:

  * #1 @ 1,3: 4x4
  * #2 @ 3,1: 4x4
  * #3 @ 5,5: 2x2

Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........

The four square inches marked with X are claimed by both 1 and 2. (Claim 3,
while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough
fabric. How many square inches of fabric are within two or more claims?

Your puzzle answer was 112378.


--- Part Two ---

Amidst the chaos, you notice that exactly one claim doesn't overlap by even a
single square inch of fabric with any other claim. If you can somehow draw
attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are
made.

What is the ID of the only claim that doesn't overlap?

Your puzzle answer was 603.
"""

def draw_claims_on_fabric(claims):
    fabric = {}
    for claim in claims:
        x, y = claim.pos
        rows, cols = claim.size
        for row in range(rows):
            for col in range(cols):
                if (x+row, y+col) in fabric:
                    fabric[(x+row, y+col)] = 'X'
                else:
                    fabric[(x+row, y+col)] = claim.id
    return fabric

def find_overlapping_square_inches(claims):
    claims = parse_claims(claims)
    fabric = draw_claims_on_fabric(claims)
    return len([1 for square in fabric.values() if square == 'X'])

def find_not_overlapping_claim(claims):
    claims = parse_claims(claims)
    fabric = draw_claims_on_fabric(claims)
    for claim in claims:
        x, y = claim.pos
        rows, cols = claim.size
        overlapped = False
        for row in range(rows):
            for col in range(cols):
                if fabric[x+row, y+col] == 'X':
                    overlapped = True
        if not overlapped:
            return claim.id

def parse_claims(claims_as_strings):
    Claim = namedtuple('Claim', ['id', 'pos', 'size'])
    claims = []
    for row in claims_as_strings:
        claim_id, claim_spec  = row.replace(" ", "").split('@')
        claim_id = int(claim_id.strip("#"))
        claim_pos, claim_size = claim_spec.split(":")
        claim_pos = tuple([int(each) for each in claim_pos.split(",")])
        claim_size = tuple([int(each) for each in claim_size.split("x")])
        claims.append(Claim(id=claim_id, pos=claim_pos, size=claim_size))
    return claims

def main():
    claims = []
    with open("day_3_claims.txt", 'r') as claims_file:
        claims = claims_file.read().splitlines()

    overlapping_square_inches = find_overlapping_square_inches(claims)
    print(f"Overlapping square inches: {overlapping_square_inches}")
    print(f"Not overlapping claim: {find_not_overlapping_claim(claims)}")

if __name__ == '__main__':
    main()
