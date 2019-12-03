import doctest
from collections import defaultdict
from itertools import permutations


def main():
    people = set()
    weights = defaultdict(int)
    with open('day13_input.txt') as f:
        for line in f:
            parts = line.strip().split(' ')
            people.add(parts[0])
            weight = int(parts[3])
            if parts[2] == 'lose':
                weight = -weight
            weights[(parts[0], parts[-1][:-1])] = weight

    def score(seating):
        total = 0
        for i in range(len(seating)):
            total += weights[(seating[i], seating[i - 1])]
            total += weights[(seating[i - 1], seating[i])]
        return total

    first = min(people)
    options = (o for o in permutations(people) if o[0] == first)
    scored_options = ((score(o), o) for o in options)
    print(max(scored_options))

    def and_me(seating):
        result = ['Me']
        result.extend(seating)
        return result
    options = (and_me(o) for o in permutations(people))
    scored_options = ((score(o), o) for o in options)
    print(max(scored_options))


if __name__ == "__main__":
    doctest.testmod()
    main()
