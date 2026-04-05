name = "rohan"
age = 20
print(type(name))
print(type(age))


# Assiging multiple values to multiple variables

x , y , z = 10 , 20 , 30

def myfunc():
    global x
    # in this we use global keyword to change the value of x
    print(x)
    x = 300

myfunc()   
print(x)

def myfunc2():
    x = 100
    #  here x is local variable
    # so it will not change the value of x
    print(x)

myfunc2()    
print(x)
# Here we can see that the value of x is changed in myfunc() but not in myfunc2()


# Here we list all data types in python
# Python has the following data types built-in by default, in these categories:

# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry" , 34 , 5.55]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	dict / dictionary	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# x = None	NoneType	


# Setting the data type
x = str("Hello World")
y = int(20)
z = float(20.5)
a = complex(1j)
b = list(("apple", "banana", "cherry" , 34 , 5.55 , False))
c = tuple(("apple", "banana", "cherry" , 34 , 5.55 , False))
# tuple is also a list but it is immutable
# we can not change the value of tuple
d = range(6)
e = dict(name = "John", age = 36)
f = set(("apple", "banana", "cherry"))
g = frozenset(("apple", "banana", "cherry"))
h = bool(True)
i = bytes(b"Hello")
j = bytearray(5)
k = memoryview(bytes(5))
l = None



# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)
