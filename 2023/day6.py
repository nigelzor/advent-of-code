import doctest
import re


def margin(time, distance):
    m = 0
    for i in range(1, time):
        speed = i
        distance_i = speed * (time - i)
        if distance_i > distance:
            m += 1
        elif m > 0:
            break
    return m


def main():
    whitespace = re.compile(" +")

    with open('day6_input.txt') as f:
        time_line = f.readline().split(":")[1].strip()
        distance_line = f.readline().split(":")[1].strip()

        races = zip(
            (int(s) for s in whitespace.split(time_line)),
            (int(s) for s in whitespace.split(distance_line))
        )

        time_2 = int(time_line.replace(" ", ""))
        distance_2 = int(distance_line.replace(" ", ""))

    part1 = 1
    for (time, distance) in races:
        part1 *= margin(time, distance)
    print(f"Part 1: {part1}")

    part2 = margin(time_2, distance_2)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
