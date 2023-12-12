import doctest
import re
from collections import defaultdict


def to_length_map(items):
    result = defaultdict(int)
    for item in items:
        result[len(item)] += 1
    return result


def possible_placements(n: int, pattern: str):
    # """
    # >>> possible_placements(1, "?")
    # ['#']
    # >>> possible_placements(1, '??')
    # ['#.', '.#']
    # >>> possible_placements(2, '???')
    # ['##.', '.##']
    # >>> possible_placements(1, '???')
    # ['#.', '.#.', '..#']
    # >>> possible_placements(1, '????')
    # ['#.', '.#.', '..#.', '...#']
    # >>> possible_placements(1, '?#?')
    # ['.#.']
    # >>> possible_placements(2, '?#?')
    # ['##.', '.##']
    # >>> possible_placements(1, '?#??')
    # ['.#.']
    # >>> possible_placements(2, '?#??')
    # ['##.', '.##.']
    # >>> possible_placements(2, "?")
    # []
    # """
    p = re.compile(f"(?<!#)(?=[#?]{{{n}}}(?!#))")
    for m in p.finditer(pattern):
        start, end = m.span()
        before = pattern[:max(0, start - 1)]
        after = pattern[start + n + 1:]
        yield (before, after)


def partition_groups(groups):
    """
    >>> partition_groups([1, 2, 3])
    ([1, 2], 3, [])
    >>> partition_groups([1])
    ([], 1, [])
    >>> partition_groups([1, 4, 2, 4, 3, 4])
    ([1, 4, 2], 4, [3, 4])
    >>> partition_groups([4, 4])
    ([4], 4, [])
    """
    longest = max(groups)
    indexes = [(i, c) for i, c in enumerate(groups) if c == longest]
    middle = indexes[len(indexes) // 2][0]
    return groups[:middle], longest, groups[middle + 1:]


def count_placements(pattern, groups):
    """
    >>> count_placements("", [])
    1
    >>> count_placements(".", [])
    1
    >>> count_placements("#", [])
    0
    >>> count_placements("#", [1])
    1
    >>> count_placements("?", [1])
    1
    >>> count_placements("??", [1])
    2
    >>> count_placements("???", [1])
    3
    >>> count_placements("???", [1, 1])
    1
    """

    if len(groups) == 0:
        if '#' in pattern:
            return 0
        return 1

    pattern = pattern.strip('.')

    if pattern == '':
        return 0

    g_before, g, g_after = partition_groups(groups)
    total = 0
    for (before, after) in possible_placements(g, pattern):
        total += count_placements(before, g_before) * count_placements(after, g_after)

    return total


def main():
    part1 = 0
    part2 = 0

    with open('day12_input.txt') as f:
        for line in f:
            pattern, groups = line.strip().split(' ')
            groups = [int(r) for r in groups.split(',')]
            print(pattern, groups)
            part1 += count_placements(pattern, groups)

            expanded_pattern = '?'.join([pattern] * 5)
            part2 += count_placements(expanded_pattern, groups * 5)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
