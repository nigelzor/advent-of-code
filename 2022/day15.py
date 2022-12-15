import doctest
import re
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def manhattan(a: Point, b: Point):
    return abs(a.x - b.x) + abs(a.y - b.y)


def range_union(self: range, other: range):
    """
    >>> range_union(range(0, 2), range(1, 3))
    range(0, 3)
    >>> range_union(range(0, 2), range(2, 4))
    range(0, 4)
    >>> range_union(range(0, 1), range(2, 3))
    """
    # overlapping ranges
    if other.start in self:
        if other.stop > self.stop:
            return range(self.start, other.stop)
        return self
    if self.start in other:
        if self.stop > other.stop:
            return range(other.start, self.stop)
        return other
    # adjoining ranges
    if other.start == self.stop:
        return range(self.start, other.stop)
    if self.start == other.stop:
        return range(other.start, self.stop)
    # disjoint
    return None


def append_range(ranges: List[range], new_range: range):
    """
    >>> append_range(append_range([], range(0, 1)), range(1, 2))
    [range(0, 2)]
    """
    for r in ranges:
        u = range_union(r, new_range)
        if u:
            if u != r:
                ranges.remove(r)
                append_range(ranges, u)
            break
    else:
        ranges.append(new_range)
    return ranges


def main():
    sensors = dict()
    beacons = dict()

    p = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    with open('day15_input.txt') as f:
        for line in f:
            match = p.match(line)
            if match:
                [sx, sy, bx, by] = [int(v) for v in match.groups()]
                sensor = Point(sx, sy)
                beacon = Point(bx, by)
                distance = manhattan(sensor, beacon)
                sensors[sensor] = distance
                beacons[beacon] = True

    def collect_ranges(y):
        ranges = []
        for sensor, strength in sensors.items():
            # print('sensor at', sensor, 'with strength', strength)
            rows_away = abs(y - sensor.y)
            # print(rows_away, 'rows away; effective strength', strength - rows_away)
            strength -= rows_away
            if strength >= 0:
                contribution = range(sensor.x - strength, sensor.x + strength + 1)
                append_range(ranges, contribution)
                # print('+', contribution, '=', ranges.ranges)
        return ranges

    # In the row where y=2000000, how many positions cannot contain a beacon?
    row = 2000000
    print(sum(len(r) for r in collect_ranges(row)) - sum(1 for b in beacons if b.y == row))  # 4665948

    # Find the only possible position for the distress beacon. What is its tuning frequency?
    limit = 4000000
    xs = range(0, limit + 1)
    ys = range(0, limit + 1)
    for y in ys:
        ranges = collect_ranges(y)
        for r in ranges:
            if range_union(r, xs) != r:
                x = min(ranges, key=lambda r: r.start).stop
                print(4000000 * x + y)  # 13543690671045
                return


if __name__ == "__main__":
    doctest.testmod()
    main()
