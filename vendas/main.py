
from modelos.cliente import Cliente 
from modelos.produtos import Produto

from dao.daoCliente import DaoCliente
from dao.daoProduto import DaoProduto

c = Cliente(2,'maria','maria@gmail.com')

daoCliente = DaoCliente(c)
#daoCliente.salvar()

#clientes = daoCliente.consultar()
#for x in clientes:
 # print(x)

cliente = daoCliente.consultarUm(2)
#cliente.display()

#daoCliente.deletar(1)
cliente.setNome('Pedrinho')
cliente.setEmail('pedrinho@gmail.com')
daoCliente.alterar(cliente)

cliente = daoCliente.consultarUm(2)
#cliente.display()

p = Produto(2,'trigo', 3.85, 10)
daoProduto = DaoProduto(p)

#daoProduto.salvar()
produtos = daoProduto.consultar()
for x in produtos:
    print(x)

produto = daoProduto.consultarUm(2)
produto.display()

produto.setDescricao('Trigo especial')
daoProduto.alterar(produto)