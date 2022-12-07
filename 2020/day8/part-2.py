def execute(instructions):
    next_instruction = 0
    executed_instructions = []

    accumulator = 0

    while not next_instruction in executed_instructions and next_instruction < len(instructions):
        executed_instructions = [*executed_instructions, next_instruction]

        instruction, value = instructions[next_instruction]

        if instruction == 'nop':
            next_instruction = next_instruction + 1

            continue

        if instruction == 'acc':
            accumulator = accumulator + int(value)

            next_instruction = next_instruction + 1

            continue

        if instruction == 'jmp':
            next_instruction = next_instruction + int(value)

            continue

    return accumulator, next_instruction in executed_instructions


def run_with_substitution(instructions, base, substitute):
    for index, (instruction, value) in enumerate(instructions):
        if instruction == base:
            accumulator, loop_detected = execute(
                [*instructions[:index], [substitute, value], *instructions[index+1:]])

            if not loop_detected:
                return accumulator


def fix_nop_to_jmp(instructions):
    return run_with_substitution(instructions, base='nop', substitute='jmp')


def fix_jmp_to_nop(instructions):
    return run_with_substitution(instructions, base='jmp', substitute='nop')


if __name__ == "__main__":
    with open('./input.txt') as f:
        instructions = [instruction.strip().split(' ')
                        for instruction in f.readlines()]

        print(fix_jmp_to_nop(instructions) or fix_nop_to_jmp(instructions))
