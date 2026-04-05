# Function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# In Python a function is defined using the def keyword:

def say_hello():
    print("Hello World")

# To call a function, use the function name followed by parenthesis:
say_hello()

# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def say_hello(name):
    print("Hello " + name)

say_hello("John")

# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
# This function expects 2 arguments, and gets 2 arguments:
def say_hello(fname, lname):
    print("Hello " + fname + " " + lname)

say_hello("John", "Doe")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def say_hello(*names):
    print("Hello " + names[0] + " " + names[1])

say_hello("John", "Doe")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def say_hello(**names):
    print("Hello " + names["fname"] + " " + names["lname"])

say_hello(fname="John", lname="Doe")

# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
def say_hello(name = "John"):
    print("Hello " + name)

say_hello("Doe")
say_hello()


def factorial(n):
    if n == 0:
        return 1
    else:
        n * factorial(n - 1)

print(factorial(5))


# lambda function
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax
# lambda arguments : expression
# The expression is executed and the result is returned:
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
    return lambda a : a * n
    # it return a function that multiplies a with n

mydoubler = myfunc(2)
# 2 is the value of n
# 11 is the value of a
print(mydoubler(11))

mytripler = myfunc(3)
print(mytripler(11))

