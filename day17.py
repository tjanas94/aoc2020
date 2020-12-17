cubes = {
    0: {}
}

with open('day17.txt') as f:
    for y, line in enumerate(f):
        for x, point in enumerate(line.strip()):
            if point == '#':
                if not y in cubes[0]:
                    cubes[0][y] = {}
                cubes[0][y][x] = True

def activeNeighbors(px, py, pz, cubes):
    result = 0
    for z in range(-1, 2):
        for y in range(-1, 2):
            for x in range(-1, 2):
                newX = px + x
                newY = py + y
                newZ = pz + z
                if (z != 0 or y != 0 or x != 0) and cubes.get(newZ, {}).get(newY, {}).get(newX, False):
                    result += 1

    return result

def part1():
    lastCubes = cubes

    for i in range(6):
        minLayer = min(lastCubes) - 1
        maxLayer = max(lastCubes) + 1
        minRow = None
        maxRow = None
        minColumn = None
        maxColumn = None

        for layer in lastCubes.values():
            currentMinRow = min(layer) - 1
            currentMaxRow = max(layer) + 1
            if minRow is None or currentMinRow < minRow:
                minRow = currentMinRow
            if maxRow is None or currentMaxRow > maxRow:
                maxRow = currentMaxRow

            for row in layer.values():
                currentMinColumn = min(row) - 1
                currentMaxColumn = max(row) + 1
                if minColumn is None or currentMinColumn < minColumn:
                    minColumn = currentMinColumn
                if maxColumn is None or currentMaxColumn > maxColumn:
                    maxColumn = currentMaxColumn

        newCubes = {}
        for z in range(minLayer, maxLayer + 1):
            for y in range(minRow, maxRow + 1):
                for x in range(minColumn, maxColumn + 1):
                    active = lastCubes.get(z, {}).get(y, {}).get(x, False)
                    neighbors = activeNeighbors(x, y, z, lastCubes)
                    newActive = (active and neighbors == 2) or neighbors == 3

                    if newActive:
                        if not z in newCubes:
                            newCubes[z] = {}
                        if not y in newCubes[z]:
                            newCubes[z][y] = {}
                        newCubes[z][y][x] = True

        lastCubes = newCubes

    result = 0
    for layer in lastCubes.values():
        for row in layer.values():
            for active in row.values():
                result += 1

    return result

print(part1())
