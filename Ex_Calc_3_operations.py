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