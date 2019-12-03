import doctest
import re
from collections import defaultdict

TURN_ON = 'turn on'
TURN_OFF = 'turn off'
TOGGLE = 'toggle'

p = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')


def parse(line):
    cmd, x1, y1, x2, y2 = p.match(line).groups()
    return cmd, int(x1), int(y1), int(x2), int(y2)


def main():
    lights = defaultdict(bool)
    lights2 = defaultdict(int)

    with open('day6_input.txt') as f:
        for line in f:
            cmd, x1, y1, x2, y2 = parse(line)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if cmd == TURN_ON:
                        lights[(x, y)] = True
                        lights2[(x, y)] += 1
                    if cmd == TURN_OFF:
                        lights[(x, y)] = False
                        lights2[(x, y)] = max(lights2[(x, y)] - 1, 0)
                    if cmd == TOGGLE:
                        lights[(x, y)] = not lights[(x, y)]
                        lights2[(x, y)] += 2

    print(sum(1 for z in lights.values() if z))
    print(sum(lights2.values()))


if __name__ == "__main__":
    doctest.testmod()
    main()
