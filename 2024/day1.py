import doctest


def main():
    ls = []
    rs = []
    with open("day1_input.txt") as f:
        for line in f:
            l, r = [int(x) for x in line.split()]
            ls.append(l)
            rs.append(r)
    ls.sort()
    rs.sort()

    total = sum(abs(l - r) for l, r in zip(ls, rs))
    print(f"part 1: {total}")

    total = sum(l * rs.count(l) for l in ls)
    print(f"part 2: {total}")


if __name__ == "__main__":
    doctest.testmod()
    main()
