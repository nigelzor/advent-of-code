import doctest

UP = -1j
DOWN = 1j
LEFT = -1
RIGHT = 1

directions = {
    'U': UP,
    'D': DOWN,
    'L': LEFT,
    'R': RIGHT,
}
diagonals = [UP + LEFT, UP + RIGHT, DOWN + LEFT, DOWN + RIGHT]

head_movements = directions.values()
tail_movements = list(directions.values()) + diagonals


def main():
    visited = set()
    segments = [0+0j] * 10

    def print_grid():
        def all_ys():
            return [int(p.imag) for p in visited] + [int(p.imag) for p in segments]

        def all_xs():
            return [int(p.real) for p in visited] + [int(p.real) for p in segments]

        for y in range(min(all_ys()) - 1, max(all_ys()) + 2):
            for x in range(min(all_xs()) - 1, max(all_xs()) + 2):
                p = x + y * 1j
                for i, ip in enumerate(segments):
                    if ip == p:
                        print(i, end='')
                        break
                else:
                    if p in visited:
                        print('#', end='')
                    else:
                        print('.', end='')
            print()

    with open('day9_input.txt') as f:
        for line in f:
            [direction, steps] = line.rstrip().split(' ')
            direction = directions[direction]
            steps = int(steps)

            while steps > 0:
                steps -= 1
                segments[0] += direction
                for i in range(0, len(segments) - 1):
                    head = segments[i]
                    tail = segments[i + 1]
                    adjacent_to_tail = set(tail + d for d in tail_movements)
                    if head != tail and head not in adjacent_to_tail:
                        # print('moving', i, 'from', tail, 'towards', head)
                        adjacent_to_head = set(head + d for d in head_movements)
                        if adjacent_to_head & adjacent_to_tail:
                            segments[i + 1] = next(iter(adjacent_to_head & adjacent_to_tail))
                        else:
                            adjacent_to_head = set(head + d for d in tail_movements)
                            segments[i + 1] = next(iter(adjacent_to_head & adjacent_to_tail))

                visited.add(segments[len(segments) - 1])
            # print()
            # print(line)
            # print_grid()

    print(len(visited))


if __name__ == "__main__":
    doctest.testmod()
    main()
