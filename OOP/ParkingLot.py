from enum import Enum

class VehicleType(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Vehicle:
    def __init__(self, type: VehicleType):
        if not isinstance(type, VehicleType):
            raise TypeError("type must be of vehicletype enum.")
        self.type = type


class ParkingSpot:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.is_available = True
        self.vehicle = None
    
    def park_vehicle(self, vehicle):
        if self.is_available:
            self.vehicle = vehicle
            self.is_available = False
            return True
        return False
    
    def unpark_vehicle(self):
        if not self.is_available:
            self.is_available = True
            self.vehicle = None
            return True
        return False

    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
        return f"{self.id} - {self.type} - {status}"

class ParkingFloor:
    def __init__(self, no, small_type, mid_type, large_type):
        self.no = no
        self.spots = []

        for id in range(small_type):
            self.spots.append(ParkingSpot(f"s-{id}", VehicleType.SMALL))
        for id in range(mid_type):
            self.spots.append(ParkingSpot(f"m-{id}", VehicleType.MEDIUM))
        for id in range(large_type):
            self.spots.append(ParkingSpot(f"l-{id}", VehicleType.LARGE))

    def is_spot_available(self, vehicle_type):
        for idx, spot in enumerate(self.spots):
            if spot.type == vehicle_type and spot.is_available:
                return idx
        return None

    def park_vehicle(self, spot_idx, vehicle):
        if self.spots[spot_idx].park_vehicle(vehicle):
            return True
        return False
    
    def unpark_vehicle(self, spot_idx):
        return self.spots[spot_idx].unpark_vehicle()
    

    def display_spots(self):
        for spot in self.spots:
            print(spot)

class ParkingLot:
    def __init__(self, total_floors):
        self.total_floors = total_floors
        self.current_floors = 0
        self.floors = []


    def add_floor(self, small, mid, large):
        if self.current_floors >= self.total_floors:
            print("Cannot add more floors to parking lot.")
        else:
            self.floors.append(ParkingFloor(len(self.floors) + 1, small, mid, large))
            self.current_floors += 1
            print("Floor added.")

    def park_vehicle(self, vehicle):
        for floor in self.floors:
            spot_idx = floor.is_spot_available(vehicle.type)
            if spot_idx is not None:
                floor.park_vehicle(spot_idx, vehicle)
                print(f"Vehicle parked on {floor.no} at spot {floor.spots[spot_idx].id}")
                return floor, spot_idx
        print("Cannot park vehicle")
        return None, None

    def unpark_vehicle(self, floor, spot_idx):
        
        if floor.unpark_vehicle(spot_idx):
            print("Vehicle unparked")

    def display_spots(self):
        for floor in self.floors:
            floor.display_spots()

if __name__ == "__main__":

    pl = ParkingLot(2)
    pl.add_floor(2, 2, 2)

    v1 = Vehicle(VehicleType.SMALL)
    v2 = Vehicle(VehicleType.MEDIUM)
    v3 = Vehicle(VehicleType.SMALL)

    pl.add_floor(1, 1, 1)
    v4 = Vehicle(VehicleType.SMALL)



    floor, spot = pl.park_vehicle(v1)
    floor2, spot2 = pl.park_vehicle(v2)
    floor3, spot3 = pl.park_vehicle(v3)
    floor4, spot4 = pl.park_vehicle(v4)

    pl.display_spots()

    

            

    

    


