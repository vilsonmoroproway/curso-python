import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        resultado = Calculadora.somar(10,5)
        self.assertEqual(resultado, 15)

    def test_subtrair(self):
        resultado = Calculadora.subtrair(10,5)
        self.assertEqual(resultado, 5)

    def test_multiplicar(self):
        resultado = Calculadora.multiplicar(10,5)
        self.assertEqual(resultado, 50)

    def test_dividir_com_divisor_diferente_Zero(self):
            resultado = Calculadora.dividir(10,5)
            self.assertEqual(resultado, 2)

    def test_dividir_divisor_zero(self):
        with self.assertRaises(ValueError):
          Calculadora.dividir(10, 0)       


if __name__ == "__main__":
    unittest.main()