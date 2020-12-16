import doctest


def to_range(s):
    lo, hi = s.split('-')
    return range(int(lo), int(hi) + 1)


def main():
    with open('day16_input.txt') as file:
        lines = [line.strip() for line in file.readlines()]
    ilines = iter(lines)

    fields = dict()
    while True:
        line = next(ilines)
        if not line:
            break
        f, rest = line.split(': ')
        ranges = rest.split(' or ')
        fields[f] = [to_range(r) for r in ranges]

    def any_field_matches(n):
        for name, ranges in fields.items():
            for r in ranges:
                if n in r:
                    return True
        return False

    next(ilines)  # "your ticket:"
    my_ticket = [int(x) for x in next(ilines).split(',')]

    next(ilines)  # empty
    next(ilines)  # "nearby tickets:"

    nearby_tickets = []
    for line in ilines:
        nearby_tickets.append([int(x) for x in line.split(',')])

    error_rate = 0
    valid_tickets = []
    for ticket in nearby_tickets:
        valid = True
        for f in ticket:
            if not any_field_matches(f):
                error_rate += f
                valid = False
        if valid:
            valid_tickets.append(ticket)

    print(error_rate)

    def possibly_field(k, n):
        ranges = fields[k]
        return any(n in r for r in ranges)

    def remove_options(n, to_remove):
        if not to_remove & possibilities[n]:
            return
        possibilities[n] -= to_remove
        if len(possibilities[n]) == 1:
            # print(f'{n} must be {possibilities[n]}')
            for other_n, p in possibilities.items():
                if n != other_n:
                    remove_options(other_n, possibilities[n])

    possibilities = {n: set(fields.keys()) for n in range(len(fields))}
    for ticket in valid_tickets:
        for n, f in enumerate(ticket):
            to_remove = {k for k in possibilities[n] if not possibly_field(k, f)}
            remove_options(n, to_remove)

    assert all(len(p) == 1 for p in possibilities.values())
    mapping = {next(iter(p)): n for n, p in possibilities.items()}

    result = 1
    for k, n in mapping.items():
        if k.startswith('departure'):
            result *= my_ticket[n]
    print(result)


if __name__ == "__main__":
    doctest.testmod()
    main()
