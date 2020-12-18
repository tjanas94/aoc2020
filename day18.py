lines = []

with open('day18.txt') as f:
    for line in f:
        lines.append(line.strip())

def push(char, depth, groups):
    while depth:
        groups = groups[-1]
        depth -= 1

    groups.append(char)

def getGroups(line):
    groups = []
    depth = 0
    for char in line:
        if char == '(':
            push([], depth, groups)
            depth += 1
        elif char == ')':
            depth -= 1
        elif char != ' ':
            push(char, depth, groups)

    return groups

def calculate(groups):
    numbers = []
    operations = []
    for item in groups:
        isNumber = True

        if isinstance(item, list):
            numbers.append(calculate(item))
        elif item.isdigit():
            numbers.append(int(item))
        else:
            operations.append(item)
            isNumber = False

        if isNumber and len(operations):
            b = numbers.pop()
            a = numbers.pop()
            op = operations.pop()

            if op == '*':
                numbers.append(a * b)
            elif op == '+':
                numbers.append(a + b)

    return numbers.pop()

def calculateWithAddition(groups):
    numbers = []
    operations = []
    for item in groups:
        isNumber = True

        if isinstance(item, list):
            numbers.append(calculateWithAddition(item))
        elif item.isdigit():
            numbers.append(int(item))
        else:
            operations.append(item)
            isNumber = False

        if isNumber and len(operations) and operations[-1] == '+':
            b = numbers.pop()
            a = numbers.pop()
            operations.pop()
            numbers.append(a + b)

    for op in operations:
        b = numbers.pop()
        a = numbers.pop()
        numbers.append(a * b)

    return numbers.pop()

def part1():
    for line in lines:
        groups = getGroups(line)
        yield calculate(groups)

def part2():
    for line in lines:
        groups = getGroups(line)
        yield calculateWithAddition(groups)

print(sum(part1()))
print(sum(part2()))
