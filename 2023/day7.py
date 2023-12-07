import doctest
import re
from collections import Counter
from dataclasses import dataclass
from typing import List

card_power = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


@dataclass(order=True)
class Hand:
    type: int
    cards: List[int]


def parse_hand(hand: str) -> Hand:
    cards = [card_power[c] for c in hand]
    r = list((b, a) for (a, b) in Counter(cards).items())
    r.sort(reverse=True)
    return Hand(type=hand_type(r), cards=cards)


def hand_type(hand):
    if hand[0][0] == 5:
        return 10
    if hand[0][0] == 4:
        return 9
    if hand[0][0] == 3 and hand[1][0] == 2:
        return 8
    if hand[0][0] == 3:
        return 7
    if hand[0][0] == 2 and hand[1][0] == 2:
        return 6
    if hand[0][0] == 2:
        return 2
    return 1


def main():
    whitespace = re.compile(" +")

    hands = list()

    with open('day7_input.txt') as f:
        for line in f:
            hand, bid = whitespace.split(line.strip())
            bid = int(bid)
            hand = parse_hand(hand)
            hands.append((hand, bid))

    hands.sort()

    total = 0
    for rank, (hand, bid) in enumerate(hands, start=1):
        print(rank, hand, bid)
        total += rank * bid
    print(total)


if __name__ == "__main__":
    doctest.testmod()
    main()
