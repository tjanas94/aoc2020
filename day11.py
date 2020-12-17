from copy import deepcopy

lines = []

with open('day11.txt') as f:
    for line in f:
        lines.append(list(line.strip()));

def adjacent(x, y, lines):
    positions = [
        [x - 1, y - 1],
        [x, y - 1],
        [x + 1, y - 1],
        [x - 1, y],
        [x + 1, y],
        [x - 1, y + 1],
        [x, y + 1],
        [x + 1, y + 1],
    ]

    result = 0
    for posX, posY in positions:
        if -1 < posX < len(lines[y]) and -1 < posY < len(lines) and lines[posY][posX] == '#':
            result += 1

    return result

def visible(x, y, lines):
    positions = [
        [-1, -1],
        [0, -1],
        [1, -1],
        [-1, 0],
        [1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
    ]

    result = 0
    for diffX, diffY in positions:
        posX = x + diffX
        posY = y + diffY

        while -1 < posX < len(lines[y]) and -1 < posY < len(lines):
            if lines[posY][posX] == 'L':
                break
            elif lines[posY][posX] == '#':
                result += 1
                break

            posX += diffX
            posY += diffY

    return result

def part1():
    changed = True
    result = deepcopy(lines)
    while changed:
        changed = False
        clonedLines = deepcopy(result)
        for y, line in enumerate(clonedLines):
            for x, value in enumerate(line):
                if value == 'L' and adjacent(x, y, clonedLines) == 0:
                    changed = True
                    result[y][x] = '#'
                elif value == '#' and adjacent(x, y, clonedLines) >= 4:
                    changed = True
                    result[y][x] = 'L'

    return sum(line.count('#') for line in result)

def part2():
    changed = True
    result = deepcopy(lines)
    while changed:
        changed = False
        clonedLines = deepcopy(result)
        for y, line in enumerate(clonedLines):
            for x, value in enumerate(line):
                if value == 'L' and visible(x, y, clonedLines) == 0:
                    changed = True
                    result[y][x] = '#'
                elif value == '#' and visible(x, y, clonedLines) >= 5:
                    changed = True
                    result[y][x] = 'L'

    return sum(line.count('#') for line in result)

print(part1())
print(part2())
