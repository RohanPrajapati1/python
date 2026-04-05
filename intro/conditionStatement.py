a = 33 
b = 200

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
# Output: b is greater than a
# In this code, a and b are two variables. We are using the if statement to check whether a is greater than b. It is not, so the else block will be executed

# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
# Example
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
# Output: a and b are equal
# In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print that a and b are equal.

# The else keyword catches anything which isn't caught by the preceding conditions.
# Example
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Output: a is greater than b
# In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print that a is greater.

# You can also have an else without the elif:
# Example
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
# Output: b is not greater than a
# In this example b is not greater than a, so the first condition is not true, so the else block will be executed

# One line if statement
# Example
a = 200
b = 33
if a > b: print("a is greater than b")
# Output: a is greater than b
# This technique is known as Ternary Operators, or Conditional Expressions.

# You can also have multiple else statements on the same line:
# Example
a = 2
b = 330
print("A") if a > b else print("B")
# Output: B
# This technique is known as Ternary Operators, or Conditional Expressions.

# You can also have multiple else statements on the same line:
# Example
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# Output: =
# This technique is known as Ternary Operators, or Conditional Expressions.

# nested if
# Example
x = 41
y = 42
z = 43
if y > x:
    if y > z:
        print("y is greater than x and z")
    else:
        print("y is greater than x not z")
# Output: y is greater than x not z
# In this example we have a nested if: the outer if contains the inner if. The outer if contains the condition y > x, which is true, so we go to the inner if and check if y is greater than z. This condition is not true, so we print that y is greater than x not z.


# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
# Example
a = 33
b = 200
if b > a:
    pass
# having an empty if statement like this, would raise an error without the pass statement

    