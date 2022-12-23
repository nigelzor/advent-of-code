import doctest
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    index: int
    value: int
    previous: Any
    next: Any

    def move_between(self, a, b):
        print(f'{self.value} moves between {a.value} and {b.value}')

        assert a.next == b
        assert b.previous == a

        # ???
        if self == a or self == b:
            return

        self.previous.next = self.next
        self.next.previous = self.previous
        self.previous = a
        self.next = b
        a.next = self
        b.previous = self

    def __hash__(self):
        return self.index

    def __repr__(self):
        return f'Node(index: {self.index}, value: {self.value}, previous: {self.previous.index}, next: {self.next.index})'


def main():
    with open('day20_input.txt') as f:
        input = [int(line) for line in f]

    nodes = dict()
    for i, value in enumerate(input):
        nodes[i] = Node(i, value, None, None)
    for i in nodes.keys():
        nodes[i].next = nodes[(i + 1) % len(nodes)]
        nodes[i].previous = nodes[(i - 1) % len(nodes)]

    def print_nodes():
        as_list = []
        node = nodes[0]
        while len(as_list) < len(nodes):
            as_list.append(node)
            node = node.next
        print([n.value for n in as_list])

    print_nodes()

    for n in nodes.values():
        value = n.value
        if value > 0:
            insert_after = n
            for _ in range(value):
                insert_after = insert_after.next
                if insert_after == n:
                    insert_after = insert_after.next
            n.move_between(insert_after, insert_after.next)

        elif value < 0:
            insert_before = n
            for _ in range(-value):
                insert_before = insert_before.previous
                if insert_before == n:
                    insert_before = insert_before.previous
            n.move_between(insert_before.previous, insert_before)

        else:
            print(f'{n.value} does not move')

    print_nodes()

    part1 = 0
    n_after_zero = next(n for n in nodes.values() if n.value == 0)
    for _ in range(3):
        for _ in range(1000):
            n_after_zero = n_after_zero.next
        part1 += n_after_zero.value
    print(part1)



if __name__ == "__main__":
    doctest.testmod()
    main()
