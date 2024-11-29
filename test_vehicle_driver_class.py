
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True

class Driver:
    def __init__(self, name):
        self.name = name

    def take_vehicle(self, vehicle):
        if vehicle.is_running:
            raise Exception("The vehicle is not available for a ride.")
        vehicle.start()

# Example usage:
car = Vehicle("Toyota", "Corolla")
driver = Driver("Alice")

# The driver takes the vehicle and starts it
driver.take_vehicle(car)

# Testing the behavior when trying to take the same vehicle again
try:
    driver.take_vehicle(car)
except Exception as e:
    print(e)  # Output: "The vehicle is not available for a ride."