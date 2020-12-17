numbers = []

with open('day15.txt') as f:
    numbers = f.read().strip().split(',')

def part1():
    mem = {}
    current = None
    for i in range(2020):
        last = current
        if i < len(numbers):
            current = int(numbers[i])
        elif last not in mem:
            current = 0
        else:
            current = i - mem[last]

        mem[last] = i

    return current

def part2():
    mem = {}
    current = None
    for i in range(30000000):
        last = current
        if i < len(numbers):
            current = int(numbers[i])
        elif last not in mem:
            current = 0
        else:
            current = i - mem[last]

        mem[last] = i

    return current

print(part1())
print(part2())
