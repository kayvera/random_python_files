class Car():
	''' a simple attempt to represent a car'''
	
	def __init__(self, make, model, year):
		'''intialize attributes to describe a car.'''
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		'''return a neatly formatted descriptive name'''
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		'''print a statement showing the car's mileage '''
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	def update_odometer(self,mileage):
		'''set the odometer reading to the given value
		reject the change if it attempts to roll the odometer back
		'''
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	def increment_odometer(self, miles):
		'''add the given amount to the odometer reading.'''
		self.odometer_reading += miles

