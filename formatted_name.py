def get_formatted_name(first_name, last_name):
	'''return first and last name together'''
	full_name = first_name + ' ' + last_name
	return full_name.title()

muscian = get_formatted_name('jimi', 'hendrix')
print(muscian)


def get_formatted_name(first_name, middle_name, last_name):
	'''return first and last name together'''
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('john','lee','hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name = ''):
	'''return first and last name together'''
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else: 
		full_name = first_name + ' ' + last_name	
	return full_name.title()

muscian = get_formatted_name('justin', 'bieber')
print(muscian)

musician = get_formatted_name('john','lee','hooker')
print(musician)


