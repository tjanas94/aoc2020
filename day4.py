import re

passports = []
currentPassport = {}

with open('day4.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            passports.append(currentPassport)
            currentPassport = {}
            continue

        for part in line.split(' '):
            [key, value] = part.split(':')
            currentPassport[key] = value

    if currentPassport:
        passports.append(currentPassport)

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
heightRegex = re.compile('^(\d+)(cm|in)$')
hairColorRegex = re.compile('^#[0-9a-f]{6}$')
eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
pidRegex = re.compile('^\d{9}$')

def validateHeight(x):
    result = heightRegex.match(x)
    if not result:
        return False

    [height, unit] = result.groups()

    if unit == 'cm':
        return 150 <= int(height) <= 193

    if unit == 'in':
        return 59 <= int(height) <= 76

    return False

validators = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': validateHeight,
    'hcl': hairColorRegex.match,
    'ecl': eyeColors.count,
    'pid': pidRegex.match,
}

def part1():
    for passport in passports:
        yield all(field in passport for field in requiredFields)

def part2():
    for passport in passports:
        yield all(field in passport and validators[field](passport[field]) for field in requiredFields)

print(sum(part1()))
print(sum(part2()))
