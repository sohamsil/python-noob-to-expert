###################################################################
# Calculate area of a circle based on the radius provided by user #
###################################################################

print("Welcome to Circle Radius Calculator!\n")

# Define radius variable and take input from user
radius: float = float(input("Entire Radius(cm): "))

# Output Area of circle using formula (3.14 * Radius**2)
area: float = 3.14*radius**2
print(f"Area of circle with radius:{radius} cm = {area} cm^2")
