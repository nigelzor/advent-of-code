import doctest
import re

LITERAL = 1
ALTERNATION = 2
SEQUENCE = 3


def parse(rule):
    if rule[0] == '"':
        return LITERAL, rule[1:-1]
    parts = rule.split(' | ')
    if len(parts) > 1:
        return ALTERNATION, [parse(part) for part in parts]
    else:
        return SEQUENCE, parts[0].split(' ')


def to_regex(rules, rule):
    if rule[0] == LITERAL:
        return rule[1]
    elif rule[0] == SEQUENCE:
        return ''.join(to_regex(rules, rules[p]) for p in rule[1])
    elif rule[0] == ALTERNATION:
        return '(' + '|'.join(to_regex(rules, p) for p in rule[1]) + ')'


def main():
    with open('day19_input.txt') as file:
        lines = [line.strip() for line in file]

    rules = dict()
    lines = iter(lines)
    for line in lines:
        if not line:
            break
        n, parts = line.split(': ', 2)
        rules[n] = parse(parts)

    messages = [line for line in lines]
    rule0 = re.compile(to_regex(rules, rules['0']))
    print(sum(1 for m in messages if rule0.fullmatch(m)))

    rules['8'] = parse('42 | 42 8')
    # 42 8?
    # 42+

    rules['11'] = parse('42 31 | 42 11 31')
    # 42 11? 31
    # 42 42 11? 31 31
    # 42{1,n} 31{1,n} with equal n

    # rules['0'] = parse('8 11')
    # 42+ 42{1,n} 31{1,n} with equal n
    # 42{2,m} 31{1,n} with m > n

    rule42 = re.compile('^' + to_regex(rules, rules['42']))
    rule31 = re.compile('^' + to_regex(rules, rules['31']))

    def match_part2(line):
        count42 = 0
        while m := rule42.match(line):
            count42 += 1
            line = line[m.end():]
        if count42 < 2:
            return False
        count31 = 0
        while m := rule31.match(line):
            count31 += 1
            line = line[m.end():]
        if count31 < 1:
            return False
        if len(line):
            return False
        return count42 > count31

    print(sum(1 for m in messages if match_part2(m)))


if __name__ == "__main__":
    doctest.testmod()
    main()
