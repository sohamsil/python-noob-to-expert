###############################################################################
# for loops are used to iterate a known number of times, which is common when #
# you’re processing data collections with a specific number of data items     #
###############################################################################

# for loop using a finite list of integers
numbers: list = [1, 2, 3, 4, 5]
print("Printing numbers: ",end=' ')
for number in numbers:
    print(number,end=' ')

# for loop using a finite list of strings
names: list = ["Alice", "Bob", "Charlie"]
print("\nPrinting name: ",end=' ')
for name in names:
    print(name,end=' ')

# for loop using a finite list of mixed data types
mixed_data:list = [1, "Alice", 3.14, True]
print("\nPrinting data: ",end=' ')
for item in mixed_data:
    print(item,end=' ')


# for loop using default range
print("\nPrinting items from default range: ",end=' ')
for item in range(10):
    print(item,end=' ')

# for loop using range with start
print("\nPrinting items from range with start: ",end=' ')
for item in range(1,10):
    print(item,end=' ')

# for loop using range with start & step
print("\nPrinting items from range with start & step: ",end=' ')
for item in range(1,10,2):
    print(item,end=' ')