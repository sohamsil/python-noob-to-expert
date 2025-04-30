#########################################################################################
# A tuple is an ordered, immutable collection of elements, defined using parentheses () #
# or the tuple() constructor. Tuples are useful for storing fixed collections of items  #
# and support indexing, slicing, and iteration.                                         #
#########################################################################################

# Create a tuple
t1: tuple = (1,2,3,4,5)
print(f"t1 type: {type(t1)}")
print(f"t1: {t1}")
print(f"Value of first key in t1: {t1[0]}")

# Create a tuple using tuple() constructor
t2:tuple = tuple([1,2,3])
print(f"t2: {t2}")

# Check if a value in tuple can be changed
t2[0] = 10