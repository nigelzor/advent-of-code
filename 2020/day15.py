import doctest
from collections import defaultdict


def main():
    start = [int(x) for x in '1,2,16,19,18,0'.split(',')]
    previous = None
    last_seen = defaultdict(int)

    for t, x in enumerate(start):
        t += 1
        last_seen[previous] = t - 1
        previous = x
        # print(t, ':', x)

    for t in range(len(start), 30000000):
        t += 1
        if last_seen[previous]:
            x = t - last_seen[previous] - 1
        else:
            x = 0

        last_seen[previous] = t - 1
        previous = x

        if t == 2020:
            print(t, ':', x)
    print(t, ':', x)


if __name__ == "__main__":
    doctest.testmod()
    main()
