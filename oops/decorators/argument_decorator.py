def changecase(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

@changecase
def myfunction(name):
    return "Hello " + name
print(myfunction("Vridhi")) 


# - Call print(myfunction("Vridhi"))
# - myfunction("Vridhi") → calls wrapper("Vridhi").
# - Inside wrapper:
# - func(name) → calls the original myfunction("Vridhi") → returns "Hello Vridhi".
# - Then .upper() is accessed.
# -  "HELLO VRIDHI",
