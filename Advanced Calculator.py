import re

# Square root calculation function
def my_sqrt(x, tolerance=1e-30):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    if x == 0:
        return 0
    guess = x
    while abs(guess * guess - x) > tolerance:
        guess = (guess + x / guess) / 2
    return guess

# Power calculation function
def my_pow(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / my_pow(x, -y)
    result = 1
    for _ in range(int(y)):
        result *= x
    return result

def get_operand_index(op_index, operators):
    return op_index - operators[:op_index].count('(') - operators[:op_index].count(')')

# This part will check the errors in input
def is_valid_expression(expr):
    if expr.count('(') != expr.count(')'):
        print("Invalid input: mismatched parentheses.")
        return False
    if any(op in expr for op in ['++', '--', '**', '//']):
        print("Invalid input: repeated operators (e.g., ++, --, **, //).")
        return False
    return True


def calculate_expression(expression):
    expression = expression.replace(" ", "")
    if not is_valid_expression(expression):
        return

    # This loop will separate operands and operators in different lists
    operands = []
    operators = []
    i = 0
    while i < len(expression):
        negative_match = re.match(r"\(-\d+(?:\.\d+)?\)", expression[i:])
        if negative_match:
            operands.append(float(negative_match.group()[1:-1]))
            i += len(negative_match.group())
            continue
        number_match = re.match(r"\d+(?:\.\d+)?", expression[i:])
        if number_match:
            operands.append(float(number_match.group()))
            i += len(number_match.group())
            continue
        operator_match = re.match(r"([+\-*/()%^])", expression[i:])
        if operator_match:
            operators.append(operator_match.group())
            i += len(operator_match.group()) 
            continue
    print(operands)
    print(operators)

    # This loop will calculate ()
    while '(' in operators and ')' in operators:
        i = 0
        while i < len(operators):
            if operators[i] == ')' and operators[i - 2] == '%':
                operand_index = get_operand_index(i - 1,operators) - 1
                result = my_sqrt(operands[operand_index])
                del operands[operand_index:operand_index + 1]
                operands.insert(operand_index, result)
                del operators[i - 2:i - 1]
                print(operands)
                print(operators)
            if operators[i] == ')' and operators[i - 2] == '(':
                operand_index = get_operand_index(i - 1, operators)
                match operators[i - 1]:
                    case '^':
                        result = my_pow(operands[operand_index], operands[operand_index + 1])
                    case '*':
                        result = operands[operand_index] * operands[operand_index + 1]
                    case '/':
                        result = operands[operand_index] / operands[operand_index + 1]
                    case '+':
                        result = operands[operand_index] + operands[operand_index + 1]
                    case '-':
                        result = operands[operand_index] - operands[operand_index + 1]
                del operands[operand_index:operand_index + 2]
                operands.insert(operand_index, result)
                del operators[i - 2:i + 1]
                print(operands)
                print(operators)
            else:
                i += 1

    # This loop will calculate * and / in order from left to right
    i = 0
    while i < len(operators):
        if operators[i] == '*':
            result = operands[i] * operands[i + 1]
            del operands[i:i + 2]
            operands.insert(i, result)
            del operators[i]
        elif operators[i] == '/':
            result = operands[i] / operands[i + 1]
            del operands[i:i + 2]
            operands.insert(i, result)
            del operators[i]
        else:
            i += 1

    # This loop will calculate + and - in order from left to right
    i = 0
    while i < len(operators):
        if operators[i] == '+':
            result = operands[i] + operands[i + 1]
            del operands[i:i + 2]
            operands.insert(i, result)
            del operators[i]
        elif operators[i] == '-':
            result = operands[i] - operands[i + 1]
            del operands[i:i + 2]
            operands.insert(i, result)
            del operators[i]
        else:
            i += 1

    print(f"The result is {operands[0]}")  

print("This is a simple calculator. Please insert your numbers and operator: ")
expr = input() 
calculate_expression(expr)