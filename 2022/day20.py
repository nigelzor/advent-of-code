import doctest
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    index: int
    value: int
    previous: Any
    next: Any

    def remove(self):
        self.previous.next = self.next
        self.next.previous = self.previous

    def move_between(self, a, b):
        # print(f'{self.value} moves between {a.value} and {b.value}')

        assert a.next == b
        assert b.previous == a
        assert a != self
        assert b != self

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
        nodes[i] = Node(i, value * 811589153, None, None)
    for i in nodes.keys():
        nodes[i].next = nodes[(i + 1) % len(nodes)]
        nodes[i].previous = nodes[(i - 1) % len(nodes)]

    length_with_one_removed = len(nodes) - 1
    for _ in range(10):
        for n in nodes.values():
            if n.value > 0:
                value = n.value % length_with_one_removed
                if value:
                    n.remove()
                    insert_after = n
                    for _ in range(value):
                        insert_after = insert_after.next
                    n.move_between(insert_after, insert_after.next)

            elif n.value < 0:
                value = -n.value % length_with_one_removed
                if value:
                    n.remove()
                    insert_before = n
                    for _ in range(value):
                        insert_before = insert_before.previous
                    n.move_between(insert_before.previous, insert_before)

    coordinate_sum = 0
    n_after_zero = next(n for n in nodes.values() if n.value == 0)
    for _ in range(3):
        for _ in range(1000):
            n_after_zero = n_after_zero.next
        coordinate_sum += n_after_zero.value
    print(coordinate_sum)  # 3346



if __name__ == "__main__":
    doctest.testmod()
    main()
