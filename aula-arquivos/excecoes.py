try:
    a = 10
    b = 2
    c = a / b
except:
    print('não é possivel dividir por zero')
finally:
    print('calculo realizado')

print('ola')


try:
    with open('excecao.txt','x') as f:
        f.write('ola mundo')
except FileExistsError:
    print('Arquivo já existe')


def dividir():
    a = 10
    b = 0

    if b == 0:
       raise Exception('Erro ao dividir por zero')

    return a / b


try:
    dividir()
except Exception as e:
    print(e)


try:
    x = int(input('Digite sua idade: '))
    if type(x) is int:
        print(f'Sua idade é {x}')
    
except ValueError:
    print('Digite numeros inteiros')