groups = []
currentGroup = []

with open('day6.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            groups.append(currentGroup)
            currentGroup = []
            continue

        currentGroup.append(list(line))

    if currentGroup:
        groups.append(currentGroup)

def part1():
    for group in groups:
        [head, *tail] = group
        yield len(set(head).union(*tail))

def part2():
    for group in groups:
        [head, *tail] = group
        yield len(set(head).intersection(*tail))

print(sum(part1()))
print(sum(part2()))
