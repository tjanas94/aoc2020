program = []

with open('day8.txt') as f:
    for line in f:
        program.append(line.strip('\n.').split(' '));

def execute(program):
    log = set()
    loop = False
    idx = 0
    acc = 0

    while idx < len(program):
        if idx in log:
            loop = True
            break

        log.add(idx)
        instruction, argument = program[idx]

        if instruction == 'acc':
            idx += 1
            acc += int(argument)
        elif instruction == 'jmp':
            idx += int(argument)
        elif instruction == 'nop':
            idx += 1

    return acc, loop

def part1():
    return execute(program)[0]

def part2():
    changes = {
        'jmp': 'nop',
        'nop': 'jmp'
    }
    for idx, line in enumerate(program):
        instruction, argument = line
        if instruction in changes:
            copy = [*program]
            copy[idx] = [
                changes[instruction],
                argument,
            ]

            acc, loop = execute(copy)
            if not loop:
                return acc

print(part1())
print(part2())
