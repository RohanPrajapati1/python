# Decorator is a function that take function as input and returns a new function that is a modified version of the original function.

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfuncion(): # myfuncion = changecase(myfuncion) / myfuncion = myinner(myfuncion)


    return "Hello vridhi"

print(myfuncion())


# - Call print(myfuncion())
# - myfuncion() → really calls myinner().
# - myinner() → calls the original myfuncion() (inside it) → gets "Hello vridhi".
# - Then .upper() is applied → "HELLO VRIDHI".
# - Finally, print() displays:
