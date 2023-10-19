# test_mi_programa.py

import unittest
from suma import suma


class TestMiPrograma(unittest.TestCase):

  def test_suma_positiva(self):
    self.assertEqual(suma(2, 3), 5)

  def test_suma_negativa(self):
    self.assertEqual(suma(-2, -3), -51)


if __name__ == '__main__':
  unittest.main()
