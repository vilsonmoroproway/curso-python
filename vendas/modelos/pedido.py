class Pedido:
    def __init__(self, data, cliente):
        self.id = 0
        self.data = data
        self.cliente = cliente
    
    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id