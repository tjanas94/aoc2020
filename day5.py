boardings = []

with open('day5.txt') as f:
    for line in f:
        boardings.append(line.strip())

def decodeBoarding(boarding):
    binary = boarding.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')

    return int(binary, 2)

def part1():
    for boarding in boardings:
        yield decodeBoarding(boarding)

def part2():
    seats = sorted(part1())
    previous = 0
    for seat in seats:
        if previous and previous + 1 != seat:
            return previous + 1
        previous = seat

print(max(part1()))
print(part2())
