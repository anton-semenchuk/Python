def error_handler(problem):
    len_of_operand = 0

    for char in problem:
        if char == '*' or char == '/':
            print("Error: Operator must be '+' or '-'.")

        if char == '+' or char == '-' or char == ' ' or str.isdigit(char):
            pass
        else:
            print('Error: Numbers must only contain digits.')
            
        if str.isdigit(char):
            len_of_operand += 1
            if len_of_operand > 4:
                print('Error: Numbers cannot be more than four digits.')
        else:
            len_of_operand = 0

def seporator(length):
    result = '--'
    for _ in range(length):
        result += '-'
    return result

def problem_arranger(problem, show_answers):
    operand1 = 0
    operand2 = 0
    answer = 0
    sign = ''
    longest_operand = 0
    len_operand1 = 0
    len_operand2 = 0

    for char in problem:
        if char == '-' or char == '+':
            sign = char

    operands = problem.split(' ' + sign + ' ')
    operand1 = int(operands[0])
    operand2 = int(operands[1])

    answer = operand1 + operand2 if sign == '+' else operand1 - operand2

    # вычисление длиннейщего операнда
    len_operand1 = len(str(operand1))
    len_operand2 = len(str(operand2))
    longest_operand = len_operand1 if len_operand1 > len_operand2 else len_operand2

    # return
    if show_answers:
        return f'{operand1:>{longest_operand + 2}}\n{sign} {operand2:>{longest_operand}}\n{seporator(longest_operand)}\n{answer:>{longest_operand + 2}}'
    else:
        return f'{operand1:>{longest_operand + 2}}\n{sign} {operand2:>{longest_operand}}\n{seporator(longest_operand)}'

def arithmetic_arranger(problems, show_answers=False):
    result = []

    if len(problems) > 5:
        print('Error: Too many problems.')

    for problem in problems:

        # обработка ошибок
        error_handler(problem)

        # решение
        result.append(problem_arranger(problem, show_answers))

    # output
    for i, problem in enumerate(result):
        result[i] += '    '
    result[len(result) - 1] = result[len(result) - 1].strip()

    return result

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')