import doctest
import re
from typing import Dict, List


def parse_sample(s: str) -> Dict[str, int]:
    """
    >>> parse_sample("11 red, 8 green, 9 blue")
    {'red': 11, 'green': 8, 'blue': 9}
    """
    result = dict()
    for part in s.split(", "):
        n, c = part.split(" ")
        result[c] = int(n)
    return result


def possible(s: Dict[str, int], allowed: Dict[str, int]):
    for k, v in s.items():
        if v > allowed.get(k, 0):
            return False
    return True


def minimum(samples: List[Dict[str, int]]) -> Dict[str, int]:
    result = dict()
    for s in samples:
        for k, v in s.items():
            result[k] = max(result.get(k, 0), v)
    return result


def power(samples):
    m = minimum(samples)
    return m.get('red', 0) * m.get('green', 0) * m.get('blue', 0)


def main():
    line_pattern = re.compile(r"Game (\d+): (.*)")

    part1 = {'red': 12, 'green': 13, 'blue': 14}
    part1_total = 0

    part2_total = 0

    with open('day2_input.txt') as f:
        for line in f:
            match = line_pattern.match(line)
            game = int(match.group(1))
            samples = [parse_sample(s) for s in match.group(2).split('; ')]
            if all(possible(s, part1) for s in samples):
                part1_total += game
            part2_total += power(samples)

    print(part1_total)
    print(part2_total)


if __name__ == "__main__":
    doctest.testmod()
    main()
