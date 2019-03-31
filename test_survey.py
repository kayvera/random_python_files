import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	'''test for the class anonymoussurvey'''
	
	def setUp(self):
		'''
		create a survey and a set of responses for use in all test methods
		'''
		question = 'What language did you first learn to speak?'
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']
	
	def test_store_single_response(self):
		'''test that a single response is stored properly.'''
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)
	
	def test_store_three_response(self):
		'''test that a three responses are stored properly.'''
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

unittest.main()
