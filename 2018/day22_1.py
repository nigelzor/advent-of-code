# depth: 11817
# target: 9,751

from functools import lru_cache

ROCKY = 0
WET = 1
NARROW = 2

depth = 11817
target = (9, 751)

# depth = 510
# target = (10, 10)

def erosion_level(x, y):
    return (geologic_index(x, y) + depth) % 20183

@lru_cache(maxsize=None)
def geologic_index(x, y):
    if x == 0 and y == 0:
        return 0
    if x == target[0] and y == target[1]:
        return 0
    if y == 0:
        return x * 16807
    if x == 0:
        return y * 48271
    return erosion_level(x - 1, y) * erosion_level(x, y - 1)

def region_type(x, y):
    return erosion_level(x, y) % 3

def risk(x, y):
    return region_type(x, y)


if __name__ == '__main__':
    total_risk = 0
    for x in range(0, target[0] + 1):
        for y in range(0, target[1] + 1):
            total_risk += risk(x, y)

    print('total_risk', total_risk)
