class Car:
    topspeed = 150
    location = 0
    
    def printTopSpeed(self):
        print(f"Top speed: {self.topspeed}")
    
    def drive(self):
        self.location += 10
    
    def stop(self):
        print(f"Your final location is {self.location} miles from where you started")


car1 = Car()

car1.printTopSpeed()

car1.drive()
car1.drive()
car1.drive()

car1.stop()
