# Parent class / base class
class Person:
    def __init__ (self, firstname , lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        print(self.firstname , " " , self.lastname)


# child class / derived class
class Student (Person):
    pass
    # pass -> use if you dont want to add any other properties 

s1 = Student("Vridhi" , "Rajeev")
s1.print_name()