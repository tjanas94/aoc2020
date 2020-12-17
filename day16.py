import re
from collections import defaultdict

sectionMatcher = re.compile('^(.+?):$')
ruleMatcher = re.compile('^(.+?): (\d+?)-(\d+?) or (\d+?)-(\d+?)$')

section = 'rules'
rules = {}
yourTicket = []
nearbyTickets = []

with open('day16.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        sectionMatch = sectionMatcher.match(line)
        if sectionMatch:
            section = sectionMatch.group(1)
        elif section == 'rules':
            name, *numbers = ruleMatcher.match(line).groups()
            rules[name] = numbers
        elif section == 'your ticket':
            yourTicket = line.split(',')
        elif section == 'nearby tickets':
            nearbyTickets.append(line.split(','))

def matchRule(value, rule):
    return int(rule[0]) <= int(value) <= int(rule[1]) or int(rule[2]) <= int(value) <= int(rule[3])

def part1():
    for ticket in nearbyTickets:
        for value in ticket:
            if not any(matchRule(value, rule) for rule in rules.values()):
                yield int(value)

def validTicket(ticket):
    for value in ticket:
        if not any(matchRule(value, rule) for rule in rules.values()):
            return False

    return True

def part2():
    validTickets = [ticket for ticket in nearbyTickets if validTicket(ticket)]
    matchingColumns = defaultdict(lambda: [])
    for name, rule in rules.items():
        for idx in range(len(validTickets[0])):
            if all(matchRule(ticket[idx], rule) for ticket in validTickets):
                matchingColumns[idx].append(name)

    columns = {}
    while True:
        head, *tail = sorted(matchingColumns.items(), key=lambda item: len(item[1]))
        idx, names = head
        name = names[0]
        columns[name] = idx
        matchingColumns = {}
        for key, value in tail:
            matchingColumns[key] = [rule for rule in value if rule != name]

        if not matchingColumns:
            break

    result = 1
    for name, idx in columns.items():
        if name.startswith('departure '):
            result *= int(yourTicket[idx])

    return result


print(sum(part1()))
print(part2())
