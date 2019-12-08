import doctest


def main():
    w = 25
    h = 6
    layers = []
    with open('day8_input.txt') as f:
        data = iter(f.readline().strip())
        try:
            while True:
                layers.append([[int(next(data)) for _ in range(w)] for _ in range(h)])
        except StopIteration:
            pass

    # part 1
    def count(layer, value):
        return sum(sum(1 for v in row if v == value) for row in layer)

    min_layer = min((count(layer, 0), layer) for layer in layers)[1]
    ones = count(min_layer, 1)
    twos = count(min_layer, 2)
    print(ones * twos)

    # part 2
    out = dict()
    out[0] = '⬛️'
    out[1] = '⬜️'

    for y in range(h):
        for x in range(w):
            values = [l[y][x] for l in layers]
            values = [out[v] for v in values if v != 2]
            print(values[0], end='')
        print('')


if __name__ == "__main__":
    doctest.testmod()
    main()
