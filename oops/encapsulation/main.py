class Car:
    def __init__(self , brand , model):
        self.__brand = brand # private attribute
        self.__model = model # private attribute

    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model

    
class ElectricCar (Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model) # to call the parent class constructor
        self.__battery_size = battery_size

    def get_battery_size(self):
        return self.__battery_size


e1 = ElectricCar("Tesla" , "Model S" , 100)
e1.__brand = "BMW" # this will not change the brand because it is a private attribute
print(e1.get_brand()) # this will print "Tesla" because the private attribute is not
