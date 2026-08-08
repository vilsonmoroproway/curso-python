from daos.daoProduto import DaoProduto
from modelos.produto import Produto

def salvar():
    descricao = input('Informe descrição: ')
    preco = float(input('Informe preço: '))
    estoque = int(input('Informe estoque: '))
    p = Produto(0,descricao,preco,estoque)
    daoProduto = DaoProduto(p)
    daoProduto.salvar()

