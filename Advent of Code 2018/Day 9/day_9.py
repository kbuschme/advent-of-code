"""
Advent of Code 2018

https://adventofcode.com/2018/day/9

--- Day 9: Marble Mania ---

You talk to the Elves while you wait for your navigation system to initialize.
To pass the time, they introduce you to their favorite marble game.

The Elves play this game by taking turns arranging the marbles in a circle
according to very particular rules. The marbles are numbered starting with 0
and increasing by 1 until every marble has a number.

First, the marble numbered 0 is placed in the circle. At this point, while it
contains only a single marble, it is still a circle: the marble is both
clockwise from itself and counter-clockwise from itself. This marble is
designated the current marble.

Then, each Elf takes a turn placing the lowest-numbered remaining marble into
the circle between the marbles that are 1 and 2 marbles clockwise of the
current marble. (When the circle is large enough, this means that there is one
marble between the marble that was just placed and the current marble.)
The marble that was just placed then becomes the current marble.

However, if the marble that is about to be placed has a number which is a
multiple of 23, something entirely different happens.
First, the current player keeps the marble they would have placed, adding it
to their score. In addition, the marble 7 marbles counter-clockwise from
the current marble is removed from the circle and also added to the current
player's score. The marble located immediately clockwise of the marble
that was removed becomes the new current marble.

For example, suppose there are 9 players. After the marble with value 0 is
placed in the middle, each player (shown in square brackets) takes a turn.
The result of each of those turns would produce circles of marbles like this,
where clockwise is to the right and the resulting current marble is in
parentheses:

[-] (0)
[1]  0 (1)
[2]  0 (2) 1
[3]  0  2  1 (3)
[4]  0 (4) 2  1  3
[5]  0  4  2 (5) 1  3
[6]  0  4  2  5  1 (6) 3
[7]  0  4  2  5  1  6  3 (7)
[8]  0 (8) 4  2  5  1  6  3  7
[9]  0  8  4 (9) 2  5  1  6  3  7
[1]  0  8  4  9  2(10) 5  1  6  3  7
[2]  0  8  4  9  2 10  5(11) 1  6  3  7
[3]  0  8  4  9  2 10  5 11  1(12) 6  3  7
[4]  0  8  4  9  2 10  5 11  1 12  6(13) 3  7
[5]  0  8  4  9  2 10  5 11  1 12  6 13  3(14) 7
[6]  0  8  4  9  2 10  5 11  1 12  6 13  3 14  7(15)
[7]  0(16) 8  4  9  2 10  5 11  1 12  6 13  3 14  7 15
[8]  0 16  8(17) 4  9  2 10  5 11  1 12  6 13  3 14  7 15
[9]  0 16  8 17  4(18) 9  2 10  5 11  1 12  6 13  3 14  7 15
[1]  0 16  8 17  4 18  9(19) 2 10  5 11  1 12  6 13  3 14  7 15
[2]  0 16  8 17  4 18  9 19  2(20)10  5 11  1 12  6 13  3 14  7 15
[3]  0 16  8 17  4 18  9 19  2 20 10(21) 5 11  1 12  6 13  3 14  7 15
[4]  0 16  8 17  4 18  9 19  2 20 10 21  5(22)11  1 12  6 13  3 14  7 15
[5]  0 16  8 17  4 18(19) 2 20 10 21  5 22 11  1 12  6 13  3 14  7 15
[6]  0 16  8 17  4 18 19  2(24)20 10 21  5 22 11  1 12  6 13  3 14  7 15
[7]  0 16  8 17  4 18 19  2 24 20(25)10 21  5 22 11  1 12  6 13  3 14  7 15

The goal is to be the player with the highest score after the last marble is
used up. Assuming the example above ends after the marble numbered 25, the
winning score is 23+9=32 (because player 5 kept marble 23 and removed marble
9, while no other player got any points in this very short example game).

Here are a few more examples:

10 players; last marble is worth 1618 points: high score is 8317
13 players; last marble is worth 7999 points: high score is 146373
17 players; last marble is worth 1104 points: high score is 2764
21 players; last marble is worth 6111 points: high score is 54718
30 players; last marble is worth 5807 points: high score is 37305

What is the winning Elf's score?

Your puzzle answer was 394486.


--- Part Two ---

Amused by the speed of your answer, the Elves are curious:

What would the new winning Elf's score be if the number of the last marble
were 100 times larger?

Amused by the speed of your answer, the Elves are curious:

What would the new winning Elf's score be if the number of the last marble
were 100 times larger?

Your puzzle answer was 3276488008.
"""

class Marble(object):
    def __init__(self, value):
        super(Marble, self).__init__()
        self.value = value
        self.next_marble = self
        self.previous_marble = self

    def __str__(self):
        return str(self.as_list())

    def as_list(self):
        values = [self.value]
        current_marble = self.rotate()
        while current_marble != self:
            values.append(current_marble.value)
            current_marble = current_marble.rotate()
        return values

    def append(self, value):
        new_marble = Marble(value)
        # Link new marble to existing marbles
        new_marble.next_marble = self.next_marble
        new_marble.previous_marble = self
        # Link existing marbles to new marble
        self.next_marble.previous_marble = new_marble
        self.next_marble = new_marble

    def pop(self):
        value = self.value
        self.previous_marble.next_marble = self.next_marble
        self.next_marble.previous_marble = self.previous_marble
        return value

    def rotate(self, steps=1):
        if steps > 1:
            return self.next_marble.rotate(steps=steps-1)
        else:
            return self.next_marble

    def rotate_counter_clockwise(self, steps=1):
        if steps > 1:
            return self.previous_marble.rotate_counter_clockwise(steps=steps-1)
        else:
            return self.previous_marble

def next_player(scores, current_player):
    if current_player == len(scores):
        return 1
    else:
        return current_player + 1

def play_marble_mania(players, last_marble, verbose=False):
    scores = {player: 0 for player in range(1, players+1)}
    current_player = 1
    ring = Marble(0)
    for marble in range(1, last_marble+1):
        if marble % 23 == 0:
            ring = ring.rotate_counter_clockwise(7)
            removed_marble = ring.pop()
            scores[current_player] += marble + removed_marble
        else:
            ring = ring.rotate()
            ring.append(marble)
        ring = ring.rotate()
        if verbose:
            print_game_state(ring, current_player)
        current_player = next_player(scores, current_player)
    return scores

def print_game_state(ring, current_player):
    origin_marble = ring
    while origin_marble.value != 0:
        origin_marble = origin_marble.rotate()
    board = "".join([f" {marble} " if marble != ring.value else f"({marble})"
                                   for marble in origin_marble.as_list()])
    print(f"[{current_player}]", board, sep="")

def calculate_highest_score(players, last_marble):
    scores = play_marble_mania(players, last_marble)
    return max(scores.values())

def main():
    marbles = []
    with open('day_9_marbles.txt', 'r') as marbles_file:
        line = marbles_file.read().splitlines()
        players, last_marble = [int(s) for s in line[0].split()
                                       if s.isdigit()]

    score = calculate_highest_score(players, last_marble)
    print(f"Winning Elf's score: {score}")

    score = calculate_highest_score(players, last_marble*100)
    print(f"Winning Elf's score (with number of last marble x100): {score}")

if __name__ == '__main__':
    main()
