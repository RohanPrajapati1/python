# You can use multiple decorators on one function.

# This is done by placing the decorator calls on top of each other.

# Decorators are called in the reverse order, starting with the one closest to the function.


def changecase(func):
    def wrapper():
        return func().upper()
    return wrapper

def greeting(func):
    def wrapper():
        return "Hello " + func() + " Have a good day!"
    return wrapper

@changecase
@greeting
def myfunction():
    return "vridhi"

print(myfunction())

