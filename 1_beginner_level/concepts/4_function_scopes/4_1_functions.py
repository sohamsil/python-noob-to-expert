##########################################################################################
# A function in Python is a reusable block of code that performs a specific task.        #
# It is defined using the def keyword, can take input arguments, and may return a value. #
# Functions help organize code, improve readability, and enable reusability.             #
##########################################################################################

# Define a function and define a variable inside the function
def print_name() -> None:
    name: str = "Lumos"

    print("Function : print_name, Output:", end=" ")
    print(f"Hello! {name}")

# Define a function and pass arguments
def print_fullname(fname: str, lname: str) -> None:

    print("Function : print_fullname, Output:", end=" ")
    print(f"Hello! {fname} {lname}")

# Define a function, pass arguments and return value
def return_fullname(fname: str, lname: str) -> str:

    print("Function : return_fullname, Output:", end=" ")
    return f"{fname} {lname}"

# Every Python file (module) has a special built-in variable called __name__
# If the file is being run directly, then __name__ is set to "__main__"
# If the file is being imported into another script, __name__ is set to 
# the name of the module (i.e. the filename without .py).
if __name__ == "__main__":

    print_name()
    print_fullname("Lumos", "Code")

    fullname = return_fullname("Lumos", "Code")
    print(f"Hey! {fullname}")
