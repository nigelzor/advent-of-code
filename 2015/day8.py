import doctest


def main():
    def expand(c):
        if c == '"':
            return 2
        if c == "\\":
            return 2
        return 1

    c = 0
    m = 0
    e = 0
    with open('day8_input.txt') as f:
        for line in f:
            line = line.rstrip()
            c += len(line)
            m += len(eval(line))
            e += sum(expand(c) for c in line) + 2

    print(c - m)
    # 1517 is low
    print(e - c)


if __name__ == "__main__":
    doctest.testmod()
    main()
