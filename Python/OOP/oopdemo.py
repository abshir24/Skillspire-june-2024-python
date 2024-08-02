class Vehicle:
    x = 5
    
    def printInfo(self):
        print("Test")



class Car(Vehicle):
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def printCarInfo(self):
        print(f"Make: {self.make}", f"Model: {self.model}", f"color: {self.color}", f"Year: {self.year}")

car1 = Car("-","-","-","-")

car1.printInfo()

# class Plane(Vehicle):
#     pass
