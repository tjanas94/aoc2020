import re

ruleMatcher = re.compile('^(\d+): (.+)$')

rules = {}
messages = []

with open('day19.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        match = ruleMatcher.match(line)
        if match:
            name, rule = match.groups()
            rules[name] = rule.replace('"', '').split(' ')
        else:
            messages.append(line)

def unwrapRule(name, depth = 0):
    result = ''
    for part in rules[name]:
        if part.isdigit():
            if part == name:
                depth += 1
            if depth < 6:
                result += unwrapRule(part, depth)
        else:
            result += part

    return f'(?:{result})'

def part1():
    unwrapped = unwrapRule('0')
    for message in messages:
        yield bool(re.match(f'^{unwrapped}$', message))

def part2():
    rules['8'] = ['42', '|', '42', '8']
    rules['11'] = ['42', '31', '|', '42', '11', '31']
    unwrapped = unwrapRule('0')
    for message in messages:
        yield bool(re.match(f'^{unwrapped}$', message))

print(sum(part1()))
print(sum(part2()))
