#################################################################################################
# A dictionary is a mutable, unordered collection of key-value pairs, where each key is unique. #
# Dictionaries are defined using curly braces {} and allow fast access, addition, and           #
# modification of values using their keys.                                                      #
#################################################################################################

# Create a diictionary
d1: dict = {0: 'First Value', 1: 'Second Value'}
print(f"d1 type: {type(d1)}")
print(f"d1: {d1}")
print(f"Value of first key in d1: {d1[0]}")

# Create dictionary using dict() constructor
d2: dict = dict([[0, 'First'], [1, 'Second']])
print(f"d2: {d2}")

# Create a nested dictionary
d3: dict = {'name': "Lumos", 'details': {
    'dob': "1/1/1990", 'email': "lumos.code@gmail.com"}}

print(f"d3['name']:{d3['name']}")
print(f"d3['details']:{d3['details']}")
print(f"d3['details']['email']:{d3['details']['email']}")

# Update value of a key
d3['details']['email'] = "abc@xyz.com"
print(f"d3['details']['email']:{d3['details']['email']}")