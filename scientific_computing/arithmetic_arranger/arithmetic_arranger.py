def arithmetic_arranger(problems, solutions=False):
    # first error message
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for index, problem in enumerate(problems):
        value1, operator, value2 = problem.split()

        # other error messages
        if not operator in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not value1.isdigit() or not value2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(value1) > 4 or len(value2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # choose between addition and subtraction
        if operator == "+":
            solution = int(value1) + int(value2)
        else:
            solution = int(value1) - int(value2)

        line_length = len(max([value1, value2], key=len))

        line1 += value1.rjust(line_length + 2)
        line2 += operator + value2.rjust(line_length + 1)
        line3 += "-" * (line_length + 2)
        line4 += str(solution).rjust(line_length + 2)

        # distance between each problem
        if index < len(problems) - 1:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "

    # print problem
    arranged_problems = line1 + "\n" + line2 + "\n" + line3

    # print solution
    if solutions:
        arranged_problems += "\n" + line4

    return arranged_problems
