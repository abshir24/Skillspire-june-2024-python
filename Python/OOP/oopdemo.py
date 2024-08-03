class Vehicle:
    def __init__(self,type, weight):
        self.type = type
        self.weight = weight

    def printVehicleInfo(self):
        print(f"Type: {self.type}", f"Weight: {self.weight}")
    

class Plane(Vehicle):
    def __init__(self,model,color, passengers, type, weight):   
        self.model = model
        self.color = color
        self.passengers = passengers
        
        super().__init__(type, weight)


    def printPlaneInfo(self):
        print(f"Model: {self.model}", f"Number of Passengers: {self.passengers}")
        

plane = Plane("Boeing 757", "Blue", 150, "Plane", 50000) 

plane.printVehicleInfo()



