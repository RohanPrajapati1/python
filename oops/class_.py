# Defining a class
class Animal:
    class_variable = "I am a class variable, shared by all instances of the class"
    # instance variable is unique to each instance of the class, while class variable is shared among all instances of the class.

    # constructor
    def __init__(self , name , species):
        self.name = name
        self.species = species
    # in python declare attribute in constructor and use self to access it
    # Without self, Python would not know which object's properties you want to access:
    # It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class:


    # user defined method
    def make_sound(self, sound):
        print(f"{self.name} says {sound}")

    def make_sound_indirectly(self):
        # we can also call method within another method using self 
        self.make_sound("Hello, I am a " + self.species)
    

# creating an object 
dog = Animal("Buddy" , "Dog")
cat = Animal("Whiskers" , "Cat")

# calling class variable using class name and instance name
print(dog.class_variable)
print(Animal.class_variable)

Animal.class_variable = "can be change by class name not by instance"

print(dog.class_variable)
print(Animal.class_variable)


dog.make_sound("woof")
cat.make_sound("meow")


dog.make_sound_indirectly()
cat.make_sound_indirectly()