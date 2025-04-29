#######################################################################################
# Basic calculator perform arithmetic operations(Add,Subtract,Multiply,Divide,Modulo) #
#######################################################################################


def basic_calculator(num1: any, num2: any, operator: str) -> any:

    # Perform calculation using Switch Case
    print(f"Calculating : {num1}{operator}{num2}")

    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            result = num1 / num2
        case '%':
            result = num1 % num2
        case _:
            print("Incorrect operator!")
            result = None

    return result


if __name__ == "__main__":

    print("Welcome to Basic Calculator!")

    # Get input from users for number 1,number 2 and arithmatic operator
    num1: int = int(input("Enter first number : "))
    num2: int = int(input("Enter second number : "))
    operator: str = input("Enter operator(+,-,*,/,%) : ")

    result = basic_calculator(num1, num2, operator)

    if result:
        print(f"Result : {result}")
