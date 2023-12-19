import doctest
import re
from dataclasses import dataclass


fields = 'xmas'


@dataclass
class Anything:
    def __and__(self, other):
        return other

    def __invert__(self):
        return Nothing()

    def __contains__(self, item):
        return True


@dataclass
class Nothing:
    def __and__(self, other):
        return self

    def __invert__(self):
        return Anything()

    def __contains__(self, item):
        return False


@dataclass
class Above:
    x: int

    def __and__(self, other):
        if isinstance(other, Anything):
            return self
        if isinstance(other, Nothing):
            return other
        if isinstance(other, Above):
            return Above(max(self.x, other.x))
        if isinstance(other, Below):
            return Between.from_range(self.x, other.x)

    def __contains__(self, item):
        return item > self.x

    def __invert__(self):
        """
        >>> ~Above(5)
        Below(x=6)
        """
        return Below(self.x + 1)


@dataclass
class Below:
    x: int

    def __and__(self, other):
        """
        >>> Above(4) & Below(5)
        Nothing()
        """

        if isinstance(other, Anything):
            return self
        if isinstance(other, Nothing):
            return other
        if isinstance(other, Above):
            return Between.from_range(other.x, self.x)
        if isinstance(other, Below):
            return Below(min(self.x, other.x))

    def __contains__(self, item):
        return item < self.x

    def __invert__(self):
        """
        >>> ~Below(5)
        Above(x=4)
        """
        return Above(self.x - 1)


@dataclass
class Between:
    x: int
    y: int

    @staticmethod
    def from_range(min, max):
        if max - min <= 1:
            return Nothing()
        return Between(min, max)

    def __len__(self):
        """
        >>> len(Between(0, 4001))
        4000
        """
        return self.y - self.x - 1

    def __and__(self, other):
        if isinstance(other, Anything):
            return self
        if isinstance(other, Nothing):
            return other
        if isinstance(other, Above):
            return Between.from_range(max(self.x, other.x), self.y)
        if isinstance(other, Below):
            return Between.from_range(self.x, min(other.x, self.y))

    def __contains__(self, item):
        return self.x < item < self.y


def main():
    workflow_pattern = re.compile(r"(\w+)\{(.*)}")

    workflows = dict()
    parts = []

    def parse_rule(s):
        if ':' in s:
            condition, target = s.split(':')
            if '<' in condition:
                field, value = condition.split('<')
                return fields.index(field), Below(int(value)), target
            elif '>' in condition:
                field, value = condition.split('>')
                return fields.index(field), Above(int(value)), target
        else:
            return s

    def parse_part(line):
        return [int(p[2:]) for p in line.strip()[1:-1].split(',')]

    with open('day19_input.txt') as f:
        for line in f:
            line = line.strip()
            if not line:
                break

            name, rules = workflow_pattern.match(line).groups()
            rules = [parse_rule(r) for r in rules.split(',')]
            workflows[name] = rules

        for line in f:
            parts.append(parse_part(line))

    def accepts(workflow, part):
        for rule in workflow:
            next_workflow = None
            if isinstance(rule, tuple):
                field, range, target = rule
                if part[field] in range:
                    next_workflow = target
            else:
                next_workflow = rule
            if next_workflow == 'A':
                return True
            if next_workflow == 'R':
                return False
            if next_workflow:
                return accepts(workflows[next_workflow], part)

    part1 = 0
    for part in parts:
        if accepts(workflows['in'], part):
            part1 += sum(part)
    print(f'Part 1: {part1}')

    def expand_ranges(workflow_name, ranges):
        if any(isinstance(r, Nothing) for r in ranges):
            pass
        if workflow_name == 'A':
            yield ranges, 'A'
        elif workflow_name == 'R':
            yield ranges, 'R'
        else:
            workflow = workflows[workflow_name]
            for rule in workflow:
                if isinstance(rule, tuple):
                    field, range, target = rule
                    matched_ranges = list(ranges)
                    matched_ranges[field] = ranges[field] & range
                    yield from expand_ranges(target, matched_ranges)
                    unmatched_ranges = list(ranges)
                    unmatched_ranges[field] = ranges[field] & ~range
                    ranges = unmatched_ranges
                else:
                    yield from expand_ranges(rule, ranges)

    part2 = 0
    for ranges, result in expand_ranges('in', [Between(0, 4001)] * 4):
        if result == 'A':
            product = 1
            for r in ranges:
                product *= len(r)
            part2 += product
    print(f'Part 2: {part2}')


if __name__ == "__main__":
    doctest.testmod()
    main()
