import doctest

map = {
    'A': 1,  # rock
    'B': 2,  # paper
    'C': 3,  # scissors
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def beats(x):
    if x == 1:
        return 2
    if x == 2:
        return 3
    if x == 3:
        return 1


def loses(x):
    if x == 1:
        return 3
    if x == 2:
        return 1
    if x == 3:
        return 2


def score(me, opp):
    if me == opp:
        return 3
    if me == beats(opp):
        return 6
    return 0


def main():
    total_part1 = 0
    total_part2 = 0
    with open('day2_input.txt') as f:
        for line in f:
            [opp, me] = line.strip().split(' ')
            opp = map[opp]

            me1 = map[me]
            total_part1 += me1 + score(me1, opp)

            if me == 'X':
                me2 = loses(opp)
            elif me == 'Y':
                me2 = opp
            else:
                me2 = beats(opp)

            total_part2 += me2 + score(me2, opp)

    print(total_part1)  # 8392
    print(total_part2)  # 10116


if __name__ == "__main__":
    doctest.testmod()
    main()
