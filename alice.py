'''this file doesnt currently exist error'''

filename = 'alison.txt'

try:
	with open(filename, encoding ='utf-8') as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + "'" + filename + "'" + " does not exist."
	print(msg)

filename = 'alice.txt'

try:
	with open(filename, encoding = 'utf-8') as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + "'" + filename + "'" + " does not exist."
	print(msg)
else: 
	#Count the approx. number of words in the file
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")

def count_words(filename):
	'''count the approx number of words in the file'''
	try:
		with open(filename, encoding = 'utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		#msg = "Sorry, the file " + "'" + filename + "'" + " does not exist."
		#print(msg)
		pass #silent fail
	else: 
		'''Count the approx. number of words in the file'''
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")	

filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
	count_words(filename)


