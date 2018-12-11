gsn = 7400

def power(x, y):
    rid = x + 10
    pl = rid * y
    pl += gsn
    pl *= rid
    pl = (pl % 1000) // 100
    return pl - 5

# gsn = 8
# print(power(3, 5))
# gsn = 57
# print(power(122, 79))


ps = dict()
for x in range(1, 300 + 1):
    for y in range(1, 300 + 1):
        ps[x, y] = power(x, y)


def maxp(size):
    max = None
    max_c = None
    for x in range(1, 300 + 1 - (size - 1)):
        for y in range(1, 300 + 1 - (size - 1)):
            p = 0
            for xa in range(x, x + size):
                for ya in range(y, y + size):
                    p += ps[xa, ya]
            if max is None or p > max:
                max = p
                max_c = (x, y)
    return max_c, max


for s in range(1, 300):
    print('max power at size', s, maxp(s))
