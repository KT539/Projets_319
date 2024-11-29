def main():
    operand1, operator, operand2 = ask_user_input()
    result = calculate(operand1, operator, operand2)
    display_result(operand1, operator, operand2, result)


def ask_user_input():

    operand1 = float(input("Enter the first operand: "))
    operator = input("Enter an operator (+, -, *, /): ")
    operand2 = float(input("Enter the second operand: "))
    return operand1, operator, operand2


def calculate(operand1, operator, operand2):
    match operator:
        case '+':
            result = operand1 + operand2
        case '-':
            result = operand1 - operand2
        case '*':
            result = operand1 * operand2
        case '/':
            if operand2 == 0:
                print("Error: Division by zero is undefined.")
                return
            result = operand1 / operand2
        case _:
            print("Invalid operator.")
            return
    return result


def display_result(operand1, operator, operand2, result):
    print("The result of", operand1, operator, operand2, "is : ", result)
    return operand1, operator, operand2, result


main()