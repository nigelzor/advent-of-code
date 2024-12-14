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

    for _ in range(100):

        tick()

    part1 = safety_factor()
    part2 = 0

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
