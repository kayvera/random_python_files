answer = 17

if answer != 42:
	print("That is not the correct answer. Please try again!")

#7-3

number = input("Please tell me a number: " )
number = int(number)

if number % 2 == 0:
	print("The number " + str(number) + " is even!")
else:
	print("The number " + str(number) + " is odd!")
