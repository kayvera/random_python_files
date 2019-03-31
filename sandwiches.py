#7-8

sandwich_orders = ['ham','turkey','vegetarian','vietnamese','pb&j',
				   'pastrami','pastrami','pastrami']
				   
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
	print("Sorry, the deli is all out of pastrami today.")
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	
	print("I made your " + current_sandwich + " sandwich!")
	finished_sandwiches.append(current_sandwich)
	
print("\nThe following sandwiches were made:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title() + " sandwich.")

#7-9

responses = {}

polling_active = True

while polling_active:
	name = input('\nWhat is your name? ')
	dream_vacation = input("\nIf you could finish one place in the world, where would you go?")

	responses[name] = dream_vacation
	
	repeat = input("\nWould you like another person to respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

print("\n--- Poll Results ---")
for name, dream_vacation in responses.items():
	print(name.title() + " would like to go to " + dream_vacation.title() + ".")
