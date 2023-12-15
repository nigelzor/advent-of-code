import doctest


def hash(str):
    h = 0
    for s in str:
        h += ord(s)
        h *= 17
        h %= 256
    return h


def main():
    line = open('day15_input.txt').readline().strip()
    steps = line.split(',')

    print(f"Part 1: {sum(hash(s) for s in steps)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
