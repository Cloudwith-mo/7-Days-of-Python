class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
carA = Car("Mercedes-Benz", "S-Class", "2023")
carB = Car("BMW", "7 Series", "2023")
carC = Car("Audi", "A8", "2023")
carD = Car("Porsche", "Panamera", "2023")
carE = Car("Tesla", "Model S Plaid", "2023")

# print(carA.make)
# print(carA.model)
# print(carA.year)

# print()
# print(carB.make)
# print(carB.model)
# print(carB.year)

# print()
# print(carE.make)
# print(carE.model)
# print(carE.year)


# class Manufacturer(Car):
#     def __init__ (self, make, model, year, country):
#         super().__init__(make, model, year)
#         self.country = country
        
# manufacturer = Manufacturer("BMW", "7 Series", "2023", "Germany")

# print()
# print(manufacturer.make)
# print(manufacturer.model)
# print(manufacturer.year)
# print(manufacturer.country)