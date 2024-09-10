class Vehicle():
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def get_size(self):
        pass

class Car(Vehicle):
    def get_size(self):
        return "medium"
class Truck(Vehicle):
    def get_size(self):
        return "large"
class Motorcycle(Vehicle):
    def get_size(self):
        return "small"
    
class ParkingSpot():
    def __init__(self, spot_size):
        self.spot_size = spot_size
        self.vehicle = None
    
    def can_fit_vehicle(self, vehicle):
        vehicle_size = vehicle.get_size()
        if self.spot_size == 'small' and vehicle_size == 'small':
            return True
        elif self.spot_size == 'medium' and vehicle_size in ['small', 'medium']:
            return True
        elif self.spot_size == 'large':
            return True
        else:
            return False
    
    def park_vehicle(self, vehicle):
        if self.can_fit_vehicle(vehicle):
            self.vehicle = vehicle
            return True
        return False
    
    def remove_vehicle(self):
        self.vehicle = None


class ParkingLot():
    def __init__(self, small_spot, medium_spot, large_spot):
        self.lots = []

        for _ in range(small_spot):
            self.lots.append(ParkingSpot('small'))
        for _ in range(medium_spot):
            self.lots.append(ParkingSpot('medium'))
        for _ in range(large_spot):
            self.lots.append(ParkingSpot('large'))
    
    def park_vehicle(self, vehicle: Vehicle):
        for lot in self.lots:
            if not lot.vehicle and lot.can_fit_vehicle(vehicle):
                lot.park_vehicle(vehicle)
                return True
        return False

    def free_spot(self, license_plate):
        for lot in self.lots:
            if lot.vehicle and lot.vehicle.license_plate == license_plate:
                lot.remove_vehicle()
                return True
        return False

    def available_spots(self):
        return sum(1 for spot in self.lots if spot.vehicle is None)



parking_lot = ParkingLot(small_spot=2, medium_spot=2, large_spot=1)

# Create some vehicles
car = Car("ABC123")
truck = Truck("TRUCK1")
motorcycle = Motorcycle("MOTO1")

# Try to park the vehicles
print(parking_lot.park_vehicle(car))        # True (Car fits in a medium spot)
print(parking_lot.park_vehicle(truck))      # True (Truck fits in the large spot)
print(parking_lot.park_vehicle(motorcycle)) # True (Motorcycle fits in a small spot)

# Check available spots
print(f"Available spots: {parking_lot.available_spots()}")  # 2 spots remaining

# Free up a spot
print(parking_lot.free_spot("ABC123"))     # True (Car is removed)

# Check available spots again
print(f"Available spots: {parking_lot.available_spots()}")
