# In this we are learning about string in python
# String is a sequence of characters
# String is immutable
# String can be enclosed in single quotes or double quotes
# String can be enclosed in triple single quotes or triple double quotes
# String can be concatenated using + operator
# String can be repeated using * operator
# String can be accessed using index
# String can be sliced using slice operator
# String can be formatted using format() method
# String can be formatted using f-string
# String can be formatted using string interpolation
# String can be formatted using template string
# String can be formatted using string concatenation
# String can be formatted using string interpolation


str = "Hello, World!"
print(str) # Hello, World!
print(type(str)) # <class 'str'>
print(len(str)) # 13
print(str[0]) # H


# slicing
print(str[0:5]) # Hello
print(str[:5]) # Hello

# negative index
print(str[-1]) # !

# repeat
print(str * 2) # Hello, World!Hello, World!
print(2 * str) # Hello, World!Hello, World!
print(str + " " + "Python") # Hello, World! Python

# format
name = "Python"
version = 3.8
print("Programming language is {} and version is {}".format(name, version)) # Programming language is Python and version is 3.8

# modifiying
print(str.upper()) # HELLO, WORLD!
print(str.lower()) # hello, world!
print(str.capitalize()) # Hello, world!
print(str.title()) # Hello, World!
print(str.swapcase()) # hELLO, wORLD!
print(str.replace("World", "Python")) # Hello, Python!
print(str.strip()) # Hello, World!
# strip means remove leading/starting and trailing/ending spaces

print(str.lstrip()) # Hello, World!
print(str.rstrip()) # Hello, World!
print(str.startswith("Hello")) # True
print(str.endswith("World!")) # True
print(str.find("World")) # 7
print(str.index("World")) # 7
print(str.count("l")) # 3
print(str.isalnum()) # False
print(str.isalpha()) # False
print(str.isdigit()) # False
print(str.islower()) # False
print(str.isupper()) # False
print(str.isspace()) # False
print(str.istitle()) # False
print(str.isprintable()) # True
print(str.isascii()) # True
print(str.isidentifier()) # False
print(str.isdecimal()) # False
print(str.isnumeric()) # False
print(str.isidentifier()) # False

# string methods
print(str.split()) # ['Hello,', 'World!']
print(str.split(",")) # ['Hello', ' World!']
# split means convert string to list 