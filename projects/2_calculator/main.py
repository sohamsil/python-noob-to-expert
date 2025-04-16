####################################################################################### 
# Basic calculator perform arithmetic operations(Add,Subtract,Multiply,Divide,Modulo) #
#######################################################################################

# Get input from users for number 1,number 2 and arithmatic operator
num1 : int = int(input("Enter first number : "))
num2 : int = int(input("Enter second number : "))
operator : str = input("Enter operator(+,-,*,/,%) : ")

result = None


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

if result:
    print(f"Result : {result}")