def find_trees(forest, step_size, skip_size=1):
    index = 0
    trees = 0

    for i, line in enumerate(forest):
        if i == 0:
            continue

        if i % skip_size != 0:
            continue

        index = (index + step_size) % (len(line) - 1)

        if line[index] == '#':
            trees = trees + 1

    print("Found %d trees for step size %d and skip size %d" %
          (trees, step_size, skip_size))

    return trees


if __name__ == "__main__":
    with open('./input.txt') as f:
        forest = f.readlines()

        trees = find_trees(forest, step_size=1) * find_trees(forest, step_size=3) * find_trees(
            forest, step_size=5) * find_trees(forest, step_size=7) * find_trees(forest, step_size=1, skip_size=2)

        print(trees)
