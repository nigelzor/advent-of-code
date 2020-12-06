import doctest


def main():
    part1 = []
    part2 = []
    with open('day6_input.txt') as f:
        any_answered = set()
        all_answered = None
        for line in f:
            parts = set(line.strip())
            if not parts:
                part1.append(any_answered)
                part2.append(all_answered)
                any_answered = set()
                all_answered = None
            else:
                any_answered |= parts
                if all_answered is None:
                    all_answered = parts
                else:
                    all_answered &= parts
        if any_answered:
            part1.append(any_answered)
            part2.append(all_answered)

    print(sum(len(g) for g in part1))
    print(sum(len(g) for g in part2))


if __name__ == "__main__":
    doctest.testmod()
    main()
