from car import Car

class Battery():
	""" a simple attempt to model a battery for an electric car"""
	
	def __init__(self, battery_size=70):
		"""initialize the battery's attributes"""
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	
	def get_range(self):
		"""print a statement about the range this battery provides"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
			
		message = "This car can go approx. " + str(range)
		message += " miles on a full charge."
		print(message)
		
	
class ElectricCar(Car):
	"""represent aspects of a car, specific to electric vehicles."""
	def __init__(self,make,model,year):
		"""
		initialize attributes of the parent class
		then initialize attributes specific to electric car
		"""
		super().__init__(make,model,year)
		self.battery = Battery()
	

	def fill_gas_tank(self):
		"""
		electric cars don't have gas tanks
		we are pretending that this method is in the parent class
		"""
		print("This car doesn't need a gas tank.")	

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
