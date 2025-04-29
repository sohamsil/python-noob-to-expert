###############################################################################
# while loops are commonly used to iterate an unknown number of times,        #
# which is useful when the number of iterations depends on a given condition. #
###############################################################################

# while loop for counting iterations
count:int = 0
while count < 10:
    count += 1
print(f"Count: {count}")


# while loop for counting iterations and break if count is more than 10
count:int = 0
while True:
    count += 1
    if count>10:
        break
print(f"Count: {count}")

# while loop to print even integers
count:int = 0
print(f"Even integers:", end=" ")
while count < 20:
    count += 1
    if count%2 != 0:
        continue
    print(count,end=" ")

# while loop to find a number or else print number not found
count:int = 0
item: int = 30
while count < 20:
    count += 1
    if item == count:
        print("Item found!")
        break
else:
    print("Item not found!")

