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
    head = 0
    tail = 0

    def print_grid():
        for y in range(int(min(p.imag for p in visited)), int(max(p.imag for p in visited)) + 1):
            for x in range(int(min(p.real for p in visited)), int(max(p.real for p in visited)) + 1):
                p = x + y * 1j
                if head == p:
                    print('H', end='')
                elif tail == p:
                    print('T', end='')
                elif p in visited:
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
                head += direction
                adjacent_to_tail = set(tail + d for d in tail_movements)
                if head != tail and head not in adjacent_to_tail:
                    adjacent_to_head = set(head + d for d in head_movements)
                    tail = next(iter(adjacent_to_head & adjacent_to_tail))
                visited.add(tail)

    print(len(visited))


if __name__ == "__main__":
    doctest.testmod()
    main()
