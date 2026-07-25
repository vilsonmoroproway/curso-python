class Cliente:
    def __init__(self, id, nome, email):
        self.setId(id)
        self.nome = nome
        self.email = email
    
    def setId(self,id):
        self.id = id
    
    def getId(self):
        return self.id
    
    def setNome(self,nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setEmail(self,email):
        self.email = email
    
    def getEmail(self):
        return self.email

    def display(self):
        print(f"{self.id} {self.nome} {self.email}")