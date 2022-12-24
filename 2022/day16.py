import doctest
import itertools
import re
from dataclasses import dataclass
from typing import Tuple
import heapq
import networkx as nx
from collections import defaultdict

TIME_LIMIT = 26
N_ACTORS = 2
INPUT_FILE = 'day16_input.txt'


@dataclass(order=True, frozen=True)
class Actor:
    location: str
    in_transit: int


@dataclass(order=True, unsafe_hash=True)
class State:
    actors: Tuple[Actor]
    open_valves: Tuple
    minute: int
    released: int
    flow_rate: int

    # parent = None

    def successors(self, rates, relevant_valves, shortest_paths):
        next_minute = self.minute + 1
        next_released = self.released + self.flow_rate

        def actor_options(actor: Actor):
            if actor.in_transit:
                return [(Actor(actor.location, actor.in_transit - 1), None)]

            if rates[actor.location] > 0 and actor.location not in self.open_valves:
                return [(actor, actor.location)]

            valves_to_open = [v for v in relevant_valves if v != actor.location and v not in self.open_valves]
            if not valves_to_open:
                return [(actor, None)]
            else:
                return [(Actor(v, shortest_paths[actor.location][v] - 1), None) for v in valves_to_open]

        for options in itertools.product(*[actor_options(a) for a in self.actors]):
            next_actors = tuple(a for a, _ in options)
            next_open_valves = self.open_valves
            next_flow_rate = self.flow_rate
            if any(v for _, v in options):
                opened = tuple(set(v for _, v in options if v))
                next_open_valves += opened
                next_flow_rate += sum(rates[v] for v in opened)
            next_state = State(next_actors, next_open_valves, next_minute, next_released, next_flow_rate)
            # next_state.parent = self
            next_state.fast_forward()
            yield next_state

    def with_score(self):
        return -self.released, self

    def fast_forward(self):
        ff = TIME_LIMIT - self.minute
        for a in self.actors:
            ff = min(ff, a.in_transit)
        if ff > 0:
            self.actors = tuple(Actor(a.location, a.in_transit - ff) for a in self.actors)
            self.minute += ff
            self.released += ff * self.flow_rate


def main():
    # these don't change
    rates = dict()
    connections = dict()

    p = re.compile(r'Valve (\w+) has flow rate=(-?\d+); tunnels? leads? to valves? ([\w, ]+)')
    with open(INPUT_FILE) as f:
        for line in f:
            match = p.match(line)
            if match:
                [valve, rate, tunnels] = match.groups()
                rates[valve] = int(rate)
                connections[valve] = tunnels.split(', ')

    graph = nx.Graph()
    for v, cs in connections.items():
        for c in cs:
            graph.add_edge(v, c, weight=1)

    shortest_paths = nx.floyd_warshall(graph)
    relevant_valves = [valve for valve, rate in rates.items() if rate > 0]

    def find_best(initial):
        seen = set()
        unexplored = []
        heapq.heappush(unexplored, initial.with_score())

        best_at_minute = defaultdict(int)
        pruned_count = 0

        def prune(state):
            check_t = state.minute - 2
            if best_at_minute[check_t] > state.released:
                return True
            best_at_minute[state.minute] = max(best_at_minute[state.minute], state.released)
            return False

        i = 0
        best = None
        while unexplored:
            i += 1
            score, state = heapq.heappop(unexplored)
            if prune(state):
                pruned_count += 1
            elif state.minute == TIME_LIMIT:
                if best is None or state.released > best.released:
                    print(f'new best released={state.released}, i={i}')
                    best = state
            else:
                successors = state.successors(rates, relevant_valves, shortest_paths)
                for s in successors:
                    if s not in seen:
                        seen.add(s)
                        heapq.heappush(unexplored, s.with_score())

        print(f'pruned {pruned_count}/{i}')
        return best

    best_terminal_node = find_best(State((Actor('AA', 0),) * N_ACTORS, (), 0, 0, 0))
    print(best_terminal_node)

    # best_path = []
    # while best_terminal_node:
    #     best_path.append(best_terminal_node)
    #     best_terminal_node = best_terminal_node.parent
    #
    # for node in reversed(best_path):
    #     print(node)


if __name__ == "__main__":
    doctest.testmod()
    main()
