
def turn():
    while True:
        yield 'left'
        yield 'straight'
        yield 'right'


def rotate(c, t):
    if t == 'straight':
        return c
    if t == 'left':
        if c == '>':
            return '^'
        if c == 'v':
            return '>'
        if c == '<':
            return 'v'
        if c == '^':
            return '<'
    if t == 'right':
        if c == '>':
            return 'v'
        if c == 'v':
            return '<'
        if c == '<':
            return '^'
        if c == '^':
            return '>'

with open('day13.txt') as f:
    track = dict()
    trains = []

    for y, line in enumerate(f):
        for x, c in enumerate(line):
            if c in "/-\\|+":
                track[x, y] = c
            elif c in "<>":
                track[x, y] = '-'
                trains.append(((x, y), c, turn()))
            elif c in "^v":
                track[x, y] = '|'
                trains.append(((x, y), c, turn()))
            elif c not in " \n":
                raise Exception('what is >' + c + '<')

    print(trains)

    for tick in range(0, 3000):
        print('tick {}'.format(tick))

        trains.sort(key=lambda x: (x[0][1], x[0][0]))

        for i, ((x, y), c, g) in enumerate(trains):
            if c == '>':
                nxy = (x + 1, y)
            if c == 'v':
                nxy = (x, y + 1)
            if c == '<':
                nxy = (x - 1, y)
            if c == '^':
                nxy = (x, y - 1)

            if any(t[0] == nxy for t in trains):
                print('crash!', nxy)
                exit()

            t = track[nxy]
            if t in '-|':
                nc = c
            elif t == '/':
                if c in '><':
                    nc = rotate(c, 'left')
                else:
                    nc = rotate(c, 'right')
            elif t == '\\':
                if c in '><':
                    nc = rotate(c, 'right')
                else:
                    nc = rotate(c, 'left')
            elif t == '+':
                nc = rotate(c, next(g))

            print('train', c, 'moved from', (x, y), 'to', nxy)
            trains[i] = (nxy, nc, g)


