class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def start_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine has started."

    def stop_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine has stopped."
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it."
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
my_new_car = Car('nissan', 'Z', 2023)
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())
my_new_car.odometer_reading = 12456
print(my_new_car.read_odometer())
my_new_car.update_odometer(10000)
print(my_new_car.read_odometer())
my_new_car.increment_odometer(500)
print(my_new_car.read_odometer())

