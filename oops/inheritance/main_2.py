class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    
class ElectricCar (Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model) # to call the parent class constructor
        self.battery_size = battery_size


e1 = ElectricCar("Tesla" , "Model S" , 100)