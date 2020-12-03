import doctest


def main():
    lines = []
    with open('day1_input.txt') as f:
        for line in f:
            lines.append(int(line))

    for a in lines:
        for b in lines:
            if a + b == 2020:
                print(a * b)

            for c in lines:
                if a + b + c == 2020:
                    print(a * b * c)


if __name__ == "__main__":
    doctest.testmod()
    main()
