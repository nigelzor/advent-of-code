import doctest


def main():
    locks = []
    keys = []
    pending = []

    def process_pending():
        if pending:
            if pending[0][0] == "#":  # lock
                locks.append([col.index(".") - 1 for col in zip(*pending)])
            else:  # key
                keys.append([6 - col.index("#") for col in zip(*pending)])
        pending.clear()

    with open("day25_input.txt") as f:
        lines = (line.strip() for line in f)
        try:
            while True:
                while line := next(lines):
                    pending.append(line)

                process_pending()
        except StopIteration:
            process_pending()

    def key_fits(lock, key):
        return all(a + b <= 5 for a, b in zip(lock, key))

    part1 = sum(1 for lock in locks for key in keys if key_fits(lock, key))

    print(f"part 1: {part1}")


if __name__ == "__main__":
    doctest.testmod()
    main()
