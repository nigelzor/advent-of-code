from collections import deque


def printm(cp, m):
    c = deque(m)
    c.reverse()
    z = c.index(0)
    c.rotate(-z)
    p = list(c)
    p[-z] = '({})'.format(p[-z])
    print(cp + 1, p)


def highscore(players, final):
    score = [0 for p in range(players)]
    player = 0
    marbles = deque([0])
    current = 1

    while current <= final:
        if current % 23 == 0:
            score[player] += current
            marbles.rotate(-7)
            removed = marbles.pop()
            score[player] += removed
            # print('remove', removed)
        else:
            marbles.rotate(2)
            marbles.append(current)
        # printm(player, marbles)

        current += 1
        player = (player + 1) % players

    return max(score)


print(10, 1618, highscore(10, 1618))
print(13, 7999, highscore(13, 7999))

print(463, 71787, highscore(463, 71787))
print(463, 71787 * 100, highscore(463, 71787 * 100))

