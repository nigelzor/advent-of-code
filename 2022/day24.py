import doctest
import functools
import heapq
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mod__(self, other):
        return Point(self.x % other.x, self.y % other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

UP = Point(0, -1)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)
WAIT = Point(0, 0)

MOVE_OPTIONS = [UP, DOWN, LEFT, RIGHT, WAIT]


def pt(x, y):
    return Point(x, y)

def bounds(grid):
    minx = min(c.x for c in grid.keys())
    maxx = max(c.x for c in grid.keys())
    miny = min(c.y for c in grid.keys())
    maxy = max(c.y for c in grid.keys())
    return minx, maxx, miny, maxy


def main():
    grid = dict()

    with open('day24_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line):
                if c == '#' or c in '^v<>':
                    grid[pt(x - 1, y - 1)] = c

    _, maxx, _, maxy = bounds(grid)
    height = maxy
    width = maxx
    size = pt(width, height)
    start = pt(0, -1)
    goal = pt(maxx - 1, maxy)
    almost_goal = goal + UP

    print(width, height, start, goal)

    moving_up = [k for k, v in grid.items() if v == '^']
    moving_down = [k for k, v in grid.items() if v == 'v']
    moving_left = [k for k, v in grid.items() if v == '<']
    moving_right = [k for k, v in grid.items() if v == '>']

    @functools.lru_cache(50)
    def grid_at_t(t):
        # print('build grid', t)
        return set((p + UP * t) % size for p in moving_up) \
                | set((p + DOWN * t) % size for p in moving_down) \
                | set((p + LEFT * t) % size for p in moving_left) \
                | set((p + RIGHT * t) % size for p in moving_right)

    def valid_move(next_grid, position):
        if position == start:
            return True
        if not (0 <= position.x < width):
            return False
        if not (0 <= position.y < height):
            return False
        return position not in next_grid

    @dataclass(frozen=True, order=True)
    class State:
        time: int
        position: Point

        def successors(self, grid_fn):
            next_time = self.time + 1
            if self.position == almost_goal:
                return [State(next_time, goal)]

            next_grid = grid_fn(next_time)
            return [State(next_time, self.position + move) for move in MOVE_OPTIONS if valid_move(next_grid, self.position + move)]

        def with_score(self):
            distance = self.position.x + self.position.y
            return (-distance, -self.time), self


    seen = set()
    unexplored = []
    heapq.heappush(unexplored, State(0, start).with_score())

    i = 0
    fastest = float('inf')
    while unexplored:
        i += 1
        score, state = heapq.heappop(unexplored)
        if state.time >= fastest:
            pass
        elif state.position == goal:
            print(f'reached goal at t={state.time}, i={i}')  # 418 too high
            fastest = state.time
        else:
            successors = state.successors(grid_at_t)
            # print(f'{len(successors)} successors: {successors}')
            for s in successors:
                if s not in seen:
                    seen.add(s)
                    heapq.heappush(unexplored, s.with_score())


if __name__ == "__main__":
    doctest.testmod()
    main()
