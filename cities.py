#prompt = "\nPlease enter the name of a city you have visited:"
#prompt += "\n(Enter 'quit' when you are finished.)"

#while True:
#	city = input(prompt)
	
#	if city == 'quit':
#		break
#	else: 
#		print("I'd love to go to " + city.title() + "!")

#8-6

def city_country(name, country) :
	'''prints name and country together very pretty'''
	formatted_city_country = name + ', ' + country
	return formatted_city_country.title()

print(city_country('san diego', 'america'))
print(city_country('mumbai','india'))
print(city_country('london','england'))

#8-7

def make_album(artist_name, album_title):
	'''return a dictionary with album name and title'''
	info = {'name': artist_name, 'title': album_title}
	return info

album = make_album('paramore','hard times')
print(album)

def make_album(artist_name, album_title, track_number = ''):
	'''return a dictionary with album name and title'''
	info = {'name': artist_name, 'title': album_title}
	if track_number:
		info['track_number'] = track_number
	return info

album = make_album('paramore', 'hard times', track_number = 1)
print(album)

#8-8

def make_album(artist_name, album_title, track_number = ''):
	'''return a dictionary with album name and title'''
	info = {'name': artist_name, 'title': album_title}
	if track_number:
		info['track_number'] = track_number
	return info

while True:
	print('\nPlease tell me the artist:')
	print("(enter 'q' at any time to quit)")
	
	name = input("Artist name: ")
	if name == 'q':
		break
	title = input("Album title: ")
	if title == 'q':
		break
	track = input("Track number: ")
	if track == 'q':
		break
	
	album = make_album(name, title, track)
	print(album)
	
	



