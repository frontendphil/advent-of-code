def parse_fields(line):
    fields = {}
    candidates = line.split(' ')

    for candidate in candidates:
        key, value = candidate.split(':')

        fields[key] = value.strip()

    return fields


requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def isValidPassport(passport):
    return all(field in passport for field in requiredFields)


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

        print('All passports %d' % len(passports))

        validPassports = filter(isValidPassport, passports)

        print('Valid passports %d' % len(list(validPassports)))
