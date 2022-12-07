if __name__ == "__main__":
    with open('./input.txt') as f:
        instructions = [instruction.strip().split(' ')
                        for instruction in f.readlines()]

        next_instruction = 0
        executed_instructions = []

        accumulator = 0

        while not next_instruction in executed_instructions:
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

        print(accumulator)
