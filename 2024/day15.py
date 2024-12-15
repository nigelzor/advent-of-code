import doctest
from dataclasses import dataclass
from operator import attrgetter


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)


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


def part1(warehouse, position, instructions):
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

    for n, i in enumerate(instructions, 1):
        direction = DIRECTIONS[i]
        if try_move(position, direction):
            position += direction

    return sum(k.y * 100 + k.x for k, v in warehouse.items() if v == "O")


def part2(warehouse, position, instructions):
    def collect_move(p, d, pending):
        into = warehouse.get(p + d)
        if into == "#":
            return False
        if into is None:
            pending.add(p)
            return True
        if into == "[":
            if collect_move(p + d, d, pending) and (
                d in (E, W) or collect_move(p + d + E, d, pending)
            ):
                pending.add(p)
                return True
        if into == "]":
            if collect_move(p + d, d, pending) and (
                d in (E, W) or collect_move(p + d + W, d, pending)
            ):
                pending.add(p)
                return True
        return False

    for n, i in enumerate(instructions, 1):
        direction = DIRECTIONS[i]
        to_move = set()
        if collect_move(position, direction, to_move):
            sorted_to_move = sorted(
                to_move,
                key=attrgetter("x" if direction in (E, W) else "y"),
                reverse=direction in (S, E),
            )
            for p in sorted_to_move:
                warehouse[p + direction] = warehouse[p]
                del warehouse[p]
            position += direction

    return sum(k.y * 100 + k.x for k, v in warehouse.items() if v == "[")


def print_warehouse(warehouse):
    height = max(k.y for k in warehouse)
    width = max(k.x for k in warehouse)
    for y in range(height + 1):
        for x in range(width + 1):
            print(warehouse.get(Point(x, y), " "), end="")
        print()


def main():
    warehouse = {}
    position = Point(0, 0)
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

    scale = Point(2, 1)
    wide_warehouse = {}
    for k, v in warehouse.items():
        if v == "#":
            wide_warehouse[k * scale] = "#"
            wide_warehouse[k * scale + E] = "#"
        elif v == "O":
            wide_warehouse[k * scale] = "["
            wide_warehouse[k * scale + E] = "]"
        elif v == "@":
            wide_warehouse[k * scale] = "@"
    wide_position = position * scale

    print(f"part 1: {part1(warehouse, position, instructions)}")
    print(f"part 2: {part2(wide_warehouse, wide_position, instructions)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
