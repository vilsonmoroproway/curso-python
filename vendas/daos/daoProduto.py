import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="bd_vendas"
)

class DaoProduto:
    def __init__(self, produto):
        self.produto = produto
        
    def salvar(self):
        mycursor = mydb.cursor()
        
        sql = "insert into tb_produtos(descricao, preco, estoque)values(%s, %s, %s)"
        val = (self.produto.getDescricao(),self.produto.getPreco(), self.produto.getEstoque())

        mycursor.execute(sql, val)
        mydb.commit()
    
    def alterar(self, alterado):
        mycursor = mydb.cursor()
        
        sql = 'update tb_produtos set descricao = %s, preco = %s, estoque = %s where id = %s'
        val = (alterado.getDescricao(),alterado.getPreco(), alterado.getEstoque(), alterado.getId())

        mycursor.execute(sql, val)
        mydb.commit()
    
    def consultar(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM tb_produtos")
        return mycursor.fetchall()

    def deletar(self,id):
        mycursor = mydb.cursor()
        sql = 'delete from tb_produtos where id = %s'
        mycursor.execute(sql,[id])
        mydb.commit()

    def consultarUm(self, id):
        cursor = mydb.cursor()
        cursor.execute(f"select * from tb_produtos where id = {id}")
        x = cursor.fetchone()
       
        self.produto.setId(x[0])
        self.produto.setDescricao(x[1])
        self.produto.setPreco(x[2])
        self.produto.setEstoque(x[3])
        
        return self.produto