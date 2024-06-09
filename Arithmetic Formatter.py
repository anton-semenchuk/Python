def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    char_top = []
    char_bottom = []
    char_line = []
    char_answers = []

    for problem in problems:
        parts = problem.split()
        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]

        # обработка ошибок
        try:
            answer = str(eval(problem))
        except:
            return 'Error: Numbers must only contain digits.'
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # решение
        max_length = max(len(operand1), len(operand2)) + 2
        char_top.append(operand1.rjust(max_length))
        char_bottom.append(operator + ' ' + operand2.rjust(max_length - 2))
        char_line.append('-' * max_length)
        char_answers.append(answer.rjust(max_length))

    arranged_problems = ""
    if char_top:
        arranged_problems += "    ".join(char_top) + '\n'
    if char_bottom:
        arranged_problems += "    ".join(char_bottom) + '\n'
    if char_line:
        arranged_problems += "    ".join(char_line)
    if show_answers:
        if char_answers:
            arranged_problems += '\n' + "    ".join(char_answers)
    return arranged_problems
    
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')
print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')