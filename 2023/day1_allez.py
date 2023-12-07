import re
from typing import List


def to_numeric(match: re.Match) -> str:
    return {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }.get(match.group(1), match.group(1))


def to_matches(line: str) -> List[str]:
    return list(map(to_numeric, re.finditer(r"(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))", line)))


def calibration(matches: List[str]) -> int:
    return int(matches[0] + matches[-1])


print(sum(map(calibration, map(to_matches, open('day1_input.txt')))))
