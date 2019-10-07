"""
Advent of Code 2017

https://adventofcode.com/2017/day/24

--- Day 24: Electromagnetic Moat ---

The CPU itself is a large, black building surrounded by a bottomless pit.
Enormous metal tubes extend outward from the side of the building at regular
intervals and descend down into the void. There's no way to cross, but you need
to get inside.

No way, of course, other than building a bridge out of the magnetic components
strewn about nearby.

Each component has two ports, one on each end. The ports come in all different
types, and only matching types can be connected. You take an inventory of the
components by their port types (your puzzle input). Each port is identified by
the number of pins it uses; more pins mean a stronger connection for your
bridge. A 3/7 component, for example, has a type-3 port on one side, and a
type-7 port on the other.

Your side of the pit is metallic; a perfect surface to connect a magnetic,
zero-pin port. Because of this, the first port you use must be of type 0. It
doesn't matter what type of port you end with; your goal is just to make the
bridge as strong as possible.

The strength of a bridge is the sum of the port types in each component.
For example, if your bridge is made of components 0/3, 3/7, and 7/4, your
bridge has a strength of 0+3 + 3+7 + 7+4 = 24.

For example, suppose you had the following components:

0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10

With them, you could make the following valid bridges:

  * 0/1
  * 0/1--10/1
  * 0/1--10/1--9/10
  * 0/2
  * 0/2--2/3
  * 0/2--2/3--3/4
  * 0/2--2/3--3/5
  * 0/2--2/2
  * 0/2--2/2--2/3
  * 0/2--2/2--2/3--3/4
  * 0/2--2/2--2/3--3/5

(Note how, as shown by 10/1, order of ports within a component doesn't matter.
However, you may only use each port on a component once.)

Of these bridges, the strongest one is 0/1--10/1--9/10; it has a strength of
0+1 + 1+10 + 10+9 = 31.

What is the strength of the strongest bridge you can make with the components
you have available?

Your puzzle answer was 1695.


--- Part Two ---

The bridge you've built isn't long enough; you can't jump the rest of the way.

In the example above, there are two longest bridges:

0/2--2/2--2/3--3/4
0/2--2/2--2/3--3/5

Of them, the one which uses the 3/5 component is stronger;
its strength is 0+2 + 2+2 + 2+3 + 3+5 = 19.

What is the strength of the longest bridge you can make?
If you can make multiple bridges of the longest length, pick the strongest one.

Your puzzle answer was 1673.
"""

def filter_components(components, port):
    """Return all components which have the specified port."""
    filtered_components = [component for component in components
        if component[0] == port or component[1] == port]
    return filtered_components

def calculate_strength(bridge):
    """Return the strength of the given bridge."""
    return sum([port_a + port_b for (port_a, port_b) in bridge])

def extend_bridge(bridge, components, completed_bridges, verbose=False):
    """Extend the given bridge as far as possible with the given components."""
    target_port = bridge[-1][-1]
    candidate_components = filter_components(components, target_port)

    if verbose:
        print(f"\nComponents: {components}")
        print(f"Target: {target_port}")
        print(f"Candidates: {candidate_components}")
        print(f"{calculate_strength(bridge)} {bridge}")

    completed_bridges.append(bridge)

    for candidate in candidate_components:
        remaining_components = components.copy()
        remaining_components.remove(candidate)

        candidate_bridge = bridge.copy()
        if candidate[0] == target_port:
            candidate_bridge.append(candidate)
        else:
            candidate_bridge.append((candidate[1], candidate[0]))

        extend_bridge(candidate_bridge, remaining_components,
                      completed_bridges)

def build_bridges(components, verbose=False):
    """Create a bridge as strong as possible."""
    completed_bridges = []
    start_port = 0
    for start_component in filter_components(components, start_port):
        if verbose:
            print("Start component:", start_component)

        if start_component[0] == start_port:
            bridge = [start_component]
        else:
            bridge = [(start_component[1], start_component[0])]

        remaining_components = components.copy()
        remaining_components.remove(start_component)
        bridge = bridge.copy()
        extend_bridge(bridge, remaining_components, completed_bridges)

    return completed_bridges

def find_strongest_bridge(components):
    """Return the strongest bridge from the given components."""
    bridges = build_bridges(components)
    return max([(bridge, calculate_strength(bridge)) for bridge in bridges],
               key=lambda bridge: bridge[1])

def find_longest_bridge(components):
    """Return the longest (and strongest) bridge from the given components."""
    bridges = build_bridges(components)
    max_bridge_length = max([len(bridge) for bridge in bridges])
    longest_bridges = [(bridge, calculate_strength(bridge))
                       for bridge in bridges
                       if len(bridge) == max_bridge_length]
    return max(longest_bridges, key=lambda bridge: bridge[1])

def main():
    components = []
    filename = 'day_24_input.txt'
    with open(filename, 'r') as input_file:
    	components = [tuple(each.split("/"))
                      for each in input_file.read().splitlines()]
    components = [(int(a), int(b)) for a, b in components]

    print("Strongest bridge:", find_strongest_bridge(components)[1])
    print("Longest (and strongest) bridge:", find_longest_bridge(components)[1])

if __name__ == '__main__':
    main()
