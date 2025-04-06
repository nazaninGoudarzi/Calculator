import re

print("This is a simple calculator. Please insert your numbers and operator: ")
expression = input()
match_result = re.match(r"(\d+)([+\-*/])(\d+)", expression)

if match_result:
    first_op = int(match_result.group(1))
    operator = match_result.group(2)
    second_op = int(match_result.group(3))

    match operator:
        case '+':
            result = first_op + second_op
            print(f"The result is {result}")
        case '-':
           result = first_op - second_op
           print(f"The result is {result}")
        case '*':
            result = first_op * second_op
            print(f"The result is {result}")
        case '/':
            if second_op != 0:
                result = first_op / second_op
                print(f"The result is {result}")
            else:
                print("Division by zero is not defined in math!")

else:
    print("invalid input!! :(")
