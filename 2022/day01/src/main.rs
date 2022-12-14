use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Could not read inputs");
    let lines = contents.split("\n");

    let mut calories = Vec::new();
    let mut current = 0;

    for line in lines {
        if line.is_empty() {
            calories.push(current);
            current = 0
        } else {
            current += line.parse::<i32>().unwrap();
        }
    }

    let max = calories.iter().max().unwrap();

    println!("Max calories: {max}");

    calories.sort_by(|a, b| b.cmp(a));

    let top: i32 = calories[0..3].iter().sum();

    println!("Top 3: {top}");
}
