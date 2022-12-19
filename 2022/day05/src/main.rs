use std::fs::read_to_string;

use regex::Regex;

fn main() {
    let contents = read_to_string("input.txt").unwrap();

    let re = Regex::new(r"move (?P<times>\d+) from (?P<from>\d+) to (?P<to>\d+)").unwrap();
    let mut stacks = init_stacks();

    for line in contents.lines() {
        if !re.is_match(line) {
            println!("does not match");
            continue;
        }

        let matches = re.captures(line).unwrap();

        let times = matches["times"].parse::<usize>().unwrap();
        let from = matches["from"].parse::<usize>().unwrap() - 1;
        let to = matches["to"].parse::<usize>().unwrap() - 1;

        println!("move {times} from {from} to {to}");

        for _i in 0..times {
            let item = get_item(&mut stacks, from);

            println!("item {item}");

            insert_item(&mut stacks, to, item);
        }
    }

    let top_values = get_top_values(&mut stacks);
    let top_string = top_values.map(|x| x.to_string()).join("");

    println!("Top {top_string}")
}

fn get_top_values(stacks: &mut [Vec<char>; 9]) -> [char; 9] {
    return [
        stacks[0].remove(0),
        stacks[1].remove(0),
        stacks[2].remove(0),
        stacks[3].remove(0),
        stacks[4].remove(0),
        stacks[5].remove(0),
        stacks[6].remove(0),
        stacks[7].remove(0),
        stacks[8].remove(0),
    ];
}

fn get_item(stacks: &mut [Vec<char>; 9], index: usize) -> char {
    let source = &mut stacks[index];

    return source.remove(0);
}

fn insert_item(stacks: &mut [Vec<char>; 9], index: usize, item: char) {
    let target = &mut stacks[index];

    target.insert(0, item);
}

fn init_stacks() -> [Vec<char>; 9] {
    return [
        vec!['P', 'V', 'Z', 'W', 'D', 'T'],
        vec!['D', 'J', 'F', 'V', 'W', 'S', 'L'],
        vec!['H', 'B', 'T', 'V', 'S', 'L', 'M', 'Z'],
        vec!['J', 'S', 'R'],
        vec!['W', 'L', 'M', 'F', 'G', 'B', 'Z', 'C'],
        vec!['B', 'G', 'R', 'Z', 'H', 'V', 'W', 'Q'],
        vec!['N', 'D', 'B', 'C', 'P', 'J', 'V'],
        vec!['Q', 'B', 'T', 'P'],
        vec!['C', 'R', 'Z', 'G', 'H'],
    ];
}
