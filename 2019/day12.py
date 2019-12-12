import doctest
import re
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

    for s in range(1, 1001):
        advance()
        print_moons(s)

    print('s={}, total_energy: {}'.format(s, sum(total_energy(m) for m in moons)))


if __name__ == "__main__":
    doctest.testmod()
    main()
