import re

lines = []
matcher = re.compile('^(mask|mem)(?:\[(\d+)\])? = (.+)$')

with open('day14.txt') as f:
    for line in f:
        result = matcher.match(line.strip())
        lines.append(result.groups())

def part1():
    andMask = 0
    orMask = 0
    mem = {}
    for name, index, value in lines:
        if name == 'mask':
            andMask = int(value.replace('X', '1'), 2)
            orMask = int(value.replace('X', '0'), 2)
        elif name == 'mem':
            mem[index] = int(value) & andMask | orMask

    return sum(mem.values())

def splitIndex(indexBits, mask):
    if mask.count('X') == 0:
        return [int(''.join(indexBits), 2)]

    pos = mask.index('X')
    mask = mask.replace('X', '0', 1)
    leftIndex = indexBits.copy()
    leftIndex[pos] = '0'
    rightIndex = indexBits.copy()
    rightIndex[pos] = '1'
    return [*splitIndex(leftIndex, mask), *splitIndex(rightIndex, mask)]

def calculateIndexes(index, mask):
    indexBits = list(format(int(index), '036b'))
    for i, c in enumerate(mask):
        if c == '1':
            indexBits[i] = '1'

    return splitIndex(indexBits, mask)

def part2():
    mask = ''
    mem = {}
    for name, index, value in lines:
        if name == 'mask':
            mask = value
        elif name == 'mem':
            for index in calculateIndexes(index, mask):
                mem[index] = int(value)

    return sum(mem.values())

print(part1())
print(part2())
