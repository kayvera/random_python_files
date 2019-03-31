#banned_users = ['andrew', 'carolina', 'david']
#user = 'marie'

#if user not in banned_users:
#	print(user.title() + ", you can post a response if you wish.")

users = []

if users:
	for user in users:
		if user == 'mikayla':
			print('\nWelcome Mikayla, you are the best')
		else:
			print("What's up " + user.title() + ', you bitch!')
else:
	print("We need to find some users first!")

		
#users = ['mikayla','rick','sanchez','chris','mike']

#for user in users:
#	if user == 'mikayla':
#		print('\nWelcome Mikayla, you are the best')
#	elif users:
#		print("What's up " + user.title() + ', you bitch!')


current_users = ['mikayla','rick','sanchez','chris','mike']
new_users = ['Mikayla','rick','john','bobby']
current_lower = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_lower:
		print('This username is already in use, pick another name.')
	else:
		print('This username is available.')

numbers =list(range(1,10))

for number in numbers:
	if number == 1:
		print('\n' + str(number) + 'st')
	elif number == 2:
		print(str(number) + 'nd')
	elif number == 3:
		print(str(number) + 'rd')
	else:
		print(str(number) + 'th')
