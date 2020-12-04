import re


def parse_fields(line):
    fields = {}
    candidates = line.split(' ')

    for candidate in candidates:
        key, value = candidate.split(':')

        fields[key] = value.strip()

    return fields


requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def validateDigit(min, max, value):
    return value >= min and value <= max


validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
validHairColors = re.compile(r'^#[0-9a-f]{6}$')
validPassportId = re.compile(r'^\d{9}$')


def validateHeight(height):
    match = re.search(r'(\d*)(in|cm)', height)

    if(match):
        value = match.group(1)
        unit = match.group(2)

        if(unit == 'cm'):
            return validateDigit(150, 193, int(value))

        return validateDigit(59, 76, int(value))

    return False


validators = {
    "byr": lambda value: validateDigit(1920, 2002, int(value)),
    "iyr": lambda value: validateDigit(2010, 2020, int(value)),
    "eyr": lambda value: validateDigit(2020, 2030, int(value)),

    "hgt": lambda value: validateHeight(value),
    "hcl": lambda value: validHairColors.match(value),
    "ecl": lambda value: value in validEyeColors,
    "pid": lambda value: validPassportId.match(value),

    "cid": lambda value: True
}


def isValidPassport(passport):
    return all(field in passport and validators[field](passport[field]) for field in requiredFields)


if __name__ == "__main__":
    with open('./input.txt') as f:
        passports = []
        passport = {}

        for line in f.readlines():
            if(line.strip() == ''):
                passports.append(passport)

                passport = {}

                continue

            passport = {**passport, **parse_fields(line)}

        if(passport):
            # add last passport
            passports.append(passport)

        print('All passports %d' % len(passports))

        validPassports = filter(isValidPassport, passports)

        print('Valid passports %d' % len(list(validPassports)))
