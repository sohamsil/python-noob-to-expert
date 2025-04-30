######################################################################################
# A set is an unordered, mutable collection of unique elements, defined using        #
# curly braces {} or the set() constructor. Sets are useful for operations like      #
# union, intersection, and difference, and automatically eliminate duplicate values. #
######################################################################################

# Create a Set
s1:set = {1,2,3}
print(f"s1 type: {type(s1)}")
print(f"s1: {s1}")

# Create a set using the set() constructor
s2:set = set([1,2,3])
print(f"s2: {s2}")

# Create a set with duplicate values
s3:set = set([1,2,2,3,3,4])
print(f"Deduplicated s3: {s3}")

# Create two sets to perform union, intersection and finding difference between two sets
set1:set = set(['a','b','c','d'])
set2:set = set(['c','d','e','f'])

print(f"Union of set1 and set2: {set1.union(set2)}")
print(f"Intersection of set1 and set2: {set1.intersection(set2)}")
print(f"Difference of set1 and set2: {set1.difference(set2)}")

