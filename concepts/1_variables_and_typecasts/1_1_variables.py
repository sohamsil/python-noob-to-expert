############################################################################## 
# Variable is a container for a value of type (string,integer,float,boolean) #
##############################################################################

# Define string variables and print values
first_name : str = "Lumos"
last_name : str = "Code"
email : str = "lumoscode@gmail.com"

print(f"{first_name} {last_name} has email : {email}")

# Define integer variables and print values
day : int = 1
month : int = 1
year : int = 1990

print(f"{first_name} {last_name} has DOB: {day}/{month}/{year}")

# Define float variable and print values
height : float = 5.7
weight : float = 63.5

print(f"{first_name} {last_name} has height: {height} feet and weight: {weight} kg")

# Define boolean variable, check condition and print statement
is_student : bool = False

if is_student:
    print(f"{first_name} {last_name} is a student")
else:
    print(f"{first_name} {last_name} is not a student")

