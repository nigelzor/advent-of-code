import doctest
import re

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def main():
    total = 0
    p = re.compile("(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))")
    with open('day1_input.txt') as f:
        for line in f:
            line = line.strip()
            first = None
            last = None
            for match in p.finditer(line):
                c = match.group(1)
                c = numbers.get(c, c)
                if first is None:
                    first = c
                last = c
            calibration = int(first + last)
            # print(line, first, last, calibration)
            total += calibration
    print(total)


if __name__ == "__main__":
    doctest.testmod()
    main()
