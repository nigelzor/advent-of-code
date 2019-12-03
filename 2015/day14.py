import doctest
from itertools import cycle


class Reindeer:
    def __init__(self, name, states):
        self.name = name
        self.states = cycle(states)
        self.speed = 0
        self.endurance = 0
        self.travelled = 0
        self.points = 0

    def tick(self):
        if self.endurance < 1:
            self.speed, self.endurance = next(self.states)
        self.travelled += self.speed
        self.endurance -= 1


def main():
    reindeer = []
    with open('day14_input.txt') as f:
        for line in f:
            parts = line.split(' ')
            name = parts[0]
            speed, endurance, recovery = [int(x) for x in parts if x.isnumeric()]
            reindeer.append(Reindeer(name, [(speed, endurance), (0, recovery)]))

    for _ in range(2503):
        for r in reindeer:
            r.tick()
        furthest = max(reindeer, key=lambda r: r.travelled)
        furthest.points += 1

    furthest = max(reindeer, key=lambda r: r.travelled)
    print(furthest.name, furthest.travelled)
    pointiest = max(reindeer, key=lambda r: r.points)
    print(pointiest.name, pointiest.points)


if __name__ == "__main__":
    doctest.testmod()
    main()
