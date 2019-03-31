requested_topping = ['mushrooms' , 'extra cheese', 'green peppers']

if requested_topping != 'anchovies':
	print('Hold the anchovies!')

if 'mushrooms' in requested_topping:
	print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
	print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")

requested_topping = ['mushrooms' , 'extra cheese', 'green peppers']

for requested_toppings in requested_topping:
	if requested_toppings == 'green peppers':
		print("Sorry, we are out of green peppers right now!")
	else:
		print('Adding ' + requested_toppings + '.')

print("\nFinished making your pizza!")

requested_topping = []

if requested_topping:
	print('Adding ' + requested_toppings + '.')
	print("\nFinished making your pizza!")
else:
	print("\nAre you sure you want plain pizza")
		
available_toppings = ['mushrooms','olives','green peppers', 'pepperoni',
					  'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print('Adding ' + requested_topping + '.')
	else: 
		print("Sorry, we don't have " + requested_topping + '.')
print("\nFinished making your pizza!")
