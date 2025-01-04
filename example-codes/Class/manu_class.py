# main.py

from car_class import Car  # Import the Car class from class.py

class Manufacturer(Car):
    def __init__(self, make, model, year, country):
        super().__init__(make, model, year)  # Call the parent class constructor
        self.country = country

# Example usage
manufacturer = Manufacturer("BMW", "7 Series", "2023", "Germany")

print(manufacturer.make)
print(manufacturer.model)
print(manufacturer.year)
print(manufacturer.country)
