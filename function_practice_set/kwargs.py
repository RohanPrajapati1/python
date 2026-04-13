#  **kwargs are used to pass number of variable with keyword

def Person(**kwargs):
    print(kwargs) # kwargs is a dictionary
    for key , value in kwargs.items():
        print(key + " : " + str(value))

Person(name = "Vridhi", age = 20, city = "Meerut")