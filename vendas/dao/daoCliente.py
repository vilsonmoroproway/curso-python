import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="bd_vendas"
)

class DaoCliente:
    def __init__(self, cliente):
        self.cliente = cliente
        
    def salvar(self):
        mycursor = mydb.cursor()
        
        sql = "insert into tb_clientes(nome, email)values(%s,%s)"
        val = (self.cliente.getNome(),self.cliente.getEmail())

        mycursor.execute(sql, val)
        mydb.commit()
    
    def alterar(self, alterado):
        mycursor = mydb.cursor()
        
        sql = 'update tb_clientes set nome = %s, email = %s where id = %s'
        val = (alterado.getNome(),alterado.getEmail(), alterado.getId())

        mycursor.execute(sql, val)
        mydb.commit()
    
    def consultar(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM tb_clientes")
        return mycursor.fetchall()

    def deletar(self,id):
        mycursor = mydb.cursor()
        sql = 'delete from tb_clientes where id = %s'
        mycursor.execute(sql,[id])
        mydb.commit()

    def consultarUm(self, id):
        cursor = mydb.cursor()
        cursor.execute(f"select * from tb_clientes where id = {id}")
        x = cursor.fetchone()
       
        self.cliente.setId(x[0])
        self.cliente.setNome(x[1])
        self.cliente.setEmail(x[2])
        
        return self.cliente