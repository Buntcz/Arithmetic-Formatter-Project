def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"
    for problem in problems:
        split_problems = problem.split(" ")
        element1 = split_problems[0]
        operand = split_problems[1]
        element2 = split_problems[2]
        if operand != "+" and operand != "-":
            return "Error: Operator must be '+' or '-'."
        if not element1.isdigit() or not element2.isdigit():
            return "Error: Numbers must contain only digits."
        if len(element1) > 4 or len(element2) > 4:
            return "Error: Numbers cannot be more than 4 digits."
        result = None
        if operand == "+":
            result = int(element1) + int(element2)
        if operand == "-":
            result = int(element1) - int(element2)
        dashes = None
        if len(element1) > len(element2):
            length = len(element1) + 2
            dashes = ("_" * length)
        else:
            length = len(element2) + 2
            dashes = ("_" * length)
        print(dashes)
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')