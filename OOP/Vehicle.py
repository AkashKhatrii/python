class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def vehicle_info(self):
        print(f"Vehicle info: {self.make}, {self.model}.")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def car_info(self):
        print(f"Car info: {self.make}, {self.model}, {self.num_doors}")

class MotorCycle(Vehicle):
    def __init__(self, make, model, type):
        super().__init__(make, model)
        self.type = type
    
    def motorcycle_info(self):
        print(f"Car info: {self.make}, {self.model}, {self.type}")

car = Car("Toyota", "Corolla", 4)
motorcycle = MotorCycle("Yamaha", "YZF-R3", "Sport")
car.vehicle_info()
car.car_info()
motorcycle.vehicle_info()
motorcycle.motorcycle_info()