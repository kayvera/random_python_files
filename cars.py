cars = ['bmw','audi','toyota','subaru']
cars.sort() #makes alphabetical
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse = True) #reverse alphabetical order
print(cars)

print(sorted(cars)) #doesnt affect long term order of the list 

cars = ['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)

print(len(cars))

locations = ['japan','italy','costa rica', 'london', 'south korea']
print(locations)

print(sorted(locations))
print(locations)

print(sorted(locations, reverse= True))
print(locations)

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse = True)
print(locations)

print(len(locations))

#index -1 always produces the last item in the list

cars = ['bmw','audi','toyota','subaru']
for car in cars: 
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
#7-1		
#rental_car = input("What kind of rental car do you want?: ")
#print("Let me see if we can find you a " + rental_car.title() + ".")


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
	

#my_new_car = Car('audi','a4', 2016)
#print("\n" + my_new_car.get_descriptive_name())
#my_new_car.read_odometer()

#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()

#my_new_car.update_odometer(23)
#my_new_car.read_odometer()

my_used_car = Car('subaru','outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()







































