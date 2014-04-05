'''
Created on Mar 9, 2014

@author: anshulchawla
'''
import unittest
from Calc.calculator_main import calculator_main


class CalculatorTest(unittest.TestCase):
    def test_addition(self):
        calculator = calculator_main()
        result = calculator.addition(a=12, b=5)
        self.assertEqual(result, 7, 'Addition Failed')
