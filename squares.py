squares = [value**2 for value in range(1,11)] #start with your expression
print(squares)

for number in range(1,21):
	print(number)

millions = []
for value in range(1,1000000):
	millions.append(value + 1)

print(max(millions))
print(min(millions))
print(sum(millions))

odd_numbers = list(range(1,20,2))
print(odd_numbers)

odd_numbers = []
for value in range(1,20,2):
	odd_numbers.append(value)

print(odd_numbers)
	
three = []
for value in range(3,30,3):
	three.append(value)
print(three)

squares = [value**3 for value in range(1,11)]
print(squares)
