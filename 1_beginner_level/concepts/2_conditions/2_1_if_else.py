####################################################################
# if-else statement evaluates whether a condition is true or false #
####################################################################

# Create a marks evaluation system
passed: bool = False

# Take marks scored as input from user
marks: int = int(input("Enter student's marks scored : "))

# Pass/fail evaluation
if marks >= 35:
    print(f"You have passed the exam with {marks} marks")
    passed = True
else:
    print(f"You have failed!")

# Condition check for course offering
if passed:
    print("Congratulations on passing your exam! Now try our advanced certification.")
else:
    print("We have got your back! You can retry the test for free.")
