frutas = ['maça','uva']

with open('frutas.txt','w', encoding='utf-8') as f:
    for fruta in frutas:
        f.write(fruta + '\n')


cesta = []
with open('frutas.txt','r') as arquivo:
    for linha in arquivo:
        cesta.append(linha.strip())

print(cesta)