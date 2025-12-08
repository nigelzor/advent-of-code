import doctest


def digits(s):
    return [int(c) for c in s]


def max_joltage(bank, n=2):
    """
    >>> max_joltage(digits("987654321111111"))
    98
    >>> max_joltage(digits("234234234234278"), 12)
    434234234278
    """
    selected = []
    left = 0
    for _ in range(n):
        right = n - len(selected) - 1
        usable = bank[left:-right] if right else bank[left:]
        best = max(usable)
        best_index = usable.index(best)
        selected.append(best)
        left += best_index + 1

    result = 0
    for d in selected:
        result = 10 * result + d
    return result


def main():
    banks = []
    with open("day3_input.txt") as f:
        for line in f:
            banks.append(digits(line.strip()))

    part1 = 0
    part2 = 0

    for bank in banks:
        part1 += max_joltage(bank, 2)
        part2 += max_joltage(bank, 12)

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
