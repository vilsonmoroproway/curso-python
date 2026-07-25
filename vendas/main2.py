from dao.daoPedido import DaoPedido
from dao.daoCliente import DaoCliente
from dao.daoProduto import DaoProduto


from modelos.pedido import Pedido
from modelos.cliente import Cliente
from modelos.produtos import Produto
from modelos.itenPedido import ItemPedido

c = Cliente(0,'','')

daoCliente = DaoCliente(c)
cliente = daoCliente.consultarUm(2)

ped = Pedido('2025/07/25',cliente)

daoPedido = DaoPedido(ped)

p = Produto(0,'',0.0,0)
daoProduto = DaoProduto(p)

p1 = daoProduto.consultarUm(1)
item1 = ItemPedido(p1, 2)
daoPedido.adicionaItem(item1)

p2 = daoProduto.consultarUm(2)
item2 = ItemPedido(p2, 3)
daoPedido.adicionaItem(item2)

daoPedido.finalizarPedido()