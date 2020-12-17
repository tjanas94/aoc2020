cubes = {
    0: {
        0: {}
    }
}

with open('day17.txt') as f:
    for y, line in enumerate(f):
        for x, point in enumerate(line.strip()):
            if point == '#':
                if not y in cubes[0][0]:
                    cubes[0][0][y] = {}
                cubes[0][0][y][x] = True

def activeNeighbors(px, py, pz, pw, cubes):
    result = 0
    for w in range(-1, 2):
        for z in range(-1, 2):
            for y in range(-1, 2):
                for x in range(-1, 2):
                    newX = px + x
                    newY = py + y
                    newZ = pz + z
                    newW = pw + w
                    if (w != 0 or z != 0 or y != 0 or x != 0) and cubes.get(newW, {}).get(newZ, {}).get(newY, {}).get(newX, False):
                        result += 1

    return result

def part1():
    lastCubes = cubes

    for i in range(6):
        minCube = min(lastCubes) - 1
        maxCube = max(lastCubes) + 1
        minLayer = None
        maxLayer = None
        minRow = None
        maxRow = None
        minColumn = None
        maxColumn = None

        for cube in lastCubes.values():
            currentMinLayer = min(cube) - 1
            currentMaxLayer = max(cube) + 1
            if minLayer is None or currentMinLayer < minLayer:
                minLayer = currentMinLayer
            if maxLayer is None or currentMaxLayer > maxLayer:
                maxLayer = currentMaxLayer

            for layer in cube.values():
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
        for w in range(minCube, maxCube + 1):
            for z in range(minLayer, maxLayer + 1):
                for y in range(minRow, maxRow + 1):
                    for x in range(minColumn, maxColumn + 1):
                        active = lastCubes.get(w, {}).get(z, {}).get(y, {}).get(x, False)
                        neighbors = activeNeighbors(x, y, z, w, lastCubes)
                        newActive = (active and neighbors == 2) or neighbors == 3

                        if newActive:
                            if not w in newCubes:
                                newCubes[w] = {}
                            if not z in newCubes[w]:
                                newCubes[w][z] = {}
                            if not y in newCubes[w][z]:
                                newCubes[w][z][y] = {}
                            newCubes[w][z][y][x] = True

        lastCubes = newCubes

    result = 0
    for cube in lastCubes.values():
        for layer in cube.values():
            for row in layer.values():
                for active in row.values():
                    result += 1

    return result

print(part1())
