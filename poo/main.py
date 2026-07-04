import produto as p

produtos = []

p1 = p.Produto('milho',1.5,10)
p2 = p.Produto('Feijão',2.5,10)
p3 = p.Produto('Trigo',3.5,10)
p4 = p.Produto('Farinha',6.5,10)

produtos.append(p1)
produtos.append(p2)
produtos.append(p3)
produtos.append(p4)

for p in produtos:
    print(p.get__descricao())
