import unittest
from modelos.cliente import Cliente
from repositories.cliente_repository import ClienteRepository

class TesteClienteRepository(unittest.TestCase):
    def test_salvar(self):
        cliente = Cliente(1,'joao','joao@gmail.com')
        repository = ClienteRepository()
        repository.salvar(cliente)

        novoCliente = repository.consultar(cliente.id)

        self.assertTrue(novoCliente.id == cliente.id)
        self.assertEqual(novoCliente.nome, cliente.nome)
        self.assertEqual(novoCliente.email, 'joao@gmail.com')

    def test_consultar(self):
        repository = ClienteRepository()
        
        cliente = Cliente(1,'joao','joao@gmail.com')        
        repository.salvar(cliente)

        cliente2 = Cliente(2,'maria','maria@gmail.com')        
        repository.salvar(cliente2)

        clientes = repository.consultarTodos()
        self.assertTrue(len(clientes) == 2)

    def test_consultar_cliente_inexistente(self):
        repository = ClienteRepository()
        novoCliente = repository.consultar(5)
        self.assertIsNone(novoCliente)

    def test_excluir(self):
       repository = ClienteRepository()
       cliente = Cliente(1,'joao','joao@gmail.com')        
       repository.salvar(cliente) 

       repository.excluir(1)
       self.assertIsNone(repository.consultar(1))

    def test_alterar(self):
        repository = ClienteRepository()
        cliente = Cliente(1,'joao','joao@gmail.com')        
        repository.salvar(cliente)

        cliente.nome = 'maria'
        cliente.email = 'maria@gmail.com'
        repository.alterar(cliente)

        clienteAlterado = repository.consultar(1)
        self.assertEqual(clienteAlterado.nome, 'maria')

if __name__ == "__main__":
    unittest.main()