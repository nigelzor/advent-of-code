import doctest
from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int
    z: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)


DOWN = Point(0, 0, -1)


def to_range(a, b):
    """
    >>> list(to_range(1, 1))
    [1]
    >>> list(to_range(3, 1))
    [1, 2, 3]
    """
    lower = min(a, b)
    upper = max(a, b) + 1
    return range(lower, upper)


def range_intersect(a, b):
    """
    >>> range_intersect(range(0, 1), range(0, 2))
    range(0, 1)
    >>> range_intersect(range(0, 1), range(1, 2)) is None
    True
    """
    return range(max(a.start, b.start), min(a.stop, b.stop)) or None


@dataclass
class Brick:
    a: Point
    b: Point

    def min_z(self):
        return min(self.a.z, self.b.z)

    def max_z(self):
        return min(self.a.z, self.b.z)

    def move_down(self):
        self.a = self.a + DOWN
        self.b = self.b + DOWN

    def occupies(self, point: Point):
        def includes(a, b, p):
            lower = min(a, b)
            upper = max(a, b)
            return lower <= p <= upper

        return includes(self.a.x, self.b.x, point.x) and includes(self.a.y, self.b.y, point.y) and includes(self.a.z, self.b.z, point.z)

    def occupies_z(self, z):
        lower = min(self.a.z, self.b.z)
        upper = max(self.a.z, self.b.z)
        return lower <= z <= upper

    def contents(self):
        if self.a.x != self.b.x:
            return [Point(x, self.a.y, self.a.z) for x in to_range(self.a.x, self.b.x)]
        if self.a.y != self.b.y:
            return [Point(self.a.x, y, self.a.z) for y in to_range(self.a.y, self.b.y)]
        if self.a.z != self.b.z:
            return [Point(self.a.x, self.a.y, z) for z in to_range(self.a.z, self.b.z)]
        return [self.a]

    @cached_property
    def footprint(self):
        if self.a.x != self.b.x:
            return [Point(x, self.a.y, 0) for x in to_range(self.a.x, self.b.x)]
        if self.a.y != self.b.y:
            return [Point(self.a.x, y, 0) for y in to_range(self.a.y, self.b.y)]
        return [Point(self.a.x, self.a.y, 0)]

    def intersects(self, other):
        return any(self.occupies(p) for p in other.contents())

    def __hash__(self):
        return id(self)


def main():
    bricks = list()
    with open('day22_input.txt') as f:
        for i, line in enumerate(f):
            lhs, rhs = line.strip().split('~')
            # name = chr(ord('A') + i)
            bricks.append(Brick(Point(*[int(v) for v in lhs.split(',')]),
                                Point(*[int(v) for v in rhs.split(',')])))

    bricks.sort(key=lambda b: b.min_z())

    bricks_in_col = defaultdict(list)
    for brick in bricks:
        for p in brick.footprint:
            bricks_in_col[p].append(brick)

    def is_occupied(p, z):
        for brick in bricks_in_col[p]:
            if brick.occupies_z(z):
                return True
        return False

    def try_move_one_down():
        moved = False
        for brick in bricks:
            z = brick.min_z() - 1
            while z >= 1:
                blocked = any(is_occupied(p, z) for p in brick.footprint)
                if not blocked:
                    moved = True
                    brick.move_down()
                    z -= 1
                else:
                    break
        return moved

    while try_move_one_down():
        pass

    def bricks_below(brick):
        result = set()
        z = brick.min_z() - 1
        for p in brick.footprint:
            for brick in bricks_in_col[p]:
                if brick.occupies_z(z):
                    result.add(brick)
        return result

    def part1():
        pinned = set()
        for brick in bricks:
            below = bricks_below(brick)
            if len(below) < 2:
                for b in below:
                    pinned.add(b)
        return len(bricks) - len(pinned)

    print(f'Part 1: {part1()}')

    def part2():
        would_fall = defaultdict(list)

        for brick in bricks:
            if brick.min_z() > 1:
                below = frozenset(bricks_below(brick))
                would_fall[below].append(brick)

        total = 0
        for brick in bricks:
            falling = {brick}
            extended = True
            while extended:
                extended = False
                for ks, fs in would_fall.items():
                    if all(k in falling for k in ks):
                        for f in fs:
                            if f not in falling:
                                extended = True
                                falling.add(f)
            total += len(falling) - 1
        return total

    print(f'Part 2: {part2()}')


if __name__ == "__main__":
    doctest.testmod()
    main()
