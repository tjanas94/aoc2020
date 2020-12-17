rules = {}

with open('day7.txt') as f:
    for line in f:
        key, content = line.strip('\n.').replace(' bags', '').replace(' bag', '').split(' contain ');

        rule = {}
        for part in content.split(', '):
            if part == 'no other':
                continue
            number, color = part.split(' ', 1)
            rule[color] = number

        rules[key] = rule

def part1(key):
    result = set()
    for color, rule in rules.items():
        if key in rule:
            result.add(color)
            result.update(part1(color))

    return result

def part2(key):
    return sum(int(number) * (1 + part2(color)) for color, number in rules[key].items())

print(len(part1('shiny gold')))
print(part2('shiny gold'))
