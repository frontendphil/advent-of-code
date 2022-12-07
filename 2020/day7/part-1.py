import re

bag_matcher = re.compile(r'(\d* )?(\w* \w*) bags?\.?$')


def bag_info(value):
    match = bag_matcher.match(value)

    return (int(match.group(1)), match.group(2)) if match.group(1) else (None, match.group(2))


def unpack_bags(bags, search, visited=[]):
    # print('searching for: ', search)
    # print('ignores: ', visited)

    matching_colors = []

    for color, package_rules in bags.items():
        if color in visited:
            continue

        if color == search:
            continue

        if search in package_rules:
            matching_colors = [*matching_colors, color]

    # print('matches: ', matching_colors, '\n')

    count = len(matching_colors)

    if count == 0:
        return 0, visited

    visits = [*visited, *matching_colors]

    for color in matching_colors:
        new_count, new_visited = unpack_bags(
            bags, color, visited=visits)

        visits = set([*visits, *new_visited])

        count = count + new_count

    return count, (visits)


if __name__ == "__main__":
    with open('./input.txt') as f:
        bags = {}

        for rule in f.readlines():
            outer, inner = rule.split(' contain ')

            _, parent = bag_info(outer)

            children = [bag_info(child.strip()) for child in inner.split(',')]

            bags[parent] = {}

            for count, child in children:
                bags[parent][child] = count

        count, _ = unpack_bags(bags, 'shiny gold')

        print(count)
