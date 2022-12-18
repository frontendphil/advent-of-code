use std::{fs::read_to_string, ops::Range, str::Lines};

fn main() {
    let contents = read_to_string("input.txt").unwrap();

    part_one(contents.lines());
    part_two(contents.lines());
}

fn part_one(contents: Lines) {
    let mut overlaps = 0;

    for assignments in contents {
        let mut iterator = assignments.split(",");

        let first = iterator.next().unwrap();
        let second = iterator.next().unwrap();

        let a = get_range(first);
        let b = get_range(second);

        if contains(&a, &b) || contains(&b, &a) {
            overlaps += 1;
        }
    }

    println!("Sum {overlaps}");
}

fn part_two(contents: Lines) {
    let mut count = 0;

    for assignments in contents {
        let mut iterator = assignments.split(",");

        let first = iterator.next().unwrap();
        let second = iterator.next().unwrap();

        let a = get_range(first);
        let b = get_range(second);

        if overlaps(&a, &b) || overlaps(&b, &a) {
            count += 1;
        }
    }

    println!("Overlaps: {count}");
}

fn overlaps(a: &Range<i32>, b: &Range<i32>) -> bool {
    return a.end >= b.start && a.end <= b.end;
}

fn contains(a: &Range<i32>, b: &Range<i32>) -> bool {
    return a.start <= b.start && a.end >= b.end;
}

fn get_range(input: &str) -> Range<i32> {
    let mut iterator = input.split("-");

    let start = iterator.next().unwrap().parse::<i32>().unwrap();
    let end = iterator.next().unwrap().parse::<i32>().unwrap();

    return start..end;
}
