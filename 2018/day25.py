def read(filename):
    points = []
    with open(filename) as f:
        for line in f:
            points.append(tuple(int(x) for x in line.strip().split(',')))
    return points


def distance(a, b):
    return sum(abs(ai - bi) for ai, bi in zip(a, b))


class Constellation(object):
    def __init__(self):
        self.points = set()

    def accept(self, point):
        for p in self.points:
            if distance(p, point) <= 3:
                return True
        return False


def group(points):
    constellations = []
    for p in points:
        modified = []
        for c in constellations:
            if c.accept(p):
                c.points.add(p)
                modified.append(c)

        if len(modified) == 0:
            c = Constellation()
            c.points.add(p)
            constellations.append(c)
        elif len(modified) > 1:
            joined = Constellation()
            for m in modified:
                joined.points.update(m.points)
                constellations.remove(m)
            constellations.append(joined)

    return constellations


def main():
    points = read('day25.txt')
    constellations = group(points)

    for c in constellations:
        print(c.points)
    print(len(constellations), 'constellations')
    # 331 is too high


if __name__ == '__main__':
    main()
