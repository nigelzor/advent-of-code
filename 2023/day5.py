import doctest
import re


class Mapping:
    def __init__(self, source, destination, override=None):
        self.source = source
        self.destination = destination
        self.override = override or []

    def get(self, n):
        for (range, offset) in self.override:
            if n in range:
                return n + offset
        return n


def main():
    whitespace = re.compile(" +")
    title = re.compile("(\w+)-to-(\w+) map:")

    maps = []

    with open('day5_input.txt') as f:
        seeds = [int(s) for s in whitespace.split(f.readline().split(":")[1].strip())]

        mapping = None

        for line in f:
            line = line.strip()

            m = title.match(line)
            if m:
                source = m.group(1)
                destination = m.group(2)
                mapping = Mapping(source, destination)
                maps.append(mapping)

            elif line:
                [destination_range_start, source_range_start, range_length] = [int(s) for s in whitespace.split(line)]
                offset = destination_range_start - source_range_start
                mapping.override.append((range(source_range_start, source_range_start + range_length), offset))

    def to_location(kind, n):
        if kind == "location":
            return n
        for mapping in maps:
            if mapping.source == kind:
                return to_location(mapping.destination, mapping.get(n))
        else:
            raise Exception(f"No mapping for {kind}")

    part1 = min(to_location("seed", seed) for seed in seeds)
    print(f"Part 1: {part1}")
    # print(f"Part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
