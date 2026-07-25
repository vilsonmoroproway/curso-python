import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="bd_vendas"
)

class DaoPedido:
    def __init__(self, pedido):
        self.pedido = pedido
        self.carrinho = []
    
    def adicionaItem(self,item):
        print(item.produto.display())
        self.carrinho.append(item)

    def removeItem(self,item):
        self.carrinho.remove(item)
    
    def finalizarPedido(self):
        # gravar pedido
        mycursor = mydb.cursor()
        
        sql = "insert into tb_pedidos(data, tb_clientes_id)values(%s,%s)"
        val = (self.pedido.data,self.pedido.cliente.getId())
        #print(self.pedido.data, self.pedido.cliente.display())
        mycursor.execute(sql, val)
        mydb.commit()

        self.pedido.id = mycursor.lastrowid

        #percorrer lista e salvar os itens
        for x in self.carrinho:
            mycursor = mydb.cursor()
            sql = 'insert into tb_carrinhos(tb_pedidos_id, tb_produtos_id, quantidade)values(%s,%s,%s)'
            val = (self.pedido.id,x.produto.getId(), x.quantidade)
            mycursor.execute(sql, val)
            mydb.commit()
           