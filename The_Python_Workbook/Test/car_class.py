class Car:
    def __init__(self, brand, model, percentFuel, yearProduced):
        self.brand = brand
        self.model = model
        self.percentFuel = percentFuel
        self.yearProduced = yearProduced

    def __str__(self) -> str:
        return f'{self.brand}, {self.model}, {self.percentFuel}, {self.yearProduced}'

    def addFuel(self, fuelToAdd):
        if fuelToAdd + self.percentFuel > 1:
            print("Warning danger of petrol spill.")
            self.percentFuel = 1
        else:
            self.percentFuel = self.percentFuel + fuelToAdd
            print("Percent fuel after adding ",
                  fuelToAdd, " : ", self.percentFuel)


myVW = Car('VW', 'Beetle', 0.3, 2010)
myMazda = Car('Mazda', '323', 1.0, 2003)


print(myVW)
myVW.addFuel(.7)
