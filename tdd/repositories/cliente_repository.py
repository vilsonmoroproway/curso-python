class ClienteRepository:
    def __init__(self):
        self.clientes = {}

    def salvar(self, cliente):
        self.clientes[cliente.id] = cliente

    def consultar(self, id):
        return self.clientes.get(id)

    def consultarTodos(self):
        return self.clientes

    def excluir(self, id):
        if id in self.clientes:
           del self.clientes[id] 

    def alterar(self,cliente):
        if cliente in self.clientes:
           #self.clientes[cliente.id].nome = cliente.nome
           #self.clientes[cliente.id].email = cliente.email
           self.clientes = cliente