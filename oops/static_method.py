class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Car: {self.make} {self.model}")

class StaticMethodExample:
    @staticmethod
    def static_method():
        print("This is a static method.")  
    # there is not need of self in static method because it does not access any instance variables or methods. It can be called directly on the class without creating an instance.
# Example usage
car1 = Car("Toyota", "Camry")
car1.display_info()
StaticMethodExample.static_method()