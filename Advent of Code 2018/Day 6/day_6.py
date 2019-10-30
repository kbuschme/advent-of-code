from collections import Counter
"""
Advent of Code 2018

https://adventofcode.com/2018/day/6

--- Day 6: Chronal Coordinates ---

The device on your wrist beeps several times, and once again you feel like
you're falling.

"Situation critical," the device announces. "Destination indeterminate.
Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they
places it thinks are safe or dangerous? It recommends you check manual page
729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the
coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate
by counting the number of integer X,Y locations that are closest to that
coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite.
For example, consider the following list of coordinates:

  * 1, 1
  * 1, 6
  * 8, 3
  * 3, 4
  * 5, 5
  * 8, 9

If we name these coordinates A through F, we can draw them on a grid, putting
0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.

This view is partial - the actual grid extends infinitely in all directions.
Using the Manhattan distance, each location's closest coordinate can be
determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf

Locations shown as . are equally far from two or more coordinates, and so
they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while
not shown here, their areas extend forever outside the visible grid. However,
the areas of coordinates D and E are finite: D is closest to 9 locations,
and E is closest to 17 (both including the coordinate's location itself).
Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?

Your puzzle answer was 3276.


--- Part Two ---

On the other hand, if the coordinates are safe, maybe the best you can do is
try to find a region near as many coordinates as possible.

For example, suppose you want the sum of the Manhattan distance to all of the
coordinates to be less than 32. For each location, add up the distances to
all of the given coordinates; if the total of those distances is less than 32,
that location is within the desired region. Using the same coordinates as
above, the resulting region looks like this:

..........
.A........
..........
...###..C.
..#D###...
..###E#...
.B.###....
..........
..........
........F.

In particular, consider the highlighted location 4,3 located at the top middle
of the region. Its calculation is as follows, where abs() is the absolute
value function:

  * Distance to coordinate A: abs(4-1) + abs(3-1) =  5
  * Distance to coordinate B: abs(4-1) + abs(3-6) =  6
  * Distance to coordinate C: abs(4-8) + abs(3-3) =  4
  * Distance to coordinate D: abs(4-3) + abs(3-4) =  2
  * Distance to coordinate E: abs(4-5) + abs(3-5) =  3
  * Distance to coordinate F: abs(4-8) + abs(3-9) = 10
  * Total distance: 5 + 6 + 4 + 2 + 3 + 10 = 30

Because the total distance to all coordinates (30) is less than 32, the
location is within the region.

This region, which also includes coordinates D and E, has a total size of 16.

Your actual region will need to be much larger than this example, though,
instead including all locations with a total distance of less than 10000.

What is the size of the region containing all locations which have a total
distance to all given coordinates of less than 10000?

Although it hasn't changed, you can still get your puzzle input.

Your puzzle answer was 38380.
"""

def print_grid(grid, landmarks):
    x_min = min(grid.keys(), key=lambda c: c[0])[0]
    x_max = max(grid.keys(), key=lambda c: c[0])[0]
    y_min = min(grid.keys(), key=lambda c: c[1])[1]
    y_max = max(grid.keys(), key=lambda c: c[1])[1]
    landmark_symbols = ['a', 'b', 'c', 'd', 'e', 'f']
    for y in range(y_min, y_max+1):
        for x in range(x_min, x_max+1):
            assigned_landmark, _ = grid[(x,y)]
            if assigned_landmark is not None:
                if (x, y) in landmarks:
                    print(landmark_symbols[assigned_landmark].upper(), end='')
                else:
                    print(landmark_symbols[assigned_landmark], end='')
            else:
                print('.', end='')
        print('\n', end='')

def assign_grid_to_closest_coordinate(coordinates, verbose=False):
    """Assign each grid position to the closest given coordinate."""
    grid = {(x, y): (i, 0) for i, (x, y) in enumerate(coordinates)}
    # Increase grid encompassing the given coordinates by 1 in each direction
    x_min = min(grid.keys(), key=lambda c: c[0])[0] - 1
    x_max = max(grid.keys(), key=lambda c: c[0])[0] + 1
    y_min = min(grid.keys(), key=lambda c: c[1])[1] - 1
    y_max = max(grid.keys(), key=lambda c: c[1])[1] + 1
    new_coordinates = {}
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            distances = [
                (area_id, sum((abs(x-c_x), abs(y-c_y))))
                for (c_x, c_y), (area_id, distance) in grid.items()]
            min_distance = min(distances, key=lambda d: d[1])[1]
            distances = [area_id
                         for area_id, distance in distances
                         if distance == min_distance]
            if len(distances) > 1:
                new_coordinates[(x,y)] = (None, min_distance)
            else:
                new_coordinates[(x,y)] = (distances[0], min_distance)
    grid.update(new_coordinates)
    return grid

def assign_grid_to_total_distance(coordinates, max_total_distance=10000):
    """Assign each grid position its total distance from given coordinates."""
    coordinates = {(x, y): (i, 0) for i, (x, y) in enumerate(coordinates)}
    # Increase given area limits in each direction by 1
    x_min = min(coordinates.keys(), key=lambda c: c[0])[0] - 1
    x_max = max(coordinates.keys(), key=lambda c: c[0])[0] + 1
    y_min = min(coordinates.keys(), key=lambda c: c[1])[1] - 1
    y_max = max(coordinates.keys(), key=lambda c: c[1])[1] + 1
    grid = {}
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            distances = [sum((abs(x-c_x), abs(y-c_y)))
                         for (c_x, c_y) in coordinates.keys()]
            total_distance = sum(distances)
            if total_distance < max_total_distance:
                grid[(x,y)] = total_distance
    return grid

def find_largest_area(coordinates, verbose=False):
    grid = assign_grid_to_closest_coordinate(coordinates)
    if verbose:
        print_grid(grid, coordinates)
    x_max = max(grid.keys(), key=lambda c: c[0])[0]
    x_min = min(grid.keys(), key=lambda c: c[0])[0]
    y_max = max(grid.keys(), key=lambda c: c[1])[1]
    y_min = min(grid.keys(), key=lambda c: c[1])[1]
    infinite_areas = set(area_id
                         for (x, y), (area_id, distance) in grid.items()
                         if x == x_min or x == x_max
                         or y == y_min or y == y_max)
    finite_areas = [area_id
                    for (x, y), (area_id, distance) in grid.items()
                    if area_id not in infinite_areas and area_id is not None]
    if verbose:
        print(f"Grid size: {len(grid)}")
        print(f"Infinite areas: {len(infinite_areas)}")
        print(f"Finite areas: {len(finite_areas)}")
    largest_area = Counter(finite_areas).most_common(1)[0][1]
    return largest_area

def find_suitable_region(coordinates, max_total_distance=10000):
    grid = assign_grid_to_total_distance(coordinates,
                                         max_total_distance=max_total_distance)
    return len(grid)

def main():
    coordinates = []
    with open('day_6_coordinates.txt', 'r') as coordinates_file:
        for row in coordinates_file.read().splitlines():
            x, y = row.split(', ')
            coordinates.append((int(x), int(y)))

    print(f"Largest area: {find_largest_area(coordinates)}")
    print(f"Suitable area: {find_suitable_region(coordinates)}")

if __name__ == '__main__':
    main()
