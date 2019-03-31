for value in range(1,5):
	print(value)

numbers = list(range(1,6)) #turns range into list 
print(numbers)

even_numbers = list(range(2,11,2)) #starts with value to and goes to 11, adds 2 repeatedly
print(even_numbers)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square) #add to list the squared values

print(squares)

#or

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

