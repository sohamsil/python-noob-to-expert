##################################################################### 
# Python offers three logical operators: and, or, and not.          #
# These operators are used to form compound Boolean expressions and # 
# evaluate multiple conditions within a single expression.          #
#####################################################################

# Create a grade evaluation system
grade : str = ""

# Take marks scored as input from user
marks : int = int(input("Enter student's marks scored : "))

# Evaluate grade
if marks<=100 and marks>80:
    grade = "A"
elif marks<=80 and marks>60:
    grade = "B"
elif marks<=60 and marks>50:
    grade = "C"
elif marks<=50 and marks>=35:
    grade = "D"
elif marks < 35 and marks>=0:
    grade = "F"
else:
    print("Invalid input!")


# Offer discount based on merit
if grade == "A":
    print(f"You have achieved Grade : {grade}.")
    print("You're eligble for 30% discount for the advanced certification.") 
elif grade == "B" or grade == "C":
    print(f"You have achieved Grade : {grade}.")
    print("You're eligble for 10% discount for the advanced certification.")
elif grade == "D":
    print(f"You have achieved Grade : {grade}.")
elif grade == "F":
    print(f"You have achieved Grade : {grade}.Please appear retry the exam")
elif not grade:
    print("Grade not available!")
else:
    pass