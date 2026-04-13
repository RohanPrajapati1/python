# Dictionary just like hashmap in java 
# dictionary is collection of key and value pairs
# dictionary are unordered , changeable and indexed(key are used as index)
dict = {"name" : "Vridhi" , "age" : 21, "city" : "Meerut"}

print(dict)

# Accessing item 
for key , value in dict.items():
    print( key , ": " , value)

# updating dictionary
# 1. updating item
dict["age"] = 22
print(dict)
dict.update({"surname" : "Rajeev"})
print(dict)

print(dict.keys())
print(dict.values())
print(dict.items())

# dictionary methods
# 1. clear() - removes all the items from the dictionary
# dict.clear()  
# 2. copy() - returns a copy of the dictionary
dict2 = dict.copy() 
print(dict2)
# 3. fromkeys() - returns / create a dictionary with the specified keys and values
dict3 = dict.fromkeys(["name" , "age"] , "unknown")
print(dict3) # {'name': 'unknown', 'age': 'unknown'}
# 4. get() - returns the value of the specified key
print(dict.get("name"))
# 5. pop() - removes the item with the specified key
dict.pop("age")
print(dict)
# 6. popitem() - removes the last inserted item
dict.popitem()
print(dict)
# 7. setdefault() - returns the value of the specified key, if the key does not exist, insert the key with the specified value
print(dict.setdefault("name" , "unknown"))
print(dict.setdefault("age" , 22))
print(dict)
# 8. update() - updates the dictionary with the specified key-value pairs
dict.update({"age" : 22})
print(dict)
# 9. values() - returns a list of all the values in the dictionary
print(dict.values())


# dictionary comprehension
squares = {x : x*x for x in range(1, 11)}


