import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_averagetest1(self):

		solution = self.app.get('/average?X=1,2,5,4,3,2')
		self.assertEqual(b'2.8333333333333335', solution.data)

	def test_averagetest2(self):

		solution = self.app.get('/average?X=0.5,1.5,2,77,8,6,5')
		self.assertEqual(b'14.285714285714286', solution.data)

	def test_meantest1(self):

		solution = self.app.get('/mean?X=12.23899904,1,8.9,3,2.4,5')
		self.assertEqual(b'5.423166506666667', solution.data)

	def test_meantest2(self):

		solution = self.app.get('/mean?X=1/2,99')
		self.assertEqual(b'49.75', solution.data)

	def test_meantest3(self):

		solution = self.app.get('/mean?X=23,5/3')
		self.assertEqual(b'12.333333333333334', solution.data)

	def test_avgtest1(self):

		solution = self.app.get('/avg?X=0,22,23,6,2')
		self.assertEqual(b'10.6', solution.data)

	def test_avgtest2(self):

		solution = self.app.get('/avg?X=22,23,24,3,23,12,9,1,0.02')
		self.assertEqual(b'13.002222222222223', solution.data)

	def test_avgtest3(self):

		solution = self.app.get('avg?X=1,1,1/2')
		self.assertEqual(b'0.8333333333333334', solution.data) 

	def test_avgtest4(self):

		solution = self.app.get('avg?X=10,2,1,2,3,4,5,6,7,8,9,3,2,1,1,123')
		self.assertEqual(b'11.6875', solution.data)


if __name__ == '__main__':
	unittest.main()
