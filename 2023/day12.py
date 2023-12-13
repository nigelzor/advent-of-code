import doctest
import functools


def possible_placements(n: int, pattern: str):
    """
    >>> list(possible_placements(1, "?"))
    [0]
    >>> list(possible_placements(1, '??'))
    [0, 1]
    >>> list(possible_placements(2, '???'))
    [0, 1]
    >>> list(possible_placements(1, '???'))
    [0, 1, 2]
    >>> list(possible_placements(1, '????'))
    [0, 1, 2, 3]
    >>> list(possible_placements(1, '?#?'))
    [1]
    >>> list(possible_placements(2, '?#?'))
    [0, 1]
    >>> list(possible_placements(1, '?#??'))
    [1, 3]
    >>> list(possible_placements(2, '?#??'))
    [0, 1]
    >>> list(possible_placements(2, "?"))
    []
    """
    last = len(pattern) - n
    start = 0
    while start <= last:
        if start != 0 and pattern[start - 1] == '#':
            start += 1
            continue
        if start != last and pattern[start + n] == '#':
            start += 1
            continue
        last_dot = pattern.rfind('.', start, start + n)
        if last_dot >= 0:
            start = last_dot + 1
            continue
        yield start
        start += 1


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
    >>> count_placements("", ())
    1
    >>> count_placements(".", ())
    1
    >>> count_placements("#", ())
    0
    >>> count_placements("#", (1,))
    1
    >>> count_placements("?", (1,))
    1
    >>> count_placements("??", (1,))
    2
    >>> count_placements("???", (1,))
    3
    >>> count_placements("???", (1, 1))
    1
    """
    if len(groups) == 0:
        if '#' in pattern:
            return 0
        return 1

    pattern = pattern.strip('.')

    if pattern == '':
        return 0

    return count_placements_internal(pattern, groups)


@functools.lru_cache(4096)
def count_placements_internal(pattern, groups):
    if pattern.startswith('#'):
        g = groups[0]
        g_before = groups[:0]
        g_after = groups[1:]

        if g > len(pattern):
            return 0
        if any(c == '.' for c in pattern[:g]):
            return 0
        if len(pattern) > g and pattern[g] == '#':
            return 0
        placements = [0]
    elif pattern.endswith('#'):
        g = groups[-1]
        g_before = groups[:-1]
        g_after = groups[:0]

        if g > len(pattern):
            return 0
        if any(c == '.' for c in pattern[-g:]):
            return 0
        if len(pattern) > g and pattern[-(g + 1)] == '#':
            return 0
        placements = [len(pattern) - g]
    else:
        g_before, g, g_after = partition_groups(groups)
        placements = possible_placements(g, pattern)

    total = 0
    for start in placements:
        before = pattern[:max(0, start - 1)]
        after = pattern[start + g + 1:]
        total += count_placements(before, g_before) * count_placements(after, g_after)

    return total


def main():
    part1 = 0
    part2 = 0

    inputs = []
    with open('day12_input.txt') as f:
        for line in f:
            pattern, groups = line.strip().split(' ')
            groups = tuple(int(r) for r in groups.split(','))
            inputs.append((pattern, groups))

    for pattern, groups in inputs:
        # print(pattern, groups)
        part1 += count_placements(pattern, groups)

        expanded_pattern = '?'.join([pattern] * 5)
        part2 += count_placements(expanded_pattern, groups * 5)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
