import doctest
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)

DIRECTIONS = {
    "^": N,
    "v": S,
    ">": E,
    "<": W,
}


def main():
    position = Point(0, 0)
    warehouse = {}
    instructions = ""

    with open("day15_input.txt") as f:
        lines = iter(f)
        for y, line in enumerate(lines):
            line = line.strip()
            if not line:
                break
            for x, c in enumerate(line):
                point = Point(x, y)
                if c in ("#", "O", "@"):
                    if c == "@":
                        position = point
                    warehouse[point] = c

        for line in lines:
            instructions += line.strip()

    def try_move(p, d):
        into = warehouse.get(p + d)
        if into == "#":
            return False
        if (into is None) or (into == "O" and try_move(p + d, d)):
            if p in warehouse:
                warehouse[p + d] = warehouse[p]
                del warehouse[p]
            return True
        return False

    def gps_total():
        total = 0
        for k, v in warehouse.items():
            if v == "O":
                total += k.y * 100 + k.x
        return total

    for n, i in enumerate(instructions, 1):
        direction = DIRECTIONS[i]
        if try_move(position, direction):
            position += direction

    print(f"part 1: {gps_total()}")
    # print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
