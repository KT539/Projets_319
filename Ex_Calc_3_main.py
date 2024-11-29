#import functions from operations:
from Ex_Calc_3_operations import add, sub, mul, div, user_input


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


#execute
main()