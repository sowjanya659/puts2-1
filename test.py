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
