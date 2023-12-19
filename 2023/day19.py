import doctest
import re
from dataclasses import dataclass


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    @staticmethod
    def parse(line):
        return Part(*[int(part[2:]) for part in line.strip()[1:-1].split(',')])

    def total(self):
        return self.x + self.m + self.a + self.s


def main():
    workflow_pattern = re.compile(r"(\w+)\{(.*)}")

    workflows = dict()
    parts = []

    def parse_rule(s):
        if ':' in s:
            condition, target = s.split(':')
            if '<' in condition:
                field, value = condition.split('<')
                value = int(value)

                def evaluate(part: Part):
                    if getattr(part, field) < value:
                        return target
                return evaluate
            elif '>' in condition:
                field, value = condition.split('>')
                value = int(value)

                def evaluate(part: Part):
                    if getattr(part, field) > value:
                        return target
                return evaluate
        else:
            return lambda part: s

    with open('day19_input.txt') as f:
        for line in f:
            line = line.strip()
            if not line:
                break

            name, rules = workflow_pattern.match(line).groups()
            rules = [parse_rule(r) for r in rules.split(',')]
            workflows[name] = rules

        for line in f:
            parts.append(Part.parse(line))

    def accepts(workflow, part: Part):
        for rule in workflow:
            v = rule(part)
            if v == 'A':
                return True
            if v == 'R':
                return False
            if v:
                return accepts(workflows[v], part)

    part1 = 0
    for part in parts:
        if accepts(workflows['in'], part):
            print(f"accepted {part}")
            part1 += part.total()
        else:
            print(f"rejected {part}")
    print(f'Part 1: {part1}')


if __name__ == "__main__":
    doctest.testmod()
    main()
