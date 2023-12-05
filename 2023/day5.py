import doctest
import re


class Range:
    def __init__(self, start, length):
        self.start = start
        self.length = length
        self.end = start + length

    def __lt__(self, other):
        return self.start < other.start

    def __len__(self):
        """
        >>> len(Range(10, 2))
        2
        """
        return self.length

    def __iter__(self):
        """
        >>> list(Range(1, 3))
        [1, 2, 3]
        """
        return iter(range(self.start, self.end))

    def __contains__(self, item):
        """
        >>> 2 in Range(0, 4)
        True
        >>> 4 in Range(0, 4)
        False
        """
        return self.start <= item < self.end

    def __and__(self, other):
        """
        >>> Range(0, 2) & Range(1, 2)
        Range(1, 1)
        """
        start = max(self.start, other.start)
        end = min(self.end, other.end)
        if start < end:
            return Range(start, end - start)

    def __repr__(self):
        return f"Range({self.start}, {self.length})"

    def offset(self, n):
        """
        >>> Range(0, 3).offset(10)
        Range(10, 3)
        """
        return Range(self.start + n, self.length)


class Mapping:
    def __init__(self, source, destination, ranges=None):
        self.source = source
        self.destination = destination
        self.ranges = ranges or []
        if ranges:
            self.fill_gaps()

    def fill_gaps(self):
        self.ranges.sort()
        last_end = 0
        to_add = []
        for (range, offset) in self.ranges:
            if range.start > last_end:
                to_add.append(Range(last_end, range.start - last_end))
            last_end = range.end
        if last_end < 2**32:
            to_add.append(Range(last_end, 2**32 - last_end))
        self.ranges.extend((r, 0) for r in to_add)

    def get(self, n):
        """
        >>> Mapping("seed", "soil", [(Range(98, 2), -48), (Range(50, 48), 2)]).get(10)
        10
        >>> Mapping("seed", "soil", [(Range(98, 2), -48), (Range(50, 48), 2)]).get(50)
        52
        >>> Mapping("seed", "soil", [(Range(98, 2), -48), (Range(50, 48), 2)]).get(97)
        99
        >>> Mapping("seed", "soil", [(Range(98, 2), -48), (Range(50, 48), 2)]).get(98)
        50
        """
        for (range, offset) in self.ranges:
            if n in range:
                return n + offset
        return n

    def get_ranges(self, r):
        """
        >>> list(Mapping("seed", "soil", [(Range(98, 2), -48), (Range(50, 48), 2)]).get_ranges(Range(10, 1)))
        [Range(10, 1)]
        >>> list(Mapping("seed", "soil", [(Range(98, 2), -48), (Range(50, 48), 2)]).get_ranges(Range(50, 1)))
        [Range(52, 1)]
        >>> list(Mapping("seed", "soil", [(Range(98, 2), -48), (Range(50, 48), 2)]).get_ranges(Range(97, 2)))
        [Range(99, 1), Range(50, 1)]
        """
        for (range, offset) in self.ranges:
            intersection = r & range
            if intersection:
                yield intersection.offset(offset)


def main():
    whitespace = re.compile(" +")
    title = re.compile(r"(\w+)-to-(\w+) map:")

    maps = dict()

    with open('day5_input.txt') as f:
        part1_seeds = [int(s) for s in whitespace.split(f.readline().split(":")[1].strip())]
        part2_seeds = [Range(start, length) for (start, length) in zip(*[iter(part1_seeds)] * 2)]

        mapping = None

        for line in f:
            line = line.strip()

            m = title.match(line)
            if m:
                source = m.group(1)
                destination = m.group(2)
                mapping = Mapping(source, destination)
                maps[source] = mapping

            elif line:
                [destination_range_start, source_range_start, range_length] = [int(s) for s in whitespace.split(line)]
                offset = destination_range_start - source_range_start
                mapping.ranges.append((Range(source_range_start, range_length), offset))

    for mapping in maps.values():
        mapping.fill_gaps()

    def to_location(kind, n):
        if kind == "location":
            return n
        m = maps[kind]
        return to_location(m.destination, m.get(n))

    def range_to_location(kind, r: Range):
        if kind == "location":
            return r.start
        m = maps[kind]
        return min(range_to_location(m.destination, nextr) for nextr in m.get_ranges(r))

    part1 = min(to_location("seed", seed) for seed in part1_seeds)
    print(f"Part 1: {part1}")
    part2 = min(range_to_location("seed", seed) for seed in part2_seeds)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
