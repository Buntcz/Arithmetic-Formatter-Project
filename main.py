def arithmetic_arranger(problems, show_answers=False):
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        split_problems = problem.split(" ")
        element1 = split_problems[0]
        operand = split_problems[1]
        element2 = split_problems[2]
        if operand != "+" and operand != "-":
            return "Error: Operator must be '+' or '-'."
        if not element1.isdigit() or not element2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(element1) > 4 or len(element2) > 4:
            return "Error: Numbers cannot be more than four digits."
        result = None
        space = " "
        if operand == "+":
            result = int(element1) + int(element2)
        if operand == "-":
            result = int(element1) - int(element2)
        dashes = None
        spaces = None
        stringResult = str(result)
        if len(element1) > len(element2):
            length = len(element1) + 2
            dashes = ("-" * length)
            spaces = (" " * (len(dashes) - len(element1)))
            secondSpaces = (" " * (len(dashes) - len(element2) - 1))
            lengthResult = len(stringResult)
            resultSpaces = " " * (length - lengthResult)
            line1.append(spaces + (element1) + space*4)
            line2.append(operand + secondSpaces + element2 + space * 4)
            line3.append(dashes + space * 4)
            line4.append(resultSpaces + stringResult + space * 4)
        else:
            length = len(element2) + 2
            dashes = ("-" * length)
            spaces = (" " * (length - len(element1)))
            lengthResult = len(stringResult)
            resultSpaces = " " * (length - lengthResult)
            line1.append( spaces + (element1) + space * 4)
            line2.append(operand + space + element2 + space * 4)
            line3.append(dashes + space * 4)
            line4.append(resultSpaces + stringResult + space * 4)
    
    line1J = "".join(line1)
    line1J = line1J.rstrip()
    line2J = "".join(line2)
    line2J = line2J.rstrip()
    line3J = "".join(line3)
    line3J = line3J.rstrip()
    line4J = "".join(line4)
    line4J = line4J.rstrip()
    if show_answers == True:
        return line1J + "\n" + line2J + "\n" + line3J + "\n" + line4J
    else:
        return line1J + "\n" + line2J + "\n" + line3J


        
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')