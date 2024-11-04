import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) # actual output vs expected output

    # Add the following test methods to the TestCalculator class:
    #Add
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0),1)
    
    #subtract
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
    
    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-3, -1), -2)

    #multiply
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
    
    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
    
    def test_devide_negative(self):
        self.assertEqual(self.calc.divide(4, -2), "error")

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(6, 2), 0)

    def test_modulo_negative(self):
        self.assertEqual(self.calc.modulo(2, 2), 0)

if __name__ == '__main__':
    unittest.main()