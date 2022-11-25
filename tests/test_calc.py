import unittest  # imorting inbuilt python testing module
import calc # where i have mentioned all the functions

class TestCalc(unittest.TestCase): # inheriting python module test case in our Class
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)

    def test_Subtract(self):
        self.assertEqual(calc.sub(10,5),5)
        self.assertEqual(calc.sub(-1,1),-2)
        self.assertEqual(calc.sub(-1,-1),0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-1,1),-1)
        self.assertEqual(calc.multiply(-1,-1),1)  

    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(-1,-1),1)
        self.assertEqual(calc.divide(5,2),2.5)

        """This Check for the assertion raise is coorectly working or not"""
        #self.assertRaises(ValueError, calc.divide, 10, 0) 
        """Another way using context manager for testing assertion raise"""
        with self.assertRaises(ValueError):
            calc.divide(10,0)

    
    def test_Even(self):
        self.assertTrue(calc.iseven(4))

    

if __name__ == '__main__':
    unittest.main()