with open('day2.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    ws = dict()

    for line in lines:
        for i in range(1, len(line)):
            w = line[:(i - 1)] + '*' + line[i:]
            if w in ws:
                print('1: {}\n2: {}'.format(line, ws[w]))
                print("common: {}".format(w.replace('*', '')))
                exit()
            else:
                ws[w] = line
