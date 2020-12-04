import doctest
import re

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
required_fields = fields - {'cid'}


def valid(passport):
    missing = required_fields - passport.keys()
    if missing:
        return False
    return True


def int_in_range(v, min, max):
    return min <= int(v) <= max


def valid_2(passport):
    if not valid(passport):
        return False
    if not int_in_range(passport['byr'], 1920, 2002):
        return False
    if not int_in_range(passport['iyr'], 2010, 2020):
        return False
    if not int_in_range(passport['eyr'], 2020, 2030):
        return False
    hgt = passport['hgt']
    if hgt.endswith('cm') and int_in_range(hgt[:-2], 150, 193):
        pass
    elif hgt.endswith('in') and int_in_range(hgt[:-2], 59, 76):
        pass
    else:
        return False
    if not re.match('^#[0-9a-f]{6}$', passport['hcl']):
        return False
    if passport['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False
    if not re.match('^[0-9]{9}$', passport['pid']):
        return False
    return True


def main():
    passports = []
    with open('day4_input.txt') as f:
        found = dict()
        for line in f:
            parts = line.strip().split()
            if not parts:
                passports.append(found)
                found = dict()
            else:
                for part in parts:
                    k, v = part.split(':')
                    found[k] = v
        if found:
            passports.append(found)

    print(sum(1 for p in passports if valid(p)))
    print(sum(1 for p in passports if valid_2(p)))


if __name__ == "__main__":
    doctest.testmod()
    main()
