print("operadores de comparação")

x = 10
y = 20

print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)


idade = 11

if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")


# até 10 anos criança
# até 20 adolescente
# até 60 adulto
# acima de 60 idoso

if idade < 10:
    print("Criança")
elif idade < 20 :
    print("adolescente")
elif idade < 60:
    print("adulto")
else:
    print("idoso")

