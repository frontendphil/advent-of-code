import re

bag_matcher = re.compile(r'(\d* )?(\w* \w*) bags?\.?$')


def bag_info(value):
    match = bag_matcher.match(value)

    return (int(match.group(1)), match.group(2)) if match.group(1) else (None, match.group(2))


def count_bags(bags, search):
    if bags[search] == None:
        return 1

    count = 1

    for color, package_rules in bags.items():
        if color == search:
            for packaged_color, packaged_count in package_rules.items():
                if packaged_count == None:
                    continue

                count = count + packaged_count * \
                    count_bags(bags, packaged_color)

    return count


if __name__ == "__main__":
    with open('./input.txt') as f:
        bags = {}

        for rule in f.readlines():
            outer, inner = rule.split(' contain ')

            _, parent = bag_info(outer)

            children = [bag_info(child.strip()) for child in inner.split(',')]

            bags[parent] = {}

            for count, child in children:
                if count == None:
                    bags[parent] = None

                    continue

                bags[parent][child] = count

        # subtract 1 to exclude the shiny gold bag itself
        count = count_bags(bags, 'shiny gold') - 1

        print(count)
