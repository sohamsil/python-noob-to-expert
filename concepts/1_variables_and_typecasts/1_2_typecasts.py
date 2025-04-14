#################################################################### 
# Typecasting is the process of converting one datatype to another #
####################################################################

# Define float variable and convert to integer
val1 : float = 10.5
val2 : int = int(val1)

print(f"val1 is of type:{type(val1)} & value:{val1} and val2 is of type:{type(val2)} & value:{val2}")

# Define int variable and convert to float
val3 : int = 12
val4 : int = float(val3)

print(f"val3 is of type:{type(val3)} & value:{val3} and val4 is of type:{type(val4)} & value:{val4}")

# Define string variable and convert to boolean
val5 : str = "Lumos"
val6 : bool = bool(val5)

print(f"val5 is of type:{type(val5)} & value:{val5} and val6 is of type:{type(val6)} & value:{val6}")
