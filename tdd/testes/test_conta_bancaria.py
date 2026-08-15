import unittest
from conta_bancaria import ContaBancaria

class TesteContaBancaria(unittest.TestCase):
    def test_criar_conta_com_saldo_inicial(self):
        conta = ContaBancaria(100)
        saldo = conta.consultar_saldo()
        self.assertEqual(saldo,100)

    def test_permitir_deposito(self):
       conta = ContaBancaria(100)
       conta.depositar(50)
       novoSaldo = conta.consultar_saldo()
       self.assertEqual(novoSaldo, 150)

    def test_permitir_saque(self):
           conta = ContaBancaria(100)
           conta.sacar(50)
           novoSaldo = conta.consultar_saldo()
           self.assertEqual(novoSaldo, 50)

    def test_nao_permitir_saque_maior_que_saldo(self):
        conta = ContaBancaria(100)
        with self.assertRaises(ValueError):
            conta.sacar(150)
            
if __name__ == "__main__":
    unittest.main()