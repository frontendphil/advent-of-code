if __name__ == "__main__":
    with open('./input.txt') as f:
        adapters = [0, *sorted([int(line.strip()) for line in f.readlines()])]

        count_1 = 0

        # the built-in adapter
        count_3 = 1

        for index, adapter in enumerate(adapters[1:]):
            predecessor = adapters[index]

            count_1 = count_1 + (1 if adapter - predecessor == 1 else 0)
            count_3 = count_3 + (1 if adapter - predecessor == 3 else 0)

        print('#1 jumps: %d, #3 jumps: %d' % (count_1, count_3))
        print('#1 * #3: %d' % (count_1 * count_3))
