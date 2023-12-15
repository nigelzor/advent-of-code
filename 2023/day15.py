import doctest
from collections import OrderedDict


def hash(str):
    h = 0
    for s in str:
        h += ord(s)
        h *= 17
        h %= 256
    return h


def main():
    line = open('day15_input.txt').readline().strip()
    steps = line.split(',')

    print(f"Part 1: {sum(hash(s) for s in steps)}")

    boxes = []
    for _ in range(256):
        boxes.append(OrderedDict())

    for step in steps:
        if step.endswith('-'):
            label = step[:-1]
            box = hash(label)
            if label in boxes[box]:
                del boxes[box][label]
        else:
            label, focal_length = step.split('=')
            box = hash(label)
            boxes[box][label] = focal_length

    part2 = 0
    for box_index, box in enumerate(boxes, start=1):
        for lens_index, (label, focal_length) in enumerate(box.items(), start=1):
            part2 += box_index * lens_index * int(focal_length)

    print(f"Part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
