import doctest


def simplify_patterns(available):
    """
    >>> simplify_patterns({"b", "bb"})
    {'b'}
    """
    return {p for p in available if not pattern_possible(p, available - {p})}


def pattern_possible(pattern, available):
    if pattern == "":
        return True
    for a in available:
        if pattern.startswith(a):
            if pattern_possible(pattern[len(a) :], available):
                return True
    return False


def main():
    with open("day19_input.txt") as f:
        lines = iter(line.strip() for line in f)

        available = set(next(lines).split(", "))
        next(lines)
        desired = list(lines)

    unique_patterns = simplify_patterns(available)
    part1 = sum(1 for pattern in desired if pattern_possible(pattern, unique_patterns))

    print(f"part 1: {part1}")


if __name__ == "__main__":
    doctest.testmod()
    main()
