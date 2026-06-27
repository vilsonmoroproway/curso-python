frutas = []
with open('frutas.txt','r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        frutas.append(linha.strip())

while True:
    print('Digite 1 para salvar')
    print('Digite 2 para excluir')
    print('Digite 3 para sair')
    opcao = int(input('Digite opção: '))
    match opcao:
        case 1:
            novaFruta = input('Digite nova fruta: ')
            frutas.append(novaFruta)
        case 2:
            frutaRemover = input('Digite nome da fruta que deseja remover: ')
            frutas.remove(frutaRemover)
        case 3:
            with open('frutas.txt','w', encoding='utf-8') as f:
                for fruta in frutas:
                    f.write(fruta + '\n')
            break
        