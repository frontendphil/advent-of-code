def sums_up(desired_result, options, candidate):
    return any([desired_result == candidate + x for x in options])


chunk_size = 25


def find_first_outlier(list, index=chunk_size):
    if index == len(list):
        return None

    preamble = list[index - chunk_size:index]

    current = list[index]

    if not any([sums_up(current, preamble, x) for x in preamble]):
        return current

    return find_first_outlier(list, index=index + 1)


if __name__ == "__main__":
    with open('./input.txt') as f:
        print(find_first_outlier([int(line.strip())
                                  for line in f.readlines()]))
