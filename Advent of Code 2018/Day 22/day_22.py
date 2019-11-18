import heapq
"""
Advent of Code 2018

https://adventofcode.com/2018/day/22

--- Day 22: Mode Maze ---

This is it, your final stop: the year -483. It's snowing and dark outside;
the only light you can see is coming from a small cottage in the distance.
You make your way there and knock on the door.

A portly man with a large, white beard answers the door and invites you inside.
For someone living near the North Pole in -483, he must not get many visitors,
but he doesn't act surprised to see you. Instead, he offers you some milk and
cookies.

After talking for a while, he asks a favor of you. His friend hasn't come back
in a few hours, and he's not sure where he is. Scanning the region briefly,
you discover one life signal in a cave system nearby; his friend must have
taken shelter there. The man asks if you can go there to retrieve his friend.

The cave is divided into square regions which are either dominantly rocky,
narrow, or wet (called its type). Each region occupies exactly one coordinate
in X,Y format where X and Y are integers and zero or greater. (Adjacent
regions can be the same type.)

The scan (your puzzle input) is not very detailed: it only reveals the depth
of the cave system and the coordinates of the target. However, it does not
reveal the type of each region. The mouth of the cave is at 0,0.

The man explains that due to the unusual geology in the area, there is
a method to determine any region's type based on its erosion level.
The erosion level of a region can be determined from its geologic index.
The geologic index can be determined using the first rule that applies from
the list below:

  * The region at 0,0 (the mouth of the cave) has a geologic index of 0.
  * The region at the coordinates of the target has a geologic index of 0.
  * If the region's Y coordinate is 0, the geologic index is its X coordinate
    times 16807.
  * If the region's X coordinate is 0, the geologic index is its Y coordinate
    times 48271.
  * Otherwise, the region's geologic index is the result of multiplying the
    erosion levels of the regions at X-1,Y and X,Y-1.

A region's erosion level is its geologic index plus the cave system's depth,
all modulo 20183. Then:

  * If the erosion level modulo 3 is 0, the region's type is rocky.
  * If the erosion level modulo 3 is 1, the region's type is wet.
  * If the erosion level modulo 3 is 2, the region's type is narrow.

For example, suppose the cave system's depth is 510 and the target's
coordinates are 10,10. Using % to represent the modulo operator, the cavern
would look as follows:

  * At 0,0, the geologic index is 0. The erosion level is
    (0 + 510) % 20183 = 510. The type is 510 % 3 = 0, rocky.
  * At 1,0, because the Y coordinate is 0, the geologic index is
    1 * 16807 = 16807. The erosion level is (16807 + 510) % 20183 = 17317.
    The type is 17317 % 3 = 1, wet.
  * At 0,1, because the X coordinate is 0, the geologic index is
    1 * 48271 = 48271. The erosion level is (48271 + 510) % 20183 = 8415.
    The type is 8415 % 3 = 0, rocky.
  * At 1,1, neither coordinate is 0 and it is not the coordinate of the target,
    so the geologic index is the erosion level of 0,1 (8415) times the erosion
    level of 1,0 (17317), 8415 * 17317 = 145722555. The erosion level is
    (145722555 + 510) % 20183 = 1805. The type is 1805 % 3 = 2, narrow.
  * At 10,10, because they are the target's coordinates, the geologic index
    is 0. The erosion level is (0 + 510) % 20183 = 510. The type is
    510 % 3 = 0, rocky.
  * Drawing this same cave system with rocky as ., wet as =, narrow as |,
    the mouth as M, the target as T, with 0,0 in the top-left corner, X
    increasing to the right, and Y increasing downward, the top-left corner
    of the map looks like this:

M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Before you go in, you should determine the risk level of the area. For the
the rectangle that has a top-left corner of region 0,0 and a bottom-right
corner of the region containing the target, add up the risk level of each
individual region: 0 for rocky regions, 1 for wet regions, and 2 for narrow
regions.

In the cave system above, because the mouth is at 0,0 and the target is at
10,10, adding up the risk level of all regions with an X coordinate from 0 to
10 and a Y coordinate from 0 to 10, this total is 114.

What is the total risk level for the smallest rectangle that includes 0,0 and
the target's coordinates?

Your puzzle answer was 8575.


--- Part Two ---

Okay, it's time to go rescue the man's friend.

As you leave, he hands you some tools: a torch and some climbing gear.
You can't equip both tools at once, but you can choose to use neither.

Tools can only be used in certain regions:

  * In rocky regions, you can use the climbing gear or the torch.
    You cannot use neither (you'll likely slip and fall).
  * In wet regions, you can use the climbing gear or neither tool.
    You cannot use the torch (if it gets wet, you won't have a light source).
  * In narrow regions, you can use the torch or neither tool.
    You cannot use the climbing gear (it's too bulky to fit).

You start at 0,0 (the mouth of the cave) with the torch equipped and must
reach the target coordinates as quickly as possible. The regions with
negative X or Y are solid rock and cannot be traversed. The fastest route
might involve entering regions beyond the X or Y coordinate of the target.

You can move to an adjacent region (up, down, left, or right; never diagonally)
if your currently equipped tool allows you to enter that region. Moving to an
adjacent region takes one minute. (For example, if you have the torch
equipped, you can move between rocky and narrow regions, but cannot enter wet
regions.)

You can change your currently equipped tool or put both away if your new
equipment would be valid for your current region. Switching to using the
climbing gear, torch, or neither always takes seven minutes, regardless of
which tools you start with. (For example, if you are in a rocky region, you
can switch from the torch to the climbing gear, but you cannot switch to
neither.)

Finally, once you reach the target, you need the torch equipped before you can
find him in the dark. The target is always in a rocky region, so if you arrive
there with climbing gear equipped, you will need to spend seven minutes
switching to your torch.

For example, using the same cave system as above, starting in the top left
corner (0,0) and moving to the bottom right corner (the target, 10,10) as
quickly as possible, one possible route is as follows, with your current
position marked X:

Initially:
X=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Down:
M=.|=.|.|=.|=|=.
X|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Right:
M=.|=.|.|=.|=|=.
.X=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Switch from using the torch to neither tool:
M=.|=.|.|=.|=|=.
.X=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Right 3:
M=.|=.|.|=.|=|=.
.|=|X|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Switch from using neither tool to the climbing gear:
M=.|=.|.|=.|=|=.
.|=|X|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Down 7:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..X==..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Right:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..=X=..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Down 3:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||.X.|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Right:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||..X|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Down:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.X..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Right 4:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=X||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Up 2:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===X===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

Switch from using the climbing gear to the torch:
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===X===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||

This is tied with other routes as the fastest way to reach the target:
45 minutes. In it, 21 minutes are spent switching tools (three times, seven
minutes each) and the remaining 24 minutes are spent moving.

What is the fewest number of minutes you can take to reach the target?

Your puzzle answer was 999.
"""
class Tile(object):
    """Tiles represent the *regions* in the cave."""
    def __init__(self, position, geo_index, erosion, terrain, symbol,
                 time=None, equipped=None):
        super(Tile, self).__init__()
        self.position = position
        self.geo_index = geo_index
        self.erosion = erosion
        self.terrain = terrain
        self.symbol = symbol
        self.equipped = equipped
        self.time = time
    def __repr__(self):
        return (f"{self.position}: {self.terrain}, "
                f"equipped: {self.equipped}, time: {self.time}")

def build_cave(depth, target, start=(0, 0), x_max=None, y_max=None):
    if x_max is None or y_max is None:
        x_max, y_max = target[0], target[1]

    cave = {}
    for x in range(x_max + 1):
        for y in range(y_max + 1):
            if (x, y) == start:
                geo_index = 0
            elif (x, y) == target:
                geo_index = 0
            elif y == 0:
                geo_index = x * 16807
            elif x == 0:
                geo_index = y * 48271
            else:
                geo_index = cave[(x-1, y)].erosion * cave[(x, y-1)].erosion

            erosion_level = (geo_index + depth) % 20183

            if erosion_level % 3 == 0:
                terrain = 'rocky'
                symbol = '.'
            elif erosion_level % 3 == 1:
                terrain = 'wet'
                symbol = '='
            elif erosion_level % 3 == 2:
                terrain = 'narrow'
                symbol = '|'

            if (x, y) == start:
                symbol = 'M'
            elif (x, y) == target:
                symbol = 'T'

            cave[(x,y)] = Tile(position=(x,y), geo_index=geo_index,
                               erosion=erosion_level, terrain=terrain,
                               symbol=symbol)
    return cave

def cave_to_string(cave):
    x_max = max(cave.keys(), key=lambda coord: coord[0])[0]
    y_max = max(cave.keys(), key=lambda coord: coord[1])[1]

    rows = []
    for y in range(y_max + 1):
        rows.append("".join([cave[(x,y)].symbol for x in range(x_max + 1)]))
    return "\n".join(rows)

def assess_risk(tile):
    if tile.terrain == 'rocky':
        return 0
    elif tile.terrain == 'wet':
        return 1
    elif tile.terrain == 'narrow':
        return 2

def assess_total_risk(cave):
    return sum([assess_risk(tile) for tile in cave.values()])

def neighbors(current_tile, x_min, x_max, y_min, y_max):
    x, y = current_tile
    next_tiles = [
        (x, y) for x, y in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
               if x_min <= x <= x_max and y_min <= y <= y_max]
    return next_tiles

def find_shortest_path(cave, target, start=((0, 0), 'torch')):
    appropriate_gear = {
        ('rocky', 'rocky'): ['climbing_gear', 'torch'],
        ('wet', 'rocky'): ['climbing_gear'],
        ('rocky', 'wet'): ['climbing_gear'],
        ('narrow', 'narrow'): ['torch', 'neither'],
        ('narrow', 'rocky'): ['torch'],
        ('rocky', 'narrow'): ['torch'],
        ('wet', 'wet'): ['neither', 'climbing_gear'],
        ('wet', 'narrow'): ['neither'],
        ('narrow', 'wet'): ['neither'],
    }

    x_min = min(cave.keys(), key=lambda pos: pos[0])[0]
    x_max = max(cave.keys(), key=lambda pos: pos[0])[0]
    y_min = min(cave.keys(), key=lambda pos: pos[1])[1]
    y_max = max(cave.keys(), key=lambda pos: pos[1])[1]

    def switch_gear(terrain, equipped):
        if terrain == 'rocky':
            if equipped == 'climbing_gear':
                return 'torch'
            elif equipped == 'torch':
                return 'climbing_gear'
        elif terrain == 'wet':
            if equipped == 'climbing_gear':
                return 'neither'
            elif equipped == 'neither':
                return 'climbing_gear'
        elif terrain == 'narrow':
            if equipped == 'torch':
                return 'neither'
            elif equipped == 'neither':
                return 'torch'

    def next_situations(current_situation, x_min, x_max, y_min, y_max):
        current_tile, current_gear = current_situation
        current_terrain = cave[current_tile].terrain
        situations = {
            (current_tile, switch_gear(current_terrain, current_gear)): 7
        }
        for next_tile in neighbors(current_tile, x_min, x_max, y_min, y_max):
            next_terrain = cave[next_tile].terrain
            if current_gear in appropriate_gear[current_terrain, next_terrain]:
                situations[(next_tile, current_gear)] = 1
        return situations

    def dijkstra(situations, target, start=((0, 0), 'torch')):
        visited = set()
        travel_times = {}
        previous_situation = {}
        for (position, gear), tile in situations.items():
            travel_times[(position, gear)] = float('inf')
            previous_situation[(position, gear)] = None

        travel_times[start] = 0
        situations[start].time = 0

        priority_queue = []
        heapq.heapify(priority_queue)
        queue_items = len(priority_queue)
        heapq.heappush(priority_queue,
                       (travel_times[start], queue_items, start))
        queue_items += 1

        while len(priority_queue) > 0:
            _, _, closest_tile = heapq.heappop(priority_queue)
            if closest_tile not in visited:
                time_to_next_situations = next_situations(
                    closest_tile, x_min, x_max, y_min, y_max)
                for next_situation, time in time_to_next_situations.items():
                    if next_situation not in visited:
                        new_travel_time = travel_times[closest_tile] + time
                        if (travel_times[next_situation] > new_travel_time):
                            travel_times[next_situation] = new_travel_time
                            previous_situation[next_situation] = closest_tile
                            heapq.heappush(priority_queue, (new_travel_time,
                                queue_items, next_situation))
                            queue_items += 1
                            # Update tile objects too, for simpler printing
                            situations[next_situation].equipped = gear
                            situations[next_situation].time = new_travel_time
                visited.add(closest_tile)
        return travel_times, previous_situation

    def route(situations, previous_situation, start, target):
        route = [situations[target]]
        current_tile = target
        while current_tile != start:
            current_tile = previous_situation[current_tile]
            route.insert(0, situations[current_tile])
        return route

    situations = {}
    for position, tile in cave.items():
        for gear in appropriate_gear[(tile.terrain, tile.terrain)]:
            situations[position, gear] = tile

    travel_times, previous_situation = dijkstra(situations, target)
    route_to_target = route(situations, previous_situation, start, target)
    return cave, travel_times, previous_situation, route_to_target

def find_friend(cave, target, start=((0, 0), 'torch')):
    cave, travel_times, previous_situation, route = find_shortest_path(
        cave, (target, 'torch'), start=start)
    return travel_times[(target, 'torch')]

def main():
    with open('day_22_scan.txt', 'r') as scan_file:
        scan = scan_file.read().splitlines()
        depth = int(scan[0][7:])
        target = tuple([int(coordinate)
                        for coordinate in scan[1][8:].split(",")])

    print(f"Cave depth: {depth}\nTarget: {target}")
    cave = build_cave(depth, target)
    total_risk = assess_total_risk(cave)
    print(f"Total risk level: {total_risk}")

    x_max , y_max = target[0] + 50, target[1] + 50
    cave = build_cave(depth, target, x_max=x_max, y_max=y_max)
    minutes = find_friend(cave, target)
    print(f"Minutes to reach the friend: {minutes}")

if __name__ == '__main__':
    main()
