import doctest
import re


def main():
    part1 = 0
    part2 = 0

    instruction = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")
    enabled = True

    with open("day3_input.txt") as f:
        for line in f:
            for match in instruction.finditer(line):
                if match[0] == "do()":
                    enabled = True
                elif match[0] == "don't()":
                    enabled = False
                else:
                    product = int(match[1]) * int(match[2])
                    part1 += product
                    if enabled:
                        part2 += product

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
