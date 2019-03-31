
def make_pizza(*toppings):
	'''Summarize the pizza we are about to make'''
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)


def make_pizza(size,*toppings):
	'''Summarize the pizza we are about to make'''
	print("\nMaking a " + str(size) + 
	"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

#this is now a module that only holds functions
