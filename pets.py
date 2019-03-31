#pets = ['dog','cat','dog','goldfish','cat','rabbit', 'cat']
#print(pets)

#while 'cat' in pets:
#	pets.remove('cat')
#print(pets)

def describe_pet(pet_name, animal_type='dog'):
	"""display information about a pet."""
	print("\nI have a " + animal_type + '.')
	print("My " + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('korra', 'cat')

describe_pet(animal_type= 'cat',pet_name= 'korra')
describe_pet(pet_name= 'willie')

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')

#8-3 & 8-3

def make_shirt(size, message):
	"""takes the size and message on the shirt"""
	print("The shirt size is " + size.title() + " and the shirt is going to say " 
	+ message + '.')

make_shirt('medium', 'Hello, world')
make_shirt(message = 'Hello,world', size='medium')
 
def make_shirt(message, size = 'large'):
	"""takes the size and message on the shirt"""
	print("The shirt size is " + size.title() + " and the shirt is going to say " 
	+ message + '.')

make_shirt(message = 'I love python')

#8-5

def describe_city(city_name, city_state):
	'''print the city name and state'''
	print(city_name.title() + " is in " + city_state.title() + '.')

describe_city('san diego', 'california')
describe_city(city_state = 'nevada', city_name = 'reno')
describe_city('miami', 'florida')


