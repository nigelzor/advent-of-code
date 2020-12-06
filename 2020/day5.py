import doctest


def row_num(bp):
    """
    >>> row_num('FBFBBFFRLR')
    44
    """
    return int(bp[:7].replace('F', '0').replace('B', '1'), 2)


def col_num(bp):
    """
    >>> col_num('FBFBBFFRLR')
    5
    """
    return int(bp[-3:].replace('L', '0').replace('R', '1'), 2)


def seat_id(bp):
    """
    >>> seat_id('FBFBBFFRLR')
    357
    """
    return row_num(bp) * 8 + col_num(bp)


def main():
    passes = []
    with open('day5_input.txt') as f:
        for line in f:
            passes.append(line.strip())

    print(max(seat_id(bp) for bp in passes))

    all_seats = [seat_id(bp) for bp in passes]
    all_seats.sort()
    for s1, s2 in zip(all_seats, all_seats[1:]):
        if s2 != s1 + 1:
            print(s1 + 1, 'between', s1, s2)


if __name__ == "__main__":
    doctest.testmod()
    main()
