use std::{fs::read_to_string, str::Lines};

const OPPONENT_ROCK: &str = "A";
const OPPONENT_PAPER: &str = "B";
const OPPONENT_SCISSOR: &str = "C";

const WE_ROCK: &str = "X";
const WE_PAPER: &str = "Y";
const WE_SCISSORS: &str = "Z";

const MUST_LOOSE: &str = "X";
const MUST_DRAW: &str = "Y";
const MUST_WIN: &str = "Z";

const SCORE_ROCK: i32 = 1;
const SCORE_PAPER: i32 = 2;
const SCORE_SCISSORS: i32 = 3;

const LOST: i32 = 0;
const DRAW: i32 = 3;
const WON: i32 = 6;

fn main() {
    let contents = read_to_string("input.txt").expect("Could not read input");

    part_one(contents.lines());
    part_two(contents.lines());
}

fn part_one(rounds: Lines) {
    let mut points = 0;

    for round in rounds {
        let mut played = round.split_whitespace();

        let opponent = played.next().unwrap();
        let us = played.next().unwrap();

        points += points_played(us) + points_result(opponent, us);
    }

    println!("Score 1: {points}")
}

fn part_two(rounds: Lines) {
    let mut points = 0;

    for round in rounds {
        let mut played = round.split_whitespace();

        let opponent = played.next().unwrap();
        let outcome = played.next().unwrap();

        let us = choose_move(opponent, outcome);

        points += points_played(&us) + points_result(opponent, &us)
    }

    println!("Score 2: {points}")
}

fn points_played(us: &str) -> i32 {
    match us {
        WE_ROCK => SCORE_ROCK,
        WE_PAPER => SCORE_PAPER,
        WE_SCISSORS => SCORE_SCISSORS,

        _ => 0,
    }
}

fn points_result(opponent: &str, us: &str) -> i32 {
    if we_won(opponent, us) {
        return WON;
    }

    if we_lost(opponent, us) {
        return LOST;
    }

    return DRAW;
}

fn we_won(opponent: &str, us: &str) -> bool {
    match opponent {
        OPPONENT_ROCK => us == WE_PAPER,
        OPPONENT_PAPER => us == WE_SCISSORS,
        OPPONENT_SCISSOR => us == WE_ROCK,

        _ => false,
    }
}

fn we_lost(opponent: &str, us: &str) -> bool {
    match opponent {
        OPPONENT_ROCK => us == WE_SCISSORS,
        OPPONENT_PAPER => us == WE_ROCK,
        OPPONENT_SCISSOR => us == WE_PAPER,

        _ => true,
    }
}

fn choose_move<'a>(opponent: &'a str, outcome: &'a str) -> String {
    match opponent {
        OPPONENT_ROCK => match outcome {
            MUST_WIN => String::from(WE_PAPER),
            MUST_LOOSE => String::from(WE_SCISSORS),
            MUST_DRAW => String::from(WE_ROCK),

            _ => todo!(),
        },
        OPPONENT_PAPER => match outcome {
            MUST_WIN => String::from(WE_SCISSORS),
            MUST_LOOSE => String::from(WE_ROCK),
            MUST_DRAW => String::from(WE_PAPER),

            _ => todo!(),
        },
        OPPONENT_SCISSOR => match outcome {
            MUST_WIN => String::from(WE_ROCK),
            MUST_LOOSE => String::from(WE_PAPER),
            MUST_DRAW => String::from(WE_SCISSORS),

            _ => todo!(),
        },

        _ => todo!(),
    }
}
