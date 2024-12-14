import doctest
import re
from z3 import Solver, Int


button_pattern = re.compile(r"Button .: X\+(\d+), Y\+(\d+)")
prize_pattern = re.compile(r"Prize: X=(\d+), Y=(\d+)")


def solve_part1(ax, ay, bx, by, x, y):
    s = Solver()
    a = Int("a")
    s.add(a >= 0, a <= 100)
    b = Int("b")
    s.add(b >= 0, b <= 100)
    s.add(a * ax + b * bx == x)
    s.add(a * ay + b * by == y)
    if s.check().r == 1:
        m = s.model()
        return 3 * m[a].as_long() + m[b].as_long()


def solve_part2(ax, ay, bx, by, x, y):
    x += 10000000000000
    y += 10000000000000

    s = Solver()
    a = Int("a")
    s.add(a >= 0)
    b = Int("b")
    s.add(b >= 0)
    s.add(a * ax + b * bx == x)
    s.add(a * ay + b * by == y)
    if s.check().r == 1:
        m = s.model()
        return 3 * m[a].as_long() + m[b].as_long()


def main():
    part1 = 0
    part2 = 0

    with open("day13_input.txt") as f:
        lines = filter(None, (l.strip() for l in f.readlines()))

        try:
            while True:
                ax, ay = [int(v) for v in button_pattern.match(next(lines)).groups()]
                bx, by = [int(v) for v in button_pattern.match(next(lines)).groups()]
                x, y = [int(v) for v in prize_pattern.match(next(lines)).groups()]

                part1 += solve_part1(ax, ay, bx, by, x, y) or 0
                part2 += solve_part2(ax, ay, bx, by, x, y) or 0
        except StopIteration:
            pass

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
