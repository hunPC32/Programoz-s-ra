import unittest
from task_base import *

class TestClass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(round(circleArea(7), 1), 153.9)
    def test_2(self):
        self.assertEqual(nameReverse("Nemes Tamás"), "Tamás Nemes")
    def test_3(self):
        self.assertEqual(easyMath(5), 615)
    def test_4(self):
        self.assertEqual(difference(-1, 5), 6)
    def test_4_2(self):
        self.assertEqual(difference(5, -1), 6)
    def test_5(self):
        self.assertEqual(int(bmiIndex(88, 1.84)*100), 2599)
    def test_6(self):
        self.assertEqual(digitsSum(1994), 23)
    def test_7(self):
        self.assertEqual(sortThree(8,3,4), [3, 4, 8])
    def test_8(self):
        self.assertEqual(bePositive([-1, 2, 3, -10, 5, -6]), [2,3,5])
    def test_9(self):
        self.assertEqual(str(decimalToBinary(58)), "111010")
    def test_10(self):
        self.assertEqual(str(decimalToHexa(19940807)).upper(),"13045C7")

if __name__=='__main__':
    unittest.main()