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

turn_right = {N: E, E: S, S: W, W: N}


def simulate(map, position, direction):
    visited = set()
    try:
        while True:
            if map[position + direction] == "#":
                direction = turn_right[direction]
            else:
                position += direction

            if (position, direction) in visited:
                return "loop"

            visited.add((position, direction))
    except KeyError:  # walked out of bounds
        return {v[0] for v in visited}


def main():
    map = dict()

    with open("day6_input.txt") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line):
                map[Point(x, y)] = c
                if c == "^":
                    guard_position = Point(x, y)

    guard_direction = N

    visited = simulate(map, guard_position, guard_direction)
    part1 = len(visited)
    print(f"part 1: {part1}")

    part2 = 0
    for possible_obstacle in visited:
        new_map = {**map, possible_obstacle: "#"}
        if simulate(new_map, guard_position, guard_direction) == "loop":
            part2 += 1
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
