lines = []
directions = ['N', 'E', 'S', 'W']

with open('day12.txt') as f:
    for line in f:
        line = line.strip()
        action = line[0]
        value = int(line[1:])
        lines.append([action, value]);

def part1():
    x = 0
    y = 0
    direction = 1

    for action, value in lines:
        if action == 'F':
            action = directions[int(direction)]
        elif action == 'L':
            direction += (360 - value) / 90
            direction %= 4
        elif action == 'R':
            direction += value / 90
            direction %= 4

        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value

    return abs(x) + abs(y)

def rotate(x, y, times):
    for i in range(int(times)):
        x, y = y, -x

    return x, y

def part2():
    wx = 10
    wy = 1
    x = 0
    y = 0

    for action, value in lines:
        if action == 'F':
            x += wx * value
            y += wy * value
        elif action == 'L':
            wx, wy = rotate(wx, wy, (360 - value) / 90)
        elif action == 'R':
            wx, wy = rotate(wx, wy, value / 90)

        if action == 'N':
            wy += value
        elif action == 'S':
            wy -= value
        elif action == 'E':
            wx += value
        elif action == 'W':
            wx -= value

    return abs(x) + abs(y)

print(part1())
print(part2())
