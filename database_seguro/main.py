from database.conexao import Conexao

print('trabalhando com .env')

try:

    conexao = Conexao.conectar()

    print("Conectado ao MySQL!")

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tb_produtos")

    produtos = cursor.fetchall()

    for produto in produtos:
        print(produto)

except Exception as e:

    print(f"Erro ao conectar ao banco: {e}")

finally:

    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada.")