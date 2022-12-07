if __name__ == "__main__":
    with open('./input.txt') as f:
        numbers = [int(line) for line in f.readlines()]

        result = 0

        for i in range(len(numbers)):
            a = numbers[i]

            for j in range(len(numbers)):
                b = numbers[j]

                for k in range(len(numbers)):
                    c = numbers[k]

                    if(a + b + c == 2020):
                        result = a * b * c

        print(result)
