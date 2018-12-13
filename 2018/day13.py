
def turn_generator():
    while True:
        yield 'left'
        yield 'straight'
        yield 'right'


def rotate(car, t):
    if t == 'straight':
        return car
    if t == 'left':
        if car == '>':
            return '^'
        if car == 'v':
            return '>'
        if car == '<':
            return 'v'
        if car == '^':
            return '<'
    if t == 'right':
        if car == '>':
            return 'v'
        if car == 'v':
            return '<'
        if car == '<':
            return '^'
        if car == '^':
            return '>'


def advance(car, xy):
    x, y = xy
    if car == '>':
        return x + 1, y
    if car == 'v':
        return x, y + 1
    if car == '<':
        return x - 1, y
    if car == '^':
        return x, y - 1


def load(filename):
    with open(filename) as f:
        track = dict()
        trains = []

        for y, line in enumerate(f):
            for x, c in enumerate(line):
                if c in "/-\\|+":
                    track[x, y] = c
                elif c in "<>":
                    track[x, y] = '-'
                    trains.append(((x, y), c, turn_generator()))
                elif c in "^v":
                    track[x, y] = '|'
                    trains.append(((x, y), c, turn_generator()))
                elif c not in " \n":
                    raise Exception('what is "{}"?'.format(c))
        return track, trains


def main(part):
    track, trains = load('day13.txt')

    for tick in range(0, 30000):
        print('tick {}'.format(tick))

        trains.sort(key=lambda train: (train[0][1], train[0][0]))
        dead = set()

        if len(trains) < 2:
            print('last train', ', '.join(['{} {}'.format(*t[:2]) for t in trains]))
            break

        for i, (xy, car, turn) in enumerate(trains):
            if i in dead:
                continue

            next_xy = advance(car, xy)

            for j, t in enumerate(trains):
                if i != j and j not in dead and t[0] == next_xy:
                    print('train moved from', xy, car, 'to crash at', next_xy)
                    dead.add(i)
                    dead.add(j)
                    if part == 1:
                        return
                    else:
                        break
            else:
                t = track[next_xy]
                if t in '-|':
                    next_car = car
                elif t == '/':
                    if car in '><':
                        next_car = rotate(car, 'left')
                    else:
                        next_car = rotate(car, 'right')
                elif t == '\\':
                    if car in '><':
                        next_car = rotate(car, 'right')
                    else:
                        next_car = rotate(car, 'left')
                elif t == '+':
                    next_car = rotate(car, next(turn))
                else:
                    raise Exception('what is "{}"?'.format(t))

                print('train moved from', xy, car, 'along', t, 'to', next_xy, next_car)
                trains[i] = (next_xy, next_car, turn)

        if len(dead):
            trains = [t for k, t in enumerate(trains) if k not in dead]


if __name__ == '__main__':
    main(part=2)
