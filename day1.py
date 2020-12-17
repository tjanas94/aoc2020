numbers = []
with open('day1.txt') as f:
    for line in f:
        numbers.append(int(line))

def part1():
    for x in numbers:
        for y in numbers:
            if x + y == 2020:
                return x * y

def part2():
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if x + y + z == 2020:
                    return x * y * z

print(part1())
print(part2())
