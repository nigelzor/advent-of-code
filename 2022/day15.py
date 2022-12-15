import doctest
import re


def print_grid(grid):
    minx = min(int(c.real) for c in grid.keys())
    maxx = max(int(c.real) for c in grid.keys())
    miny = min(int(c.imag) for c in grid.keys())
    maxy = max(int(c.imag) for c in grid.keys())

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            print(grid.get(x + y * 1j, '.'), end='')
        print('')


def manhattan(a, b):
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))


def diamond(start, distance):
    for y in range(-distance, distance + 1):
        for x in range(-(distance - abs(y)), (distance - abs(y)) + 1):
            yield start + x + y * 1j


def main():
    sensors = dict()
    beacons = dict()

    p = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    with open('day15_input.txt') as f:
        for line in f:
            match = p.match(line)
            if match:
                [sx, sy, bx, by] = [int(v) for v in match.groups()]
                sensor = sx + sy * 1j
                beacon = bx + by * 1j
                distance = manhattan(sensor, beacon)
                sensors[sensor] = distance
                beacons[beacon] = True

    minx = int(min(k.real - v for k, v in sensors.items()))
    maxx = int(max(k.real + v for k, v in sensors.items()))

    def in_range_of_sensor(pos):
        return any(manhattan(pos, k) <= v for k, v in sensors.items())

    def not_a_beacon(pos):
        return pos not in beacons and in_range_of_sensor(pos)

    y = 2000000
    print(sum(1 for x in range(minx, maxx + 1) if not_a_beacon(x + y * 1j)))


if __name__ == "__main__":
    doctest.testmod()
    main()
