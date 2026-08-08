from daos.daoCliente import DaoCliente
from daos.daoProduto import DaoProduto
from daos.daoPedido import DaoPedido
from modelos.pedido import Pedido
from modelos.itenPedido import ItemPedido
from datetime import date

def menu_pedidos():
    while True:
        print('N - Novo')
        print('D - deletar')
        print('C - consultar')
        print('S - Sair')
        opcao = input('Digite opção: ')
        match opcao.upper():
            case 'N': novo_pedido()
            case 'S': break
            case _:
                print('opção inválida')



def novo_pedido():
    codCliente = int(input('Informe código do cliente: '))
    daoCliente = DaoCliente()
    cliente = daoCliente.consultarUm(codCliente)

    pedido = Pedido(date.day(), cliente)

    while True:
       codProduto = int(input('Informe código do produto')) 
       produto = DaoProduto.consultarUm(codProduto)
       quantidade = int(input('Informe código do produto'))
       item = ItemPedido(produto, quantidade)
       DaoPedido.adicionaItem(item)

       continuar = input('Adicionar novo item? S-N')
       if continuar.upper() == 'N':
           DaoPedido.finalizarPedido()
           break
