use std::{fs::read_to_string, ops::Range};

fn main() {
    let contents = read_to_string("input.txt").unwrap();

    let mut overlaps = 0;

    for assignments in contents.lines() {
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

fn contains(a: &Range<i32>, b: &Range<i32>) -> bool {
    return a.start <= b.start && a.end >= b.end;
}

fn get_range(input: &str) -> Range<i32> {
    let mut iterator = input.split("-");

    let start = iterator.next().unwrap().parse::<i32>().unwrap();
    let end = iterator.next().unwrap().parse::<i32>().unwrap();

    return start..end;
}
