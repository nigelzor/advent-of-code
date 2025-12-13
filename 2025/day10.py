import doctest
import re
import heapq
from z3 import Int, Optimize


def parse_lights(lights):
    """
    >>> parse_lights('.##.')
    6
    """
    r = 0
    for c in lights:
        r = (r << 1) | (1 if c == "#" else 0)
    return r


def parse_buttons(n_lights, buttons):
    """
    >>> parse_buttons(4, [3])
    1
    >>> parse_buttons(4, [2,3])
    3
    """
    r = 0
    for b in buttons:
        r |= 1 << (n_lights - b - 1)
    return r


def solve_lights(lights, buttons):
    """
    >>> solve_lights(".##.", [(3,), (1,3), (2,), (2,3), (0,2), (0,1)])
    2
    """
    n_lights = len(lights)
    goal = parse_lights(lights)
    buttons = [parse_buttons(n_lights, b) for b in buttons]

    # this is super overkill. each button will be pressed at most once
    visited = {}  # state -> min(steps)
    pending = [(0, 0)]  # (steps, lights)
    while pending:
        steps, state = heapq.heappop(pending)
        for button in buttons:
            next_state = state ^ button
            next_steps = steps + 1
            if next_state == goal:
                return next_steps

            if next_state not in visited or next_steps < visited[next_state]:
                visited[next_state] = next_steps
                heapq.heappush(pending, (next_steps, next_state))
    raise Exception("No solution found")


def solve_joltage(joltage, buttons):
    """
    >>> solve_joltage([3,5,4,7], [(3,), (1,3), (2,), (2,3), (0,2), (0,1)])
    10
    """
    optimize = Optimize()

    presses = [Int(f"button_{i}") for i in range(len(buttons))]
    for b in range(len(buttons)):
        optimize.add(presses[b] >= 0)

    for i, j in enumerate(joltage):
        counter = sum(presses[b] for b in range(len(buttons)) if i in buttons[b])
        optimize.add(counter == j)

    total = sum(presses)
    optimize.minimize(total)

    assert optimize.check().r == 1
    m = optimize.model()
    return sum(m[p].as_long() for p in presses)


def ints(s):
    return [int(x) for x in s.split(",")]


def main():
    machines = []
    with open("day10_input.txt") as f:
        for line in f:
            m = re.match(r"^\[(.*)] (.*) \{(.*)}$", line.strip())
            lights = m.group(1)
            buttons = [ints(w[1:-1]) for w in m.group(2).split()]
            joltage = ints(m.group(3))

            machines.append((lights, buttons, joltage))

    part1 = sum(solve_lights(lights, buttons) for lights, buttons, _ in machines)
    print(f"part 1: {part1}")

    part2 = sum(solve_joltage(joltage, buttons) for _, buttons, joltage in machines)
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
