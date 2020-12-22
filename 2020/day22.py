import doctest
from collections import deque
from itertools import count, islice


def head(deck: deque, n: int):
    """
    >>> head(deque([1, 2, 3]), 2)
    deque([1, 2])
    """
    return deque(islice(deck, n))


def score(cards: deque[int]):
    return sum((n + 1) * c for n, c in enumerate(reversed(cards)))


def part1(deck_a, deck_b):
    while len(deck_a) and len(deck_b):
        a = deck_a.popleft()
        b = deck_b.popleft()
        if a > b:
            deck_a.append(a)
            deck_a.append(b)
        elif b > a:
            deck_b.append(b)
            deck_b.append(a)
        else:
            raise Exception('tie')

    score_a = score(deck_a)
    score_b = score(deck_b)
    print(max(score_a, score_b))


def part2(deck_a, deck_b, game_counter=count(1)):
    game = next(game_counter)
    # print(f'=== Game {game} ===')
    seen = set()
    for round in count(1):
        # print(f'-- Round {round} (Game {game}) --')
        k = (tuple(deck_a), tuple(deck_b))
        if k in seen:
            return '1'
        else:
            seen.add(k)

        a = deck_a.popleft()
        b = deck_b.popleft()
        if a <= len(deck_a) and b <= len(deck_b):
            winner = part2(head(deck_a, a), head(deck_b, b), game_counter)
        elif a > b:
            winner = '1'
        elif b > a:
            winner = '2'
        else:
            raise Exception('tie')

        # print(f'Player {winner} wins round {round} of game {game}!')
        if winner == '1':
            deck_a.append(a)
            deck_a.append(b)
        else:
            deck_b.append(b)
            deck_b.append(a)

        if len(deck_a) == 0 or len(deck_b) == 0:
            break

    # print(f'The winner of game {game} is player {winner}!')
    if game == 1:
        # print('== Post-game results ==')
        # print('Player 1\'s deck: ' + ', '.join(str(c) for c in deck_a))
        # print('Player 2\'s deck: ' + ', '.join(str(c) for c in deck_b))
        print(score(deck_a), score(deck_b))

    return winner


def main():
    decks = []
    with open('day22_input.txt') as file:
        for line in file:
            if line.startswith('Player'):
                cards = deque()
                decks.append(cards)
            elif line.strip():
                cards.append(int(line))

    part1(decks[0].copy(), decks[1].copy())
    part2(decks[0].copy(), decks[1].copy())


if __name__ == "__main__":
    doctest.testmod()
    main()
