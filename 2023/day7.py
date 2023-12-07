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

card_power_2 = card_power.copy()
card_power_2["J"] = 1


@dataclass(order=True)
class Hand:
    type: int
    cards: List[int]


def parse_hand(hand: str) -> Hand:
    cards = [card_power[c] for c in hand]

    counts = list(Counter(cards).values())
    counts.sort(reverse=True)

    return Hand(type=hand_type(counts), cards=cards)


def hand_type(counts):
    if counts[0] == 5:
        return 10
    if counts[0] == 4:
        return 9
    if counts[0] == 3 and counts[1] == 2:
        return 8
    if counts[0] == 3:
        return 7
    if counts[0] == 2 and counts[1] == 2:
        return 6
    if counts[0] == 2:
        return 2
    return 1


def parse_hand_2(hand: str) -> Hand:
    cards = [card_power_2[c] for c in hand]
    return Hand(type=hand_type_2(cards), cards=cards)


def hand_type_2(cards):
    jokers = sum(1 for c in cards if c == 1)
    if jokers >= 4:
        # can always make a five-of-a-kind
        return 10

    counts = list(Counter(c for c in cards if c != 1).values())
    counts.sort(reverse=True)
    counts[0] += jokers
    return hand_type(counts)


def winnings(hands):
    hands.sort()
    total = 0
    for rank, (hand, bid) in enumerate(hands, start=1):
        # print(rank, hand, bid)
        total += rank * bid
    return total


def main():
    whitespace = re.compile(" +")

    hands_1 = list()
    hands_2 = list()

    with open('day7_input.txt') as f:
        for line in f:
            hand, bid = whitespace.split(line.strip())
            bid = int(bid)
            hands_1.append((parse_hand(hand), bid))
            hands_2.append((parse_hand_2(hand), bid))

    print(f"Part 1: {winnings(hands_1)}")
    print(f"Part 2: {winnings(hands_2)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
