numbers = []

with open('day9.txt') as f:
    for line in f:
        numbers.append(int(line));

def checkSum(number, part):
    for x in part:
        for y in part:
            if x + y == number:
                return True

    return False

def part1():
    for idx, number in enumerate(numbers):
        if idx < 25:
            continue

        part = numbers[(idx - 25):idx]
        if not checkSum(number, part):
            return number

def part2():
    for start, x in enumerate(numbers):
        for end, y in enumerate(numbers):
            part = numbers[start:end]
            if sum(part) == foundNumber:
                return max(part) + min(part)

foundNumber = part1()
print(foundNumber)
print(part2())
