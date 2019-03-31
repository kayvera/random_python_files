users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'eintstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
			
pets = {
	'korra':{ 
		'type':'cat',
		'age': 3,
		},
	'sydney':{ 
		'type':'dog',
		'age': 2,
		},
	'roxy':{ 
		'type':'dog',
		'age': 1,
		},
}

for pet_name, pet_info in pets.items():
	print("\nPet's name: " + pet_name.title())
	species = pet_info['type']
	age = pet_info['age']
	
	print("\tSpecies: " + species.title())
	print("\tAge: " + str(age))

favorite_places = {
	'jim':{
		'places' : ['italy','france'],
		},
	'danielle':{
		'places' : ['my bedroom','UK'],
		},
	'ashley':{
		'places' : ['strip clubs','bars'],
		},
	}

for people, user_info in favorite_places.items():
	print(people.title() + "'s favorite places are:")
	location = user_info['places']
	for place in location:
		print("\t" + place.title())

favorite_numbers = {
	'george':{
		'numbers': [7,12],
		},
	'toby':{
		'numbers': [6,34],
		},
	'bob':{
		'numbers': [32,18],
		},
	}

for people, user_info in favorite_numbers.items():
	print(people.title() + "'s favorite numbers are:")
	numbers = user_info['numbers']
	for number in numbers:
		print("\t" + str(number))
		

		
		
		
		
		
		
		
		
		
		
		
		
		
