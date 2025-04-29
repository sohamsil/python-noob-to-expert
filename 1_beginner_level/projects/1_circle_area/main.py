###################################################################
# Calculate area of a circle based on the radius provided by user #
###################################################################

def calc_area(radius: any) -> float:
    area = 3.14*radius**2
    return area


if __name__ == "__main__":

    print("Welcome to Circle Radius Calculator!")

    # Define radius variable and take input from user
    radius: float = float(input("Entire Radius(cm): "))
    # Call function calc_area by passing 'radius' as arg and stored returned value in 'area'
    area = calc_area(radius)

    print(f"Area of circle with radius:{radius} cm = {area} cm^2")
