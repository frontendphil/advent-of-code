use std::{fs::read_to_string, ops::Index};

fn main() {
    let contents = read_to_string("input.txt").unwrap();

    let mut priorities = 0;

    for rucksack in contents.lines() {
        let pivot = rucksack.len();

        let first_compartment = &rucksack[..pivot];
        let second_compartment = &rucksack[pivot..];

        let duplicate = find_duplicate(first_compartment, second_compartment);

        let priority = get_priority(duplicate);
        priorities += priority;
    }
}

fn find_duplicate(a: &str, b: &str) -> char {
    for char in a.chars() {
        if b.contains(char) {
            return char;
        }
    }

    todo!()
}

static CHARS: [char; 26] = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z',
];

fn get_priority(letter: char) -> usize {
    if CHARS.contains(&letter) {
        return get_index(letter) + 1;
    }

    let lowercase_letter = letter.to_ascii_lowercase();

    if CHARS.contains(&lowercase_letter) {
        return 2 * get_index(lowercase_letter) + 1;
    }

    todo!()
}

fn get_index(letter: char) -> usize {
    return CHARS.iter().position(|&item| item == letter).unwrap();
}
