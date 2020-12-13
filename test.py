import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_mediantest1(self):

		solution = self.app.get('/median?X=22.222,98,4,2,1,5,6,77,99,89')
		self.assertEqual(b'14.111', solution.data)

	def test_mediantest2(self):

		solution = self.app.get('/median?X=1/2,89')
		self.assertEqual(b'44.75', solution.data)

	def test_mediantest3(self):

		solution = self.app.get('/median?X=30,5/2')
		self.assertEqual(b'16.25', solution.data)

	def test_mediantest4(self):

		solution = self.app.get('/median?X=22,23,24,25,26,27,28,100')
		self.assertEqual(b'25.5', solution.data)

	def test_mediantest5(self):

		solution = self.app.get('median?X=1,98')
		self.assertEqual(b"49.5", solution.data) 

	def test_mediantest6(self):

		solution = self.app.get('median?X=10,2,1,2,3,4,5,6,7,8,9,3,2,1,1,123')
		self.assertEqual(b"3.5", solution.data)

if __name__ == '__main__':
	unittest.main()
