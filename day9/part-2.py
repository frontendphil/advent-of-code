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


def find_sum_range(list, outlier, start_index=0):
    current_count = 0

    for index, entry in enumerate(list[start_index:]):
        if entry == outlier:
            return []

        current_count = current_count + entry

        if current_count > outlier:
            return find_sum_range(list, outlier, start_index=start_index + 1)

        if current_count == outlier:

            return list[start_index:index + start_index + 1]


if __name__ == "__main__":
    with open('./input.txt') as f:
        input = [int(line.strip())
                 for line in f.readlines()]

        outlier = find_first_outlier(input)

        sum_range = find_sum_range(input, outlier)

        print(min(*sum_range) + max(*sum_range))
