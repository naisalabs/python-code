class Vehicle:
    def __init__(self, fare):
        self.fare = fare


class Bus(Vehicle):
    def __init__(self, fare):
        super().__init__(fare)
        self.total_fare = fare + (fare * 10 / 100)   # 10% extra fare


bus = Bus(500)

print("Base fare:", bus.fare)
print("Total fare:", bus.total_fare)