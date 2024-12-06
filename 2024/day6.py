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


def main():
    map = dict()

    with open("day6_input.txt") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line):
                map[Point(x, y)] = c
                if c == "^":
                    guard_position = Point(x, y)

    guard_direction = N

    visited = set()
    try:
        while True:
            if map[guard_position + guard_direction] == "#":
                guard_direction = turn_right[guard_direction]
            else:
                guard_position += guard_direction

            visited.add(guard_position)
    except KeyError:
        pass  # walked out of bounds

    print(f"part 1: {len(visited)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
