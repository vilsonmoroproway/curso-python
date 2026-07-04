class Produto:
    def __init__(self, descricao, preco, estoque):
        #self.__descricao = descricao
        self.set__descricao(descricao)
        #self.__preco = preco
        self.set__preco(preco)
        #self.estoque = estoque
        self.set__estoque(estoque)
    
    def get__descricao(self):
        return self.__descricao
    
    def set__descricao(self, descricao):
        if(len(descricao) < 3):
            print('A descrição do produto deve ter no minimo 3 caracteres')
        else:
            self.__descricao = descricao
    
    def get__preco(self):
        return self.__preco
    
    def set__preco(self, preco):
        if(preco < 0):
            print('O preço não pode ser negativo')
        else:
            self.__preco = preco

    def get__estoque(self):
        return self.__estoque
    
    def set__estoque(self, estoque):
        if(estoque <= 0):
            print('O estoque deve ser maior que zero')
        else:
            self.__estoque = estoque



