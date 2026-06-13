valor = float(input("Digite o valor da compra: "))

if valor > 500:
    desconto = valor * 0.10
elif valor > 200:
    desconto = valor * 0.05
else:
    desconto = 0

valor_final = valor - desconto

print(f"Valor final: R$ {valor_final:.2f}")
print("valor final: R$ ", valor_final)