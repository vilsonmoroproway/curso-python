from services.produto_service import salvar
from services.pedido_service import menu_pedidos

def menu_main():
    print('1-Produtos')
    print('2-Clientes')
    print('3-Pedidos')

def menu_produtos():
    while True:
        print('N - Novo')
        print('D - deletar')
        print('C - consultar')
        print('S - Sair')
        opcao = input('Digite opção: ')
        match opcao.upper():
            case 'N': salvar()
            case 'S': break
            case _:
                print('opção inválida')
                    


while True:
    menu_main()

    opcao = int(input('Digite opção: '))
    match opcao:
        case 1: menu_produtos()
        case 3: menu_pedidos()
        case _:
            print('opção inválida')
            break