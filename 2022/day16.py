import doctest
import re
from dataclasses import dataclass
from typing import List, Set, Tuple
import heapq


def main():
    # these don't change
    rates = dict()
    connections = dict()

    def flow_rate(state):
        return sum(rates[r] for r in state.open_valves)

    @dataclass(frozen=True)
    class State:
        current_location: str
        open_valves: Tuple[str]
        minute: int
        released: int

        def potential(self):
            return self.released + flow_rate(self) * (30 - self.minute)

        def __lt__(self, other):
            if self.potential() > other.potential():
                return True
            return False

    initial_state = State('AA', (), 0, 0)

    p = re.compile(r'Valve (\w+) has flow rate=(-?\d+); tunnels? leads? to valves? ([\w, ]+)')
    with open('day16_input.txt') as f:
        for line in f:
            match = p.match(line)
            if match:
                [valve, rate, tunnels] = match.groups()
                rates[valve] = int(rate)
                connections[valve] = tunnels.split(', ')

    print(rates)

    def possible_states(state: State):
        next_minute = state.minute + 1
        next_released = state.released + flow_rate(state)
        if state.current_location not in state.open_valves and rates[state.current_location] > 0:
            new_open_valves = state.open_valves + (state.current_location,)
            yield State(state.current_location, new_open_valves, next_minute, next_released)
        for c in connections.get(state.current_location, []):
            yield State(c, state.open_valves, next_minute, next_released)

    tested = 0
    most_released = -1
    visited_states: Set[State] = set()
    pending_states: List[State] = [initial_state]
    while pending_states:
        best = heapq.heappop(pending_states)
        if best.minute == 30:
            tested += 1
            if best.released > most_released:
                most_released = best.released
                print(tested, best)
        else:
            for next_state in possible_states(best):
                if next_state not in visited_states:
                    visited_states.add(next_state)
                    heapq.heappush(pending_states, next_state)

    # not 1592


if __name__ == "__main__":
    doctest.testmod()
    main()
