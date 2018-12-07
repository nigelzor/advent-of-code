def loop(items):
    while True:
        yield from items


with open('day1.txt') as f:
    lines = [int(x.strip()) for x in f.readlines()]

    freq = 0
    seen = set()

    for x in loop(lines):
        freq += x
        if freq in seen:
            print(freq)
            exit()
        else:
            seen.add(freq)
