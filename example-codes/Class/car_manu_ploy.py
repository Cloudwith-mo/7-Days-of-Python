class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def speak(self):
        print("The car company, {}, makes {}.".format(self.model, self.make))
        



class Manufacturer(Car):
    def __init__ (self, make, model, year, country):
        super().__init__(make, model, year)
        self.country = country
    
    def speak(self):
        print("The car company, {}, makes {}, & their manufactured in {}".format(self.make, self.model, self.country))
        
car = Car("Toyota", "Camry", 2022)
manufacturer = Manufacturer("Mercedes", "Maybach", 2022, "Germany")

car.speak()
manufacturer.speak()