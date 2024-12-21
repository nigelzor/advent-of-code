import doctest


def bi_map(*lines: str):
    mapping = dict()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            p = (x, y)
            mapping[p] = c
            mapping[c] = p
    return mapping


door_pad = bi_map("789", "456", "123", " 0A")

control_pad = bi_map(" ^A", "<v>")


def to_movement(src, dst):
    dx = dst[0] - src[0]
    dy = dst[1] - src[1]
    presses = ""
    if dx > 0:
        presses += dx * ">"
    if dx < 0:
        presses += -dx * "<"
    if dy > 0:
        presses += dy * "v"
    if dy < 0:
        presses += -dy * "^"
    return presses


def movement_options(src, dst):
    m = to_movement(src, dst)
    if src[0] == 0 and dst[1] == 3:
        return {m + "A"}  # must move x first
    if src[1] == 3 and dst[0] == 0:
        return {m[::-1] + "A"}  # must move y first

    # two permutations: y before x and x before y
    return {m + "A", m[::-1] + "A"}


def optimal_input(code, levels):
    """
    >>> optimal_input("029A", 0)
    '<A^A>^^AvvvA'
    >>> optimal_input("029A", 1)
    'v<<A>>^A<A>AvA<^AA>A<vAAA>^A'
    >>> optimal_input("029A", 2)
    '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'
    """
    to_press = ""
    position = door_pad["A"]
    for c in code:
        target = door_pad[c]
        to_press += min(
            (expand_recursively(o, levels) for o in movement_options(position, target)),
            key=len,
        )
        position = target
    return to_press


def expand_recursively(code, levels):
    if levels == 0:
        return code
    to_press = ""
    position = control_pad["A"]
    for c in code:
        target = control_pad[c]
        to_press += min(
            (
                expand_recursively(o, levels - 1)
                for o in movement_options(position, target)
            ),
            key=len,
        )
        position = target
    return to_press


def main():
    with open("day21_input.txt") as f:
        codes = [line.strip() for line in f]

    def complexity(code, levels):
        optimal = optimal_input(code, levels)
        return int(code[:3]) * len(optimal)

    print(f"part 1: {sum(complexity(code, 2) for code in codes)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
