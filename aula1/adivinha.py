import random

numero_secreto = random.randint(1, 100)

tentativas = 0

while True:
    chute = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1

    if chute > numero_secreto:
        print("Muito alto!")
    elif chute < numero_secreto:
        print("Muito baixo!")
    else:
        print("Parabéns! Você acertou!")
        print("Tentativas:", tentativas)
        break