class Carro:
    __placa = ''
    def __init__(self, placa, cor, modelo):
        #self.__placa = ''
        self.setPlaca(placa)
        self.cor = cor
        self.modelo = modelo

    def acelerar(self):
        print('acelerando')

    def setPlaca(self,placa):
        if(len(placa) != 8):
            print('A placa deve ter 8 caracteres')
            return
        self.__placa = placa

    def getPlaca(self):
        return self.__placa



class ContaBancaria:
    __titular = ''
    __agencia = ''
    __numero = ''
    __saldo = 0.0

    def __init__(self, titular, agencia, numero):
        self.setTitular(titular)
        self.setAgencia(agencia)
        self.setNumero(numero)
    
    def setTitular(self, titular):
        if titular == '':
            print('Informe o nome do titular')
            return
        self.__titular = titular
    
    def setAgencia(self, agencia):
        if len(agencia) < 6:
            print('Informe a agência (6 digitos)')
            return
        self.__agencia = agencia

    def setNumero(self, numero):
        if numero == '':
            print('Informe o numero da conta')
            return
        self.__numero = numero

    def setSaldo(self, valor):
        self.__saldo = valor

    def getSaldo(self):
        return self.__saldo

    def info(self):
        print(f'Titular:{self.__titular} Agência:{self.__agencia} Conta:{self.__numero} Saldo:{self.__saldo}')
    

class OperacaoBancaria:

    def sacar(self, conta, valor):
        if(valor > conta.getSaldo()):
            print('saldo insuficiente')
        else:
            conta.setSaldo(conta.getSaldo() - valor)
        
    def depositar(self, conta, valor):
        conta.setSaldo(conta.getSaldo() + valor)
    
    def transferir(self, origem, destino, valor):
        self.sacar(origem,valor)
        self.depositar(destino, valor)