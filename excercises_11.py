#11-1 & 11-2

def get_formatted_place(city, country, population = ''):
	'''generate the full name of the city and country'''
	if population:
		city_country = city + ', ' + country + ' - population ' + population
	else:
		city_country = city + ', ' + country
	return city_country.title()

print("Enter 'q' at any time to quit.")
while True:
	city = input("\nPlease give me a city: ")
	if city == 'q':
		break
	country = input("Please give me the matching country: ")
	if country == 'q':
		break
		
	full_location = get_formatted_place(city,country)
	print("\tNeatly formatted location: " + full_location + '.')

import unittest

class LocationTestCase(unittest.TestCase):
	'''tests for get_formatted_place() function'''
	
	def test_city_country(self):
		'''do places like San Diego, United States work?'''
		full_location = get_formatted_place('san diego','america')
		self.assertEqual(full_location, 'San Diego, America')

	def test_city_country_population(self):
		'''do places like San Diego, United States work?'''
		full_location = get_formatted_place('san diego','america','3000000')
		self.assertEqual(full_location, 'San Diego, America - Population 3000000')
		
unittest.main() 



