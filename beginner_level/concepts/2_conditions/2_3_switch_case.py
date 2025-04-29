#########################################################################
# Switch case statements offer a more structured way to handle          #
# scenarios where multiple comparisons are required to make a decision  #
#########################################################################

# Create a grade evaluation system
grade: str = ""

# Take marks scored as input from user
marks: int = int(input("Enter student's marks scored : "))

# Evaluate grade
if marks <= 100 and marks > 80:
    grade = "A"
elif marks <= 80 and marks > 60:
    grade = "B"
elif marks <= 60 and marks > 50:
    grade = "C"
elif marks <= 50 and marks >= 35:
    grade = "D"
elif marks < 35 and marks >= 0:
    grade = "F"
else:
    print("Invalid input!")


# Offer discount based on merit using switch case statements
match grade:
    case 'A':
        print(f"You have achieved Grade : {grade}.")
        print("You're eligble for 30% discount for the advanced certification.")
    case 'B':
        print(f"You have achieved Grade : {grade}.")
        print("You're eligble for 10% discount for the advanced certification.")
    case 'C':
        print(f"You have achieved Grade : {grade}.")
        print("You're eligble for 10% discount for the advanced certification.")
    case 'D':
        print(f"You have achieved Grade : {grade}.")
    case 'F':
        print(
            f"You have achieved Grade : {grade}.Please appear retry the exam")
    case _:
        print("Grade not available!")
