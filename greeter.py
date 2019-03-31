#name = input("Please enter your name: ")
#print("Hello, " + name.title() + "!")

#prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt += "\nWhat is your first name? " #builds on prompt, spans 2 lines

#name = input(prompt)
#print("Hello, " + name.title() + "!")

def greet_user():
	"""Display a simple greeting.""" #docstrig that defines what this function does
	print("Hello")

greet_user()

def greet_user(username):
	"""Display a simple greeting."""
	print("Hello, " + username.title() +  "!")
	
greet_user('jesse')

#8-1

def display_message():
	"""Tells what I am learning in this chp"""
	print("I am learning about python functions in this chapter.")

display_message()

#8-2

def favorite_book(title):
	"""tells favorite book"""
	print("My favorite book is " + title.title() + ".")

favorite_book('Shoe Dog')

def get_formatted_name(first_name, last_name):
	'''return first and last name together'''
	full_name = first_name + ' ' + last_name
	return full_name.title()

# This is an infinite loop!
#while True:
#	print('\nPlease tell me your first name: ')
#	print("(enter 'q' at any time to quit)")
#	f_name = input("First name: ")
#	if f_name == 'q':
#		break
#	l_name = input("Last name: ")
#	if l_name == 'q':
#		break
	
#	formatted_name = get_formatted_name(f_name, l_name)
#	print("\nHello, " + formatted_name + "!")

def greet_users(names):
	'''print a simpe greeting to each user in the list'''
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
	

