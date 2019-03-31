import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	'''Test for 'name_function.py'.'''
	
	def test_first_last_name(self):
		'''do name like 'janis joplin' work?'''
		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')
	
	def test_first_last_name_middle_name(self):
		"""do names like 'Wolfgang amadeus mozart' work?"""
		formatted_name = get_formatted_name(
		'wolfgang','mozart','amadeus')
		self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
	
	
unittest.main()
