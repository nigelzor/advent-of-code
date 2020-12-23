import doctest
from itertools import count, islice


def part1(cups, iterations):
    max_cup = max(cups)
    for _ in range(iterations):
        current, a, b, c = cups[0:4]
        rest = cups[4:]

        for d in count(1):
            lesser_label = current - d
            if lesser_label < 1:
                lesser_label += max_cup
            try:
                destination = rest.index(lesser_label) + 1
                break
            except ValueError:
                continue

        rest.insert(destination, c)
        rest.insert(destination, b)
        rest.insert(destination, a)
        rest.append(current)
        cups = rest

    return cups


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


def listify(cups):
    head = None
    tail = None
    index = dict()
    for c in cups:
        n = Node(c)
        index[c] = n
        if not head:
            head = n
            tail = n
        else:
            tail.next = n
            tail = n
    tail.next = head
    return head, tail, index


def part2(cups, iterations):
    head, tail, index = listify(cups)
    max_cup = max(cups)

    current = head

    for _ in range(iterations):
        a = current.next
        b = a.next
        c = b.next

        for d in count(1):
            lesser_label = current.value - d
            if lesser_label < 1:
                lesser_label += max_cup

            if lesser_label == a.value:
                continue
            elif lesser_label == b.value:
                continue
            elif lesser_label == c.value:
                continue

            destination = index[lesser_label]
            break

        current.next = c.next
        old_destination_next = destination.next
        destination.next = a
        c.next = old_destination_next

        current = current.next

    return index[1].next.value * index[1].next.next.value


def main():
    # cups = [int(x) for x in '389125467']
    cups = [int(x) for x in '589174263']

    result = part1(cups.copy(), 100)
    after_1 = result + result
    after_1 = after_1[after_1.index(1) + 1:][:8]
    print(''.join(str(x) for x in after_1))

    extended_cups = cups + list(islice(count(max(cups) + 1), 1000000 - len(cups)))
    print(part2(extended_cups, 10000000))


if __name__ == "__main__":
    doctest.testmod()
    main()
