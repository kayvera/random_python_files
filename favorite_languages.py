from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
	language.title() + ".")

favorite_languages = {
	'jen':'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("Sarah's favorite language is " +
		favorite_languages['sarah'].title() +
		".")

person = {
	'first_name':'korra', 
	'last_name':'rivera',
	'age': 3,
	'city': 'san diego',
}
print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())

chris = {'name':'chris','number':7}
toby = {'name':'toby','number':6}
bob = {'name':'bob','number':32}

print(chris['name'].title() + "'s favorite number is " + str(chris['number'])+'.')
print(toby['name'].title() + "'s favorite number is " + str(toby['number'])+'.')
print(bob['name'].title() + "'s favorite number is " + str(bob['number'])+'.')

glossary = {
	'string': 'A series of characters.',
	'comment': 'A note in a program that python interpreter ignores',
}

for word, meaning in glossary.items():
	print(word.title() + ": " + meaning + ".")

favorite_languages = {
	'jen':'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
	language.title() + ".")

for name in favorite_languages.keys():
	print(name.title())

for language in favorite_languages.values():
	print(language.title())
	
favorite_languages = {
	'jen':'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print("Hi " + name.title() +
		", I see your favorite language is " +
		favorite_languages[name].title() + "!") 

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

favorite_languages = {
	'jen':'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
	
for name in sorted(favorite_languages.keys()):
	print("\n" + name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in sorted(favorite_languages.values()):
	print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): #makes non-repetitive
	print(language.title())

glossary = {
	'string': 'A series of characters.',
	'comment': 'A note in a program that python interpreter ignores',
}

for word, meaning in glossary.items():
	print(word.title() + ": " + meaning + ".")

rivers = {
	'nile': 'egybt',
	'zambezi': 'africa',
	'orinoco': 'venezuela',
	'ganges': 'india',
	'missouri': 'missouri',
	}

for river, place in rivers.items():
	print("\nThe " + river.title() + " river runs through " 
	+ place.title() + '.')


favorite_languages = {
	'jen':'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

friends = ['tom','chris','sandy', 'danielle', 'sarah', 'matt', 'ashley']
for name in friends:
	if name in favorite_languages.keys():
		print("Thank you for taking the poll, " + name.title() + '.')
	else:
		print(name.title() + " you should take the poll!")

favorite_languages = {
	'jen':['python','java'],
	'sarah': ['c'],
	'edward': ['ruby','c++'],
	'phil': ['python', 'r'],
	}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())






































