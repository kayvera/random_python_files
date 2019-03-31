my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]#copies list and makes a new list

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

foods = ['pizza', 'potato', 'grapefruit', 'apple', 'olive', 'beef']

print('\n' + "The first three items in the list are:")
print(foods[:3])

print('\n' + "Three items from the middle of the list are:")
print(foods[1:4])

print('\n' + "The last three items in the list are:")
print(foods[-3:])

pizzas = ['peperroni','sausage','cheese','combo']
friend_pizzas = pizzas[:]

pizzas.append('pesto')
friend_pizzas.append('pineapple')

print(pizzas)
print(friend_pizzas)

for pizza in pizzas[:3]:
	print(pizza)
	
#7-2	

dinner = input("How many people are in your dinner group?: ")
dinner = int(dinner)

if dinner >= 8:
	print("Sorry, but you will have to wait for a table!")
else: 
	print("Your table is ready!")
	































