#########################################################################################
# Scope refers to the region of a program where a variable is accessible.               #
# Variables can have different scopes: local scope (inside a function),                 #
# global scope (outside all functions), and nonlocal scope (used in nested functions).  #
# Scope determines the visibility and lifetime of a variable.                           #
#########################################################################################

####################################################################################################
# Local scope refers to variables defined inside a function, accessible only within that function. #
####################################################################################################

def func() -> None:
    var: str = "Hello World"
    print(var)

func()
# Remove comment for below code to check scope of the local variable
# print(var)

####################################################################################################################
# Enclosing scope refers to variables in the outer function of a nested function, accessible to the inner function #
####################################################################################################################


def outer_func() -> None:
    var: str = "Hello World"

    def inner_func() -> None:
        print(f"Printing from inner_func : {var}")

    inner_func()
    print(f"Printing from outer_func : {var}")

outer_func()
# Remove comment for below code to check scope of the inner function
# inner_func()


# Understanding the scope of a vraible having the same in outer and inner functions
def outer_func() -> None:
    var: str = "Hello World"

    def inner_func() -> None:
        var: str = "Hey World"
        print(f"Printing from inner_func: {var}")

    inner_func()
    print(f"Printing from outer_func : {var}")

outer_func()

# Changing the value of outer function's variable using 'nonlocal' keyword

def outer_func() -> None:
    var: str = "Hello World"

    def inner_func() -> None:
        nonlocal var
        var = "Hey World"

        print(f"Printing from inner_func: {var}")

    inner_func()
    print(f"Printing from outer_func : {var}")

outer_func()

#########################################################################################
# Global variable scope refers to variables defined outside all functions,
# accessible and modifiable throughout the program unless shadowed by a local variable. #
#########################################################################################

var: str = "Hello World"

def func() -> None:

    print(f"Printing from func : {var}")

    def change_var():

        global var
        var = "Hey World"
        print(f"Printing from change_var: {var}")

    change_var()

print(f"Printing global variable before executing func: {var}")
func()
print(f"Printing global variable after executing func: {var}")


##################################################################################################
# `dir(__builtins__)` lists all built-in functions, exceptions, and objects available in Python. #
# These include functions like `print`, `len`, and `type`, which are always accessible.          #
##################################################################################################
print(dir(__builtins__))