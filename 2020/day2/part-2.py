

if __name__ == "__main__":
    with open('./input.txt') as f:
        valid = 0

        for policy, password in [tuple(line.split(': '))
                                 for line in f.readlines()]:

            occurenceRange, letter = policy.split(' ')
            positionA, positionB = [
                int(part) - 1 for part in occurenceRange.split('-')]

            if(password[positionA] == letter and password[positionB] != letter or password[positionA] != letter and password[positionB] == letter):
                valid = valid + 1

        print(valid)
