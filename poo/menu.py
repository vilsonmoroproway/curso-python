import produto as p

produtos = []

def salvar():
    descricao = input('Informe descrição: ')
    preco = float(input('Informe preço: '))
    estoque = int(input('Informe estoque: '))

    p1 = p.Produto(descricao, preco, estoque)
    produtos.append(p1)

def consultaProduto(descricao):
    for x in produtos:
        if (descricao == x.get__descricao()):
            return x

while True:
    print('Digite 1 para salvar')
    print('Digite 2 para excluir')
    print('Digite 3 para alterar')
    print('Digite 4 para consultar todos')
    print('Digite 5 para consultar pela descrição')
    print('Digite 0 para sair')
    opcao = int(input('Digite opção: '))
    match opcao:
        case 1:
            salvar()
        case 2:
            x = consultaProduto(input('informe descrição que deseja excluir: '))
            produtos.remove(x)
        case 3:
            produtoAlterar = input('informe produto que deseja alterar: ')
            x = consultaProduto(produtoAlterar)
            print(f'Preço atual: {x.get__preco()} Estoque Atual: {x.get__estoque()}')
            x.set__preco(float(input('informe novo preço: ')))
            x.set__estoque(int(input('informe nova quantidade: ')))
                   
        case 4:
            for x in produtos:
                x.display()
        case 5:
            x = consultaProduto(input('informe descrição que deseja pesquisar: '))    
            x.display()        
        case 0:
            #grava em arquivo
            break
        case _:
            print('opção inválida')
        


