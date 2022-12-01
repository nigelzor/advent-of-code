import doctest

def main():
    elves = []
    total = 0
    with open('day1_input.txt') as f:
        for line in f:
            line = line.strip()
            if line:
                total += int(line)
            else:
                elves.append(total)
                total = 0
        if total:
            elves.append(total)

    print(max(elves))
    top = sorted(elves)[-3:]
    print(sum(top))


if __name__ == "__main__":
    doctest.testmod()
    main()
