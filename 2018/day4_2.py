import re
from collections import defaultdict, Counter

start_pattern = re.compile('.* Guard #(\d+) begins shift')
sleep_pattern = re.compile('.* 00:(\d+)] falls asleep')
wake_pattern = re.compile('.* 00:(\d+)] wakes up')

sample = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""".split("\n")

with open('day4.txt') as f:
    lines = f.readlines()
    lines.sort()

    guards = defaultdict(Counter)
    guard = None
    start = None

    for line in lines:
        m = start_pattern.match(line)
        if m:
            guard = m[1]
            continue
        m = sleep_pattern.match(line)
        if m:
            start = int(m[1])
            continue
        m = wake_pattern.match(line)
        if m:
            end = int(m[1])
            g = guards[guard]
            for m in range(start, end):
                g[m] += 1
            continue
        print('unhandled line {}'.format(line))

    sleepiest = max(guards.keys(), key=lambda g: max(guards[g].values()))
    print('sleepiest:', sleepiest)
    best_minute = guards[sleepiest].most_common(2)
    print('best minute:', best_minute)
    print('=>', int(sleepiest) * best_minute[0][0])
