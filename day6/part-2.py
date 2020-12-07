def get_answer_sheet():
    sheet = {}

    for index in range(ord('a'), ord('z') + 1):
        sheet[chr(index)] = 0

    return sheet


if __name__ == "__main__":
    with open('./input.txt') as f:
        groups = f.read().split('\n\n')

        given_answers = 0

        for group in groups:
            count = 0
            sheet = get_answer_sheet()

            answers = group.strip().split('\n')

            for answer in answers:
                for letter in answer:
                    sheet[letter] = sheet[letter] + 1

                    if sheet[letter] == len(answers):
                        count = count + 1

            given_answers = given_answers + count

        print(given_answers)
