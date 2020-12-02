def countChars(input, char):
    count = 0

    for letter in input:
        if letter == char:
            count = count + 1

    return count


if __name__ == "__main__":
    with open('./input.txt') as f:
        valid = 0

        for policy, password in [tuple(line.split(': '))
                                 for line in f.readlines()]:

            occurenceRange, letter = policy.split(' ')
            minOccurence, maxOccurence = [
                int(part) for part in occurenceRange.split('-')]

            count = countChars(password, letter)

            if(count >= minOccurence and count <= maxOccurence):
                valid = valid + 1

        print(valid)
