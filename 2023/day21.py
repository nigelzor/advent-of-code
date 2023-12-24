import doctest
from dataclasses import dataclass
from z3 import Solver, Int


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)


def manhattan(a: Point, b: Point):
    return abs(a.x - b.x) + abs(a.y - b.y)


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)


def main():
    plots = set()
    with open('day21_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                if c == '.':
                    plots.add(Point(x, y))
                if c == 'S':
                    plots.add(Point(x, y))
                    start = Point(x, y)

    width = max(p.x for p in plots) + 1
    height = max(p.y for p in plots) + 1

    def is_infinite_plot(p):
        return Point(p.x % width, p.y % height) in plots

    def part1():
        occupied = {start}
        for _ in range(64):
            result = set()
            for o in occupied:
                for d in [N, E, S, W]:
                    result.add(o + d)
            occupied = result & plots
            # print(len(occupied))
        return len(occupied)

    print(f'Part 1: {part1()}')

    def part2_slow():
        edge = {start}
        visited = set()
        enclosed = [0, 0]
        target = 26501365

        for i in range(1, target):
            next_edge = set()
            for o in edge:
                for d in [N, E, S, W]:
                    n = o + d
                    if is_infinite_plot(n) and n not in visited:
                        next_edge.add(n)
            added = 0
            for n in next_edge:
                visited.add(n)
                added += 1
            enclosed[i % 2] += added
            edge = next_edge

            if i % width == target % width:
                yield enclosed[i % 2]

    def part2():
        sequence = part2_slow()
        zero = next(sequence)
        one = next(sequence)
        two = next(sequence)
        a = Int('a')
        b = Int('b')
        c = Int('c')
        s = Solver()
        s.add(zero == a * pow(0, 2) + b * 0 + c)
        s.add(one == a * pow(1, 2) + b * 1 + c)
        s.add(two == a * pow(2, 2) + b * 2 + c)
        s.check()
        model = s.model()
        n = (26501365 // width)
        return model[a].as_long() * pow(n, 2) + model[b].as_long() * n + model[c].as_long()

    print(f'Part 2: {part2()}')


if __name__ == "__main__":
    doctest.testmod()
    main()
