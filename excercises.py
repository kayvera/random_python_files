#8-9

def show_magicians(unshown_magicians, shown_magicians):
	while unshown_magicians:
		current_magician = unshown_magicians.pop()
		shown_magicians.append(current_magician)
	print("\nThe following magicians have been shown:")
	for shown_magician in shown_magicians:
		print(shown_magician.title())

unshown_magicians = ['harry houdini','david blaine','shin lim']
shown_magicians = []

show_magicians(unshown_magicians,shown_magicians)

#8-10

def show_magicians(unshown_magicians, shown_magicians):
	while unshown_magicians:
		current_magician = unshown_magicians.pop()
		shown_magicians.append(current_magician)

def make_great(shown_magicians):
	print("\nThe following magicians have been shown:")
	for shown_magician in shown_magicians:
		print("The Great " + shown_magician.title())
	

unshown_magicians = ['harry houdini','david blaine','shin lim']
shown_magicians = []

show_magicians(unshown_magicians,shown_magicians)
make_great(shown_magicians)

print(unshown_magicians)

#8-11

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)

#8-12

def make_sandwich(*items):
	'''Summarize the sandwich we are about to make'''
	print("\nMaking a sandwich with the following items:")
	for item in items:
		print("- " + item)

make_sandwich('cheese','lettuce','tomato','onion','bread','ham')

#8-13

def build_profile(first, last, **user_info):
	'''build a dictionary containing everything we know about a user'''
	profile = {}
	profile['first_name'] = first
	profile['last_name']= last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('mikayla','rivera', 
							  location = 'san diego',
							  field = 'data',
							  hobby = 'golf')

print(user_profile)

#8-14

def make_car(manufacturer, model, **car_info):
	'''build a dictionary containing everything we know about a user'''
	car = {}
	car['Manufacturer'] = manufacturer
	car['Model_name']= model
	for key, value in car_info.items():
		car[key] = value
	return car

car_profile = make_car('subaru','outback',
						color = 'blue',
						tow_package = True)
print(car_profile)

#9-1 & 9-4 & 9-6

class Restaurant():
	
	def __init__(self, restaurant_name, cuisine_type):
		self.name= restaurant_name
		self.type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		print("\nThe restaurant's name is " + self.name.title() + ".")
		print("The restaurant serves " + self.type.title() + " food.")

	def amount_served(self):
		print("This restaurant has served " + str(self.number_served) 
		+ " customers!")
	
	def open_restaurant(self):
		print(self.name.title() + " is now open.")
	
	def update_customers(self, customers):
		self.number_served = customers	
	
	def increment_number_served(self, customers_served):
		self.number_served += customers_served

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name, cuisine_type):
		"""
		initialize attributes of the parent class
		then initialize attributes specific to the ice cream shop
		"""
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = ['chocolate', 'pistachio','mint','vanilla']
	
	def list_flavors(self):
		print("\nThe flavors we serve are:")
		for flavor in self.flavors:
			print("- " + flavor.title()) 

restaurant = Restaurant("santanas",'mexican')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.amount_served()

restaurant.number_served = 33
restaurant.amount_served()

restaurant.update_customers(23)
restaurant.amount_served()

restaurant.increment_number_served(15)
restaurant.amount_served()

ice_cream = IceCreamStand('cold stone', 'ice cream')
ice_cream.list_flavors()  

#9-2

restaurant = Restaurant("in&out",'american')
restaurant.describe_restaurant()

restaurant = Restaurant("panda express",'chinese')
restaurant.describe_restaurant()

restaurant = Restaurant("cali baguette",'vietnamese')
restaurant.describe_restaurant()

#9-3 & 9-3 & 9-7 & 9-8

class User():
	
	def __init__(self, first_name, last_name, city, state):
		self.fname = first_name
		self.lname = last_name
		self.full_name = self.fname + " " + self.lname
		self.city = city
		self.state = state
		self.login_attempts = 0
	
	def describe_user(self):
		print("\n" + self.full_name.title() + " is from " +
		self.city.title() + ", " + self.state.title() + ".")
	
	def increment_login_attempts(self):
		self.login_attempts += 1
		
		if self.login_attempts is 1:
			print("You now have " + str(self.login_attempts) + 
			" login attempt.")
		else:
			print("You now have " + str(self.login_attempts) + 
			" login attempts.")
	
	def reset_login_attempts(self):
		self.login_attempts = 0
		print("You have reset your login attempts to " + 
		str(self.login_attempts) + ".")
	
	def greet_user(self):
		print("Hello, " + self.fname.title() + ".")
	
class Privilege():
	def __init__(self, privileges = ['can add post','can delete post','can ban user']):
		self.privileges = privileges
	
	def show_privilege(self):
		print("\nThe admin's privileges are:")
		for privilege in self.privileges:
			print("- " + privilege) 
	
class Admin(User):
	def __init__(self, first_name, last_name, city, state):
		super().__init__(first_name, last_name, city, state)
		self.privilege = Privilege()	
		
		
user_1 = User('mikayla', 'rivera', 'san diego', 'california')
user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()

admin_1 = Admin('mikayla','rivera','san diego','california')
admin_1.privilege.show_privilege()

#9-9

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
	
	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
			print("This car now has a " + str(self.battery_size) + "-kWh battery.")
		else:
			print("This car already has a " + str(self.battery_size) + "-kWh battery.")
		
	
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
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()

#9-14

from random import randint

class Die():
	def __init__(self, sides=6):
		self.sides = sides
	
	def roll_dice(self):
		return randint(1,self.sides)

d6 = Die()

results = []
for roll_num in range(10):
	result = d6.roll_dice()
	results.append(result)
print("\n10 rolls of a 6-sided die:")
print(results)

d10 = Die(sides = 10)

results = []
for roll_num in range(10):
	result = d10.roll_dice()
	results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

d20 = Die(sides = 20)

results = []
for roll_num in range(20):
	result = d20.roll_dice()
	results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)

#10-1

filename = 'random_thoughts.txt'

print("\n---Reading in the entire file")
with open(filename) as file_object:
	lines = file_object.read()
print(lines)

print("\n---Looping over the lines:")
with open(filename) as f:
	for line in f:
		print(line.rstrip())

print("\n---Storing the lines in the list")
with open(filename) as f:
	lines = f.readlines()

for line in lines:
	print(line.rstrip())

#10-2

filename = 'random_thoughts.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	
for line in lines:
	line = line.rstrip()
	print(line.replace('Python', 'C'))

#10-3

#filename = 'guest.txt'

#guest_name = input("Enter your name: ")

#with open(filename, 'w') as f:
#	 f.write(guest_name)
	
#10-4

#filename = 'guest_book.txt'

#while True:
#	name = input("\nEnter your name: ")
#	if name == 'quit':
#		break
#	else: 
#		with open(filename, 'w') as f:
#			f.write(name + '\n')
#		print("Hi " + name + ", you've been added to the list")

#10-5

#filename = '10_5.txt'

#responses = []
#while True:
#	response = input("\nWhy do you like programming? ")
#	responses.append(response)
	
#	continue_poll = input("Would you like someone else to respond? (y/n)")
#	if continue_poll != 'y':
#		break
#	with open(filename, 'a') as f:
#		for response in responses:
#			f.write(response + '\n')
#10-6

#while True:
#	try:
#		x = input("Give me a number: ")
#		x = int(x)

#		y = input("Give me another number: ")
#		y = int(y)

#	except ValueError:
#		print("Sorry, I really needed a number.")

#	else:
#		sum = x + y
#		print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
	
#10-7

#print("Enter 'q' at any time to quit.\n")

#while True:
#   try:
#      x = input("\nGive me a number: ")
#        if x == 'q':
#            break

#        x = int(x)

#        y = input("Give me another number: ")
#        if y == 'q':
#            break

#        y = int(y)

#    except ValueError:
#        print("Sorry, I really needed a number.")

#    else:
#        sum = x + y
#        print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
	
#10-8

filenames = ['cats.txt', 'dogs.txt', 'mice.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")

#10-9
filenames = ['cats.txt', 'dogs.txt', 'mice.txt']

for filename in filenames:
    
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        print("\nReading file: " + filename)
        print(contents)

#10-10

def count_a_word(filename):
	'''count the approx number of words in the file'''
	try:
		with open(filename, encoding = 'utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		#msg = "Sorry, the file " + "'" + filename + "'" + " does not exist."
		#print(msg)
		pass #silent fail
	else: 
		'''Count the approx. number of time the word the is used in the file'''
		words = contents.lower().count('the')
		print("The word 'the' appears " + str(words) + ' times.')		
	
filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
	count_a_word(filename)
	
#10-11

import json

number = input("What's your favorite number? ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("Thanks! I'll remember that.")
    
#10-12

import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print("I know your favorite number! It's " + str(number) + ".")
    
#10-13

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct = input("Are you " + username + "? (y/n) ")
        if correct == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
