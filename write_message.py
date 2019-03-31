filename = 'programming.txt'

with open(filename, 'w') as file_object:
	'''stores text to an empty file'''
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

filename = 'programming.txt'

with open(filename, 'a') as file_object:
	'''opens in append and stores without erasing content, just adds'''
	file_object.write("I love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
