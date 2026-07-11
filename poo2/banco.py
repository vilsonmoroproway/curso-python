from carro import (ContaBancaria, OperacaoBancaria) 

c1 = ContaBancaria('Ana','0101-0','00001234')
c1.info()

operacao = OperacaoBancaria()
operacao.depositar(c1,100)
c1.info()
operacao.sacar(c1,20)
c1.info()

c2 = ContaBancaria('Maria','0101-0','00001235')
c1.info()
c2.info()

operacao.transferir(c1, c2, 30)
c1.info()
c2.info()
