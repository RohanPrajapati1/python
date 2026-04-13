class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model
    def fuel_type(self):
        return "Pertrol or Diesel"

    
class ElectricCar (Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model) # to call the parent class constructor
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electricity"

e1 = ElectricCar("Tesla" , "Model S" , 100) 