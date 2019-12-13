import doctest
import re
from copy import deepcopy

import math
from itertools import combinations

p = re.compile(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>')


class Moon:
    def __init__(self, position, velocity=(0, 0, 0)):
        self.position = list(position)
        self.velocity = list(velocity)

    def __str__(self):
        return 'Moon[position={}, velocity={}]'.format(self.position, self.velocity)


def main():
    moons = []
    with open('day12_input.txt') as f:
    # with open('day12_sample.txt') as f:
        for line in f:
            x, y, z = [int(v) for v in p.match(line).groups()]
            moons.append(Moon((x, y, z)))

    initial_moons = deepcopy(moons)

    def advance():
        for a, b in combinations(moons, 2):
            for i in range(3):
                if a.position[i] > b.position[i]:
                    a.velocity[i] -= 1
                    b.velocity[i] += 1
                elif a.position[i] < b.position[i]:
                    a.velocity[i] += 1
                    b.velocity[i] -= 1

        for moon in moons:
            for i in range(3):
                moon.position[i] += moon.velocity[i]

    def print_moons(s):
        print('Step {}:'.format(s))
        for moon in moons:
            print(moon)

    def total_energy(moon):
        pe = sum(abs(x) for x in moon.position)
        ke = sum(abs(x) for x in moon.velocity)
        return pe * ke

    s = 0
    cycles = [None, None, None]
    print_moons(s)
    while any(c is None for c in cycles):
        advance()
        s += 1

        if s == 1000:
            print('s={}, total_energy: {}'.format(s, sum(total_energy(m) for m in moons)))

        for d in range(3):
            if cycles[d] is None:
                if all(moons[m].position[d] == initial_moons[m].position[d]
                       and moons[m].velocity[d] == initial_moons[m].velocity[d] for m in range(len(moons))):
                    cycles[d] = s

    def lcm(a, b):
        return a // math.gcd(a, b) * b

    print(cycles)
    print(lcm(lcm(cycles[0], cycles[1]), cycles[2]))


if __name__ == "__main__":
    doctest.testmod()
    main()
