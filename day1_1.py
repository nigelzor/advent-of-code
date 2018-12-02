with open('day1.txt') as f:
    lines = [int(x.strip()) for x in f.readlines()]

    print(sum(lines))
