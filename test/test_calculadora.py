# test_calculadora.py

import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
      self.assertEqual(calculadora.suma(3,5),8)

    def test_resta(self):
       self.assertEqual(calculadora.resta(3,4),-1)

    def test_multiplica(self):
      self.assertEqual(calculadora.multiplica(2,12),24)

    def test_divide(self):
      self.assertEqual(calculadora.divide(6,3),2)

if __name__ == '__main__':
    unittest.main()
