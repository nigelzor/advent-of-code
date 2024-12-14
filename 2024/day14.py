import doctest
import re

robot_pattern = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")


def product(xs):
    r = 1
    for x in xs:
        r *= x
    return r


def main():
    robots = []

    with open("day14_input.txt") as f:
        for line in f:
            px, py, vx, vy = [int(v) for v in robot_pattern.match(line).groups()]
            robots.append(((px, py), (vx, vy)))

    width = 101
    height = 103

    def tick():
        for i, (p, v) in enumerate(robots):
            px = (p[0] + v[0]) % width
            py = (p[1] + v[1]) % height
            robots[i] = ((px, py), v)

    def safety_factor():
        quadrants = [0, 0, 0, 0]

        for p, v in robots:
            if p[0] < width // 2 and p[1] < height // 2:
                quadrants[0] += 1
            elif p[0] > width // 2 and p[1] < height // 2:
                quadrants[1] += 1
            elif p[0] > width // 2 and p[1] > height // 2:
                quadrants[2] += 1
            elif p[0] < width // 2 and p[1] > height // 2:
                quadrants[3] += 1

        return product(quadrants)

    def print_room():
        occupied = {p for p, v in robots}
        for y in range(height + 1):
            for x in range(width + 1):
                print("#" if (x, y) in occupied else " ", end="")
            print()

    def has_horizontal_line():
        occupied = {p for p, v in robots}
        for y in range(height + 1):
            consecutive = 0
            for x in range(width + 1):
                if (x, y) in occupied:
                    consecutive += 1
                    if consecutive >= 10:
                        return True
                else:
                    consecutive = 0

    for i in range(1, 10000):
        tick()

        if i == 100:
            part1 = safety_factor()

        if has_horizontal_line():
            part2 = i
            print_room()
            break

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
