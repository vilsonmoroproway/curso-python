class ContaBancaria:
    def __init__(self, valor):
        self.saldo = valor

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if(valor > self.saldo):
            raise ValueError('Saldo insuficiente')    
        self.saldo -= valor