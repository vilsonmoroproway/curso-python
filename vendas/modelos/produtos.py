class Produto:
    def __init__(self, id, descricao, preco, estoque):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
    
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getDescricao(self):
        return self.descricao    
    
    def setDescricao(self, descricao):
        self.descricao = descricao
    
    def getDescricao(self):
        return self.descricao
    
    def setPreco(self, preco):
        self.preco = preco
    
    def getPreco(self):
        return self.preco

    def setEstoque(self, estoque):
        self.estoque = estoque
    
    def getEstoque(self):
        return self.estoque
    
    def display(self):
        print(f"{self.id} {self.descricao} {self.preco} {self.estoque}")