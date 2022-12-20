use std::{collections::HashSet, fs::read_to_string};

fn main() {
    let contents = read_to_string("input.txt").unwrap();

    for line in contents.lines() {
        let start_of_packet = get_marker_index(line, 4);

        println!("start of packet {start_of_packet}");

        let start_of_message = get_marker_index(line, 14);

        println!("start of message {start_of_message}");
    }
}

fn get_marker_index(line: &str, desired_size: usize) -> i32 {
    let mut current_marker: Vec<char> = Vec::new();
    let mut index = -1;

    for char in line.chars() {
        index += 1;

        if !enough_elements(&mut current_marker, desired_size) {
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

fn enough_elements(marker: &mut Vec<char>, desired_size: usize) -> bool {
    return marker.len() == desired_size;
}

fn is_marker(marker: &mut Vec<char>) -> bool {
    let mut uniques = HashSet::new();

    let mut comparable = marker.clone();
    comparable.retain(|x| uniques.insert(*x));

    return marker.len() == comparable.len();
}
