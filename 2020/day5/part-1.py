import re
import math

col_row_matcher = re.compile(r'^(.{7})(.{3})$')


def disect_partition(partition, lower, upper, min, max):
    if(len(partition) == 1):
        return max if partition == upper else min

    if(partition.startswith(lower)):
        return disect_partition(partition[1:], lower, upper, min, min + math.floor((max - min) / 2))

    return disect_partition(partition[1:], lower, upper, min + math.ceil((max - min) / 2), max)


def get_column_id(partition):
    return disect_partition(partition, lower="L", upper="R", min=0, max=7)


def get_row_id(partition, min=0, max=127):
    return disect_partition(partition, lower="F", upper="B", min=0, max=127)


def get_seat_id(partition):
    match = col_row_matcher.match(partition)

    row_partition = match.group(1)
    column_partition = match.group(2)

    return get_row_id(row_partition) * 8 + get_column_id(column_partition)


if __name__ == "__main__":
    with open('./input.txt') as f:
        seat_id = max([get_seat_id(line) for line in f.readlines()])

        print(seat_id)
