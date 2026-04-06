class Person:
    def __init__(self , name , age):
        self.age = age
        self.name = name
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    # this method defines how the object should be represented when object is printed
    
    def greet():
        print("Hello!")

p1 = Person("Vridhi" , 21)
print(p1)
p2 = Person("Rohan" , 21)
p1.greet()
p2.greet()

del p1.greet
# p1.greet() # this will raise an error because the greet method has been deleted from the p1 instance but it is still available for p2 instance

p2.greet()

# Deleting method 
del Person.greet # this will delete the greet method from the person class and all instances of the class will no longer have access to the greet method

# now after deleting greet from person class , p2 is also no longer able to access the greet method