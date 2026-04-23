# importa a função 'conectar' do arquivo db.py
# essa função é responsável por abrir a conexão com o MySQL
from db import conectar


# chama a função conectar() e guarda a conexão na variável 'conexao'
# aqui você está abrindo uma conexão com o servidor do MySQL
conexao = conectar()


# cria um "cursor"
# o cursor é o objeto que permite executar comandos SQL
cursor = conexao.cursor()


# executa um comando SQL:
# cria um banco chamado 'meubanco' se ele ainda não existir
cursor.execute("CREATE DATABASE IF NOT EXISTS meubanco")

# seleciona o banco que você acabou de criar
# a partir daqui, todas as operações vão acontecer dentro desse banco
conexao.database = "meubanco"

def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL
    )
    """)
    print("Tabela 'usuarios' criada com sucesso!") 

def inserir_usuarios(cursor, conexao, nome, idade):
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (%s, %s)",
    (nome, idade))
    conexao.commit()

# inserir_usuarios(cursor, conexao, "Lucas", 60)

def atualizar_idade(cursor, conexao, nome, nova_idade):
    cursor.execute("UPDATE usuarios SET idade = %s WHERE nome = %s",
    (nova_idade, nome))
    conexao.commit()

def deletar_usuario(cursor, conexao, id):
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    conexao.commit()

# deletar_usuario(cursor, conexao, 4)
# deletar_usuario(cursor, conexao, 5)
deletar_usuario(cursor, conexao, 8)



# salva (confirma) a operação no banco
# algumas operações precisam disso para serem efetivadas
conexao.commit()

def listar_usuarios(cursor):
    cursor.execute("SELECT * FROM usuarios WHERE idade > 30")
    dados = cursor.fetchall()
    for linha in dados:
        print(linha)

listar_usuarios(cursor)

# só um print pra você ver que deu certo
print("Banco pronto!")

# fecha o cursor (boa prática)
cursor.close()

# fecha a conexão com o banco (muito importante)
conexao.close()