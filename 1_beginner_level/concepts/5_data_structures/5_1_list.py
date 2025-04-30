############################################################################################
# A list is a mutable, ordered collection of items that can hold elements of different     #
# data types. Lists are defined using square brackets [] and allow operations like adding, #
# removing, or modifying elements, as well as slicing and iteration.                       #
############################################################################################

# Create empty list
l1:list = []
print(f"l1 type:{type(l1)}")
print(f"List l1:{l1}")

# Create list with mutliple data type
l2:list = [1,"2",3.0,True]
print(f"List l2:{l2}")

# Create a lust using list constructor
l3:list = list([1,2,3])
print(f"List l3:{l3}")

# Let's use l2 and read elements from the list
print(f"First element of l2:{l2[0]}")
print(f"Last element of l2:{l2[-1]}")

# Read a range of elements
print(f"First to third elements of l2:{l2[0:2]}")
print(f"Second to last elements of l2:{l2[1:]}")

# add one element to a list
l2.append(4)
print(f"L2 after adding 4: {l2}")

# Remove one element to a list
l2.remove(1)
print(f"L2 after removing 1: {l2}")

# Change value of an element in list
l2[0]="Changed Value"
print(f"L2 after changing value at index 0:{l2}")

# Reverse a list
print(f"Reversed l2: {l2[::-1]}")

