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

# Execution flow when calling myfunction()
#   myfunction() -> actually calls the changecase wrapper.
#   inside changecase.wrapper:
#       it calls func() -> butdec func is the result of greeting(myfunction).
#   so first, the greeting wrapper runs:
#      calls the original myfunction() -> return "vridhi"
#      adds "Hello" and "have a good day" -> "Hello vridhi have a good day"
#   that string goes back to changecase.wrapper.
#   .upper() is applied -> "HELLO VRIDHI HAVE A GOOD DAY".