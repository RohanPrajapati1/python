# List Methods
list = ["apple", "banana", "cherry"]
# list.append("orange") # Adds an element at the end of the list
list.append("orange")
print(list) # ['apple', 'banana', 'cherry', 'orange']

# list.insert(1, "orange") # Adds an element at the specified position
list.insert(1, "orange")
print(list) # ['apple', 'orange', 'banana', 'cherry', 'orange']

# list.remove("banana") # Removes the first item with the specified value
list.remove("banana")
print(list) # ['apple', 'orange', 'cherry', 'orange']

# list.pop() # Removes the last item in the list
list.pop()
print(list) # ['apple', 'orange', 'cherry']

# list.pop(1) # Removes the item at the specified position in the list
list.pop(1)
print(list) # ['apple', 'cherry']


# list.index("apple") # Returns the index of the first element with the specified value
index = list.index("apple")
print(index) # 0

# list.count("apple") # Returns the number of elements with the specified value
count = list.count("apple")
print(count) # 1

# list.sort() # Sorts the list
list.sort()
print(list) # ['apple', 'cherry']

# list.reverse() # Reverses the order of the list
list.reverse()
print(list) # ['cherry', 'apple']

# list.copy() # Returns a shallow copy of the list
copy = list.copy()
print(copy) # ['cherry', 'apple']

# list.extend(["orange", "mango"]) # Adds the elements of a list (or any iterable), to the end of the current list
list.extend(["orange", "mango"])
print(list) # ['cherry', 'apple', 'orange', 'mango']

# list.clear() # Removes all the elements from the list
list.clear()
print(list) # []

# list is mutable 
# list is sequence type means it supports indexing and slicing.