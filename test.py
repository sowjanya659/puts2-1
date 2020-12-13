import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_minnumber1(self):

		solution = self.app.get('/min?X=1,2,77,23,199')
		self.assertEqual(b'1', solution.data)

	def test_minnumber2(self):

		solution = self.app.get('/min?X=89,233,4,2,1,23999')
		self.assertEqual(b'1', solution.data)

	def test_minnumber3(self):

		solution = self.app.get('/min?X=30,5/2,2/3,1.002,100.002')
		self.assertEqual(b'1.0', solution.data)

	def test_minnumber4(self):

		solution = self.app.get('/min?X=22,23,24,25,26,99.89,12')
		self.assertEqual(b'12', solution.data)

	def test_minnumber5(self):

		solution = self.app.get('min?X=1,98,12,14,23,25')
		self.assertEqual(b"1", solution.data) 

	def test_minnumber6(self):

		solution = self.app.get('min?X=10,2,1,2,3,4,5,6,3,2,1,1,123')
		self.assertEqual(b"1", solution.data)

if __name__ == '__main__':
	unittest.main()
