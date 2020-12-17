lines = []
with open('day3.txt') as f:
    for line in f:
        lines.append(line.strip())

def isTree(x, y):
    length = len(lines[y])
    return lines[y][x % length] == '#'

def part1(slopeX, slopeY):
    x = slopeX
    y = slopeY
    while y < len(lines):
        yield isTree(x, y)
        x += slopeX
        y += slopeY

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

def part2():
    result = 1
    for (x, y) in slopes:
        result *= sum(part1(x, y))

    return result


print(sum(part1(3, 1)))
print(part2())
