import doctest
import re


def main():
    whitespace = re.compile(" +")

    with open('day6_input.txt') as f:
        times = [int(s) for s in whitespace.split(f.readline().split(":")[1].strip())]
        distances = [int(s) for s in whitespace.split(f.readline().split(":")[1].strip())]

    part1 = 1
    for race in range(len(times)):
        time = times[race]
        distance = distances[race]
        moe = 0
        for i in range(1, time):
            speed = i
            distance_i = speed * (time - i)
            if distance_i > distance:
                moe += 1
            elif moe > 0:
                break
        # print(f"race {race}: time={time} distance={distance} moe={moe}")
        part1 *= moe

    print(f"Part 1: {part1}")


if __name__ == "__main__":
    doctest.testmod()
    main()
