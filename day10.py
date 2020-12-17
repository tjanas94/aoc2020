numbers = []

with open('day10.txt') as f:
    for line in f:
        numbers.append(int(line));

adapters = sorted(numbers)
adapters.insert(0, 0)
adapters.append(max(numbers) + 3)

def part1():
    diff = [0, 0, 0, 0]
    for idx, adapter in enumerate(adapters[:-1]):
        diff[adapters[idx + 1] - adapter] += 1

    return diff[1] * diff[3]

def part2():
    groups = {}
    for adapter in adapters:
        group = []
        for adapter2 in adapters:
            if 1 <= adapter2 - adapter <= 3:
                group.append(adapter2)

        if group:
            groups[adapter] = group

    results = {}
    for key, group in reversed(groups.items()):
        results[key] = sum(results.get(item, 1) for item in group)

    return results[0]


print(part1())
print(part2())
