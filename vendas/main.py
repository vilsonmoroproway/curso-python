
from modelos.cliente import Cliente 
from dao.daoCliente import DaoCliente

c = Cliente(2,'maria','maria@gmail.com')

daoCliente = DaoCliente(c)
#daoCliente.salvar()

#clientes = daoCliente.consultar()
#for x in clientes:
 # print(x)

cliente = daoCliente.consultarUm(2)
cliente.display()

#daoCliente.deletar(1)
cliente.setNome('Pedrinho')
cliente.setEmail('pedrinho@gmail.com')
daoCliente.alterar(cliente)

cliente = daoCliente.consultarUm(2)
cliente.display()