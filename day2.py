import re

matcher = re.compile('(\d+)-(\d+) (\w): (\w+)')

policies = []
with open('day2.txt') as f:
    for line in f:
        result = matcher.match(line)
        policies.append(result.groups())

def part1():
    for policy in policies:
        start, end, letter, password = policy
        yield int(start) <= password.count(letter) <= int(end)

def part2():
    for policy in policies:
        start, end, letter, password = policy
        yield (password[int(start) - 1] == letter) != (password[int(end) - 1] == letter)

print(sum(part1()))
print(sum(part2()))
