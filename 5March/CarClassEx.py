class Car:
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        print(f"{self.make} {self.model} {self.year}")

car_object = Car("WolksWagen","SUV","2019")
car_object.description()