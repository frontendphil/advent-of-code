use std::{collections::HashSet, fs::read_to_string};

fn main() {
    let contents = read_to_string("input.txt").unwrap();

    for line in contents.lines() {
        let index = get_marker_index(line);

        println!("Index {index}");
    }
}

fn get_marker_index(line: &str) -> i32 {
    let mut current_marker: Vec<char> = Vec::new();
    let mut index = -1;

    for char in line.chars() {
        index += 1;

        if !enough_elements(&mut current_marker) {
            println!("Add initial {char}");
            current_marker.push(char);
        } else if is_marker(&mut current_marker) {
            println!("Found index {index}");
            return index;
        } else {
            cycle_marker(&mut current_marker, char);
        }
    }

    return 0;
}

fn cycle_marker(marker: &mut Vec<char>, char: char) {
    let removed = marker.remove(0);
    marker.push(char);

    println!("Remove {removed} and inserted {char}");
}

fn enough_elements(marker: &mut Vec<char>) -> bool {
    return marker.len() == 4;
}

fn is_marker(marker: &mut Vec<char>) -> bool {
    let mut uniques = HashSet::new();

    let mut comparable = marker.clone();
    comparable.retain(|x| uniques.insert(*x));

    return marker.len() == comparable.len();
}
