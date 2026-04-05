# Tuple Methods with Examples
# Tuple Methods
tuple = ("apple", "banana", "cherry")
# tuple.count("apple") # Returns the number of times a specified value occurs in a tuple
count = tuple.count("apple")
print(count) # 1

# tuple.index("banana") # Searches the tuple for a specified value and returns the position of where it was found
index = tuple.index("banana")
print(index) # 1

# tuple.index("banana", 1) # Searches the tuple for a specified value and returns the position of where it was found
index = tuple.index("banana", 2)
print(index) # 1

# tuple.index("banana", 1, 2) # Searches the tuple for a specified value and returns the position of where it was found
index = tuple.index("banana", 1, 2)
print(index) # 1



# tuple is immutable, so it does not have methods like append(), remove(), or sort() that modify the tuple.
# tuple is sequence type means it supports indexing and slicing.