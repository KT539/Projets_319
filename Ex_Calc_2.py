# NAME: Ex_Calc_2.py
# AUTHOR: Kilian Testard
# DATE: 11.11.2024

# main function:
def main():
    nb1, nb2, operator = user_input()
    if operator == "+":
        result = add(nb1, nb2)
    elif operator == "-":
        result = sub(nb1, nb2)
    elif operator == "*":
        result = mul(nb1, nb2)
    elif operator == "/":
        result = div(nb1, nb2)
    else:
        print("Invalid operator.")
        return

    print("Your result is: ", result)


# add function:
def add(nb1, nb2):
    return nb1 + nb2


# sub function:
def sub(nb1, nb2):
    return nb1 - nb2


# mul function:
def mul(nb1, nb2):
    return nb1 * nb2


# div function:
def div(nb1, nb2):
    if nb2 == 0:
        print("Error: division by 0 is undefined.")
        return
    return nb1 / nb2


# user_input function:
def user_input():
    nb1 = float(input("Please enter the first operand: "))
    nb2 = float(input("Please enter the second operand: "))
    operator = input("Please enter an operator (+, -, *, /): ")
    return nb1, nb2, operator


# execute
main()