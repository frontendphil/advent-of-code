if __name__ == "__main__":
    with open('./input.txt') as f:
        index = 0
        trees = 0

        for i, line in enumerate(f.readlines()):
            if i == 0:
                continue

            index = (index + 3) % (len(line) - 1)

            if line[index] == '#':
                trees = trees + 1

        print(trees)

# 181
