#For the Car class initialize the objects with owner name, and a registration number.
#Other variables can include make, model, etc.
#Initialize the Garage class with a name for the garage and a total number of spots.
#Create method to "park" Car objects in the garage.
#Make sure you can't park more cars than spots available!

class Car:
    carcount = 0

    def __init__(self, owner, reginum, make, model, color):
        self.owner = owner
        self.reginum = reginum
        self.make = make
        self.model = model
        self.color = color
        Car.carcount += 1

    def Displaycar(self):
        print "The registration number for this car is", self.reginum, "and it is owned by", self.owner, "."
        print "This car is a", self.make, "brand", self.model, "and it is", self.color, "."



testcar = Car("testname", 256873, "Volvo", "XC60", "Brown")


class Garage:

    def __init__(self):
        self.carspot = []
        self.spotcheck = 3 #this is the available number of spots

    def displayGarage(self,carspot):
        print self.carspot


    def dropoff(self, carspot):
        self.carspot.append(testcar)

testcar.Displaycar()

#print Car.carcount
