import doctest
from collections import defaultdict
from functools import cmp_to_key


def precedence_comparator(must_precede):
    """
    >>> sorted([1, 2], key=precedence_comparator({1: {2}}))
    [2, 1]
    >>> sorted([1, 2], key=precedence_comparator({2: {1}}))
    [1, 2]
    """

    def compare(a, b):
        if b in must_precede.get(a, []):
            return 1
        if a in must_precede.get(b, []):
            return -1
        return 0

    return cmp_to_key(compare)


def main():
    part1 = 0
    part2 = 0

    must_precede = defaultdict(set)
    updates = []

    with open("day5_input.txt") as f:
        for line in f:
            line = line.strip()
            if "|" in line:
                l, r = line.split("|")
                must_precede[r].add(l)
            elif line:
                updates.append(line.split(","))

    by_precedence = precedence_comparator(must_precede)

    for update in updates:
        sorted_update = sorted(update, key=by_precedence)

        if update == sorted_update:
            middle = update[len(update) // 2]
            part1 += int(middle)
        else:
            middle = sorted_update[len(sorted_update) // 2]
            part2 += int(middle)

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
