class Vehicle(object): #object is a keyword in python
	def __init__(self, make=None, model=None): #start of object definition block
		self.make = make
		self.model = model
		self.kind = "<unknown>" #initialized with the string of unknown
		return
	def getMake(self):
		return self.make
	def getModel(self):
		return self.model
	def setMake(self, make=""):
		self.make = make
		return
	def setModel(self, model=""):
		self.model = model
		return

#GETTER Methods
connie = Vehicle(make="Conestoga", model="Covered Wagon") #instance of a vehicle
print(connie.getMake())
print(connie.getModel())
print(connie) #gives that it knows that this is an object and where it exists.

prairie = Vehicle(make="Prairie Schooner", model="Covered Wagon")
print(prairie.getMake(), prairie.getModel())
print(prairie)

#SETTER Methods
connie.setModel("Wagon") #Change from Covered Wagon to Wagon
print(connie.getModel()) #Wagon


#To define a landcraft, we have to create a generalized object under Vehicle, which would be a sub-class
#Landcraft is based on Vehicle instead of an object.
#So we extend Vehicle with our new class Landcraft
#Vehicle is the parent or super-class

#LANDCRAFT

class Landcraft(Vehicle):
	def __init__(self, make=None, model=None):
		Vehicle.__init__(self, make=make, model=model) #we make sure the parent initialization behavior works
		self.kind = "Landcraft" #This was set to unknown in the original class
		return
	def __repr__(self):
		return f"<Landcraft: make:{self.make} model:{self.model} kind:{self.kind}>"

m1 = Landcraft(make="General Dynamics", model="M1")
print(m1)

bradley = Landcraft(make="Bae Systems", model="Bradley")
print(bradley)

m1.setModel("Abrams M1")
print(m1) #the model would change


#LANDCRAFT SUB-CLASS

class Car(Landcraft):
	def __init__(self, make=None, model=None, vin=None, color="red"):
		Landcraft.__init__(self, make=make, model=model)
		self.vin = vin
		self.color = color
		self.wheels = 0
		self.year = 1900
		return
	
	def getYear(self):
	    return
	
	def setYear(self,year = 1900):
		self.year = year
		return
	
	def __repr__(self):
		return f"<Car: make:{self.make} model:{self.model} year:{self.year}>"


#WATERCRAFT

class Watercraft(Vehicle):
	def __init__(self, make=None, model=None):
		Vehicle.__init__(self, make=make, model=model) #we make sure the parent initialization behavior works
		self.kind = "Landcraft" #This was set to unknown in the original class
		return
	def __repr__(self):
		return f"<Watercraft: make:{self.make} model:{self.model} kind:{self.kind}>"
	

class Motorboat(Watercraft):
	def __init__(self, make=None, model=None, motorhp=None, hulltype=None, passengers=None):
		Landcraft.__init__(self, make=make, model=model)
		self.motorhp = motorhp
		self.hulltype = hulltype
		self.passengers = passengers
		self.year = 1900
	def getYear(self):
		return self.year
	def setYear(self, year=1900):
		self.year = year
		return
	def setPassengers(self, passengers=None):
		self.passengers = passengers
		return
	def __repr__(self):
		return f"<Motorboat: make:{self.make} model:{self.model} horsepower:{self.motorhp} hull construction:{self.hulltype} year:{self.year}>"