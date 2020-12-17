from functools import reduce
from math import ceil

timestamp = 0
buses = []

with open('day13.txt') as f:
    timestamp = int(f.readline())
    line = f.readline().strip().split(',')
    buses = [(idx, int(bus)) for idx, bus in enumerate(line) if bus != 'x']

def part1():
    times = []
    for idx, bus in buses:
        times.append([bus, bus * ceil(timestamp / bus)])

    result = sorted(times, key=lambda bus: bus[1])
    return result[0][0] * (result[0][1] - timestamp)

def findTimestamp(items):
    if len(items) == 1:
        return 0, items[0][1]

    timestamp, interval = findTimestamp(items[:-1])
    newInterval = 0
    found = 0
    while found < 2:
        if all((timestamp + idx) % bus == 0 for idx, bus in items):
            found += 1

        if found < 2:
            timestamp += interval
        if found == 1:
            newInterval += interval

    return timestamp - newInterval, newInterval

def part2():
    return findTimestamp(buses)[0]

print(part1())
print(part2())
