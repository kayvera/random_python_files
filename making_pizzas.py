pizzas = ['peperroni','sausage','cheese','combo']

for pizza in pizzas:
	print("I love to eat " + pizza + " pizza.")
print("I really enjoy all types of pizza because it tastes bomb af!")

#store information about a pizza being ordered
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

#summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
	"with the following toppings:")
	
for topping in pizza['toppings']:
	print("\t" + topping)
	
#7-4

prompt = "Please enter the pizza toppings you want on your pizza."
prompt += "\nWhen you're finished, please type 'quit': "

message = ''
toppings = []

#active = True
#while active:
#	print("We will add that topping to your pizza!")
#	toppings.append(message)
#	message = input(prompt)
	
#	if message == 'quit':
#		active = False
#	else:
#		print(toppings)

def make_pizza(*toppings):
	'''print the list of toppings that have been requested.'''
	print(toppings)
	
#make_pizza('pepperoni')
#make_pizza('mushrooms','green peppers','extra cheese')

from pizza import make_pizza as mp
#import pizza as p
#import pizza
#from pizza import *

pizza.mp(16,'pepperoni')
pizza.mp(12,'mushrooms','green peppers','extra cheese')

