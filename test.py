import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_maxnumber1(self):

		solution = self.app.get('/max?X=1,2,77,23,199,0.2')
		self.assertEqual(b'199', solution.data)

	def test_maxnumber2(self):

		solution = self.app.get('/max?X=1/2,89,233,4,2,1,23999')
		self.assertEqual(b'23999', solution.data)

	def test_maxnumber3(self):

		solution = self.app.get('/max?X=30,5/2,2/3,1.002,100.002')
		self.assertEqual(b'100.0', solution.data)

	def test_maxnumber4(self):

		solution = self.app.get('/max?X=22,23,24,25,26,99.89,12')
		self.assertEqual(b'100.0', solution.data)

	def test_maxnumber5(self):

		solution = self.app.get('max?X=1,98,12,14,23,25')
		self.assertEqual(b"98", solution.data) 

	def test_maxnumber6(self):

		solution = self.app.get('max?X=10,2,1,2,3,4,5,6,3,2,1,1,123')
		self.assertEqual(b"123", solution.data)

if __name__ == '__main__':
	unittest.main()
