import doctest
import re


def paper_needed(l, w, h):
    """
    >>> paper_needed(2,3,4)
    58
    >>> paper_needed(1,1,10)
    43
    """
    sides = [l*w, w*h, h*l]
    smallest = min(sides)
    return smallest + 2 * sum(sides)


def ribbon_needed(l, w, h):
    """
    >>> ribbon_needed(2,3,4)
    34
    >>> ribbon_needed(1,1,10)
    14
    """
    bow = l * w * h
    sides = [2*(l+w), 2*(w+h), 2*(h+l)]
    smallest = min(sides)
    return smallest + bow


def main():
    p = re.compile(r'(\d+)x(\d+)x(\d+)')
    with open('day2_input.txt') as f:
        total_paper = 0
        total_ribbon = 0
        for line in f:
            l, w, h = [int(v) for v in p.match(line).groups()]
            total_paper += paper_needed(l, w, h)
            total_ribbon += ribbon_needed(l, w, h)

    print(total_paper)
    print(total_ribbon)


if __name__ == "__main__":
    doctest.testmod()
    main()
