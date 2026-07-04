class Carro:
    def __init__(self,placa, marca, modelo):
        self.__placa = placa
        self.marca = marca
        self.modelo = modelo

    def display(self):
        print(f'Placa: {self.__placa} Marca: {self.marca} Modelo: {self.modelo}')

    def get__placa(self):
        return self.__placa

    def set__placa(self, placa):
        if len(placa) != 8:
            print('placa inválida')
        else:
            self.__placa = placa

fusca = Carro('abc-1234','wolkswaggen','fusca 1300l')

print(fusca.display())
fusca.set__placa('def-123')
print(fusca.get__placa())