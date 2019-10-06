from collections import Counter, namedtuple
import numpy as np

"""
Advent of Code 2017

https://adventofcode.com/2017/day/20

--- Day 20: Particle Swarm ---

Suddenly, the GPU contacts you, asking for help. Someone has asked it to
simulate too many particles, and it won't be able to finish them all in time
to render the next frame at this rate.

It transmits to you a buffer (your puzzle input) listing each particle
in order (starting with particle 0, then particle 1, particle 2, and so on).
For each particle, it provides the X, Y, and Z coordinates for the particle's
position (p), velocity (v), and acceleration (a), each in the format <X,Y,Z>.

Each tick, all particles are updated simultaneously. A particle's properties
are updated in the following order:

  * Increase the X velocity by the X acceleration.
  * Increase the Y velocity by the Y acceleration.
  * Increase the Z velocity by the Z acceleration.
  * Increase the X position by the X velocity.
  * Increase the Y position by the Y velocity.
  * Increase the Z position by the Z velocity.

Because of seemingly tenuous rationale involving z-buffering, the GPU would
like to know which particle will stay closest to position <0,0,0> in the long
term. Measure this using the Manhattan distance, which in this situation is
simply the sum of the absolute values of a particle's X, Y, and Z position.

For example, suppose you are only given two particles, both of which stay
entirely on the X-axis (for simplicity). Drawing the current states of
particles 0 and 1 (in that order) with an adjacent a number line and diagram
of current X positions (marked in parentheses), the following would take
place:

p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>                         (0)(1)

p=< 4,0,0>, v=< 1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=< 2,0,0>, v=<-2,0,0>, a=<-2,0,0>                      (1)   (0)

p=< 4,0,0>, v=< 0,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=<-2,0,0>, v=<-4,0,0>, a=<-2,0,0>          (1)               (0)

p=< 3,0,0>, v=<-1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=<-8,0,0>, v=<-6,0,0>, a=<-2,0,0>                         (0)

At this point, particle 1 will never be closer to <0,0,0> than particle 0, and so, in the long run, particle 0 will stay closest.

Which particle will stay closest to position <0,0,0> in the long term?

Your puzzle answer was 308.


--- Part Two ---

To simplify the problem further, the GPU would like to remove any particles
that collide. Particles collide if their positions ever exactly match.
Because particles are updated simultaneously, more than two particles can
collide at the same time and place. Once particles collide, they are removed
and cannot collide with anything else after that tick.

For example:

p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>    (0)   (1)   (2)            (3)
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>

p=<-3,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=<-1,0,0>, v=< 1,0,0>, a=< 0,0,0>             (0)(1)(2)      (3)
p=< 2,0,0>, v=<-1,0,0>, a=< 0,0,0>

p=< 0,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=< 0,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=< 0,0,0>, v=< 1,0,0>, a=< 0,0,0>                       X (3)
p=< 1,0,0>, v=<-1,0,0>, a=< 0,0,0>

------destroyed by collision------
------destroyed by collision------    -6 -5 -4 -3 -2 -1  0  1  2  3
------destroyed by collision------                      (3)
p=< 0,0,0>, v=<-1,0,0>, a=< 0,0,0>

In this example, particles 0, 1, and 2 are simultaneously destroyed at the
time and place marked X. On the next tick, particle 3 passes through unharmed.

How many particles are left after all collisions are resolved?

Your puzzle answer was 504.
"""

def as_vector(values):
    """Return p, v, a as vectors."""
    return np.array([int(value) for value in values[3:-1].split(",")])

def parse_particles_buffer(particles_buffer):
    """Return a list of particles from a particles buffer."""
    Particle = namedtuple('Particle', ['p', 'v', 'a'])
    particles = []
    for particle in particles_buffer:
        p, v, a = particle.split(", ")
        particles.append(Particle(p=as_vector(p),
                                  v=as_vector(v),
                                  a=as_vector(a)))
    return particles

def calculate_particles_positions(particles, iterations=1_000, verbose=False):
    """Calculate the position of the particles."""
    for i in range(iterations):
        for j, particle in enumerate(particles):
            particle = particle._replace(v=particle.v + particle.a)
            particle = particle._replace(p=particle.p + particle.v)
            particles[j] = particle

        if verbose:
            print(f"Particles: {particles}")
            print(f"Distances: {distance_from_origin(particles)}")

    return particles

def calculate_particle_positions_with_collisions(particles, iterations=1_000):
    """Calculate the position of particles and resolve collisions."""
    for i in range(iterations):
        calculate_particles_positions(particles, iterations=1)
        particle_positions = [tuple(particle.p) for particle in particles]
        positions_counter = Counter(particle_positions)

        collisions = [position for position, count in positions_counter.items()
                               if count > 1]
        particles = [particle for particle in particles
                              if not tuple(particle.p) in collisions]

    return particles

def distance_from_origin(particles):
    """Return the Manhattan distance of each particle from the origin."""
    distances = [np.sum(np.abs(particle.p)) for particle in particles]
    return distances

def find_closest_particle(particles_buffer):
    """Find the closest particle in a particle buffer."""
    particles = parse_particles_buffer(particles_buffer)
    particles = calculate_particles_positions(particles)
    distances = distance_from_origin(particles)
    closest_particle = np.argmin(distances)
    return closest_particle

def count_remaining_particles(particles_buffer):
    """Return the number of particles remaining after collisions."""
    particles = parse_particles_buffer(particles_buffer)
    particles = calculate_particle_positions_with_collisions(particles)
    return len(particles)

def main():
    particles_buffer = None
    with open("day_20_particle_buffer.txt", 'r') as buffer_file:
        particles_buffer = buffer_file.read().splitlines()

    print(f"Closest particle: {find_closest_particle(particles_buffer)}")
    print(f"Remaining particles: {count_remaining_particles(particles_buffer)}")

if __name__ == '__main__':
    main()
