from db import conectar #! 1 primeiro passo. Importar a função conectar() do módulo db.py para estabelecer uma conexão com o banco de dados MySQL.

conexao = conectar() #! 2 segundo passo. Chamar a função conectar() para criar uma conexão com o servidor MySQL e armazenar essa conexão na variável conexao.
cursor = conexao.cursor() #! 3 terceiro passo. Criar um cursor a partir da conexão. O cursor é um objeto que permite executar comandos SQL e interagir com o banco de dados.

def criar_banco(cursor): #! 6 sexto passo. Definir uma função criar_banco() que recebe o cursor como argumento e executa um comando SQL para criar um banco de dados chamado "word" se ele ainda não existir. Após criar o banco, a função imprime uma mensagem de sucesso.
    cursor.execute("CREATE DATABASE IF NOT EXISTS word") #! 7 sétimo passo. Executar o comando SQL para criar o banco de dados "word" usando o método execute() do cursor. O comando "CREATE DATABASE IF NOT EXISTS" garante que o banco só será criado se ele ainda não existir, evitando erros caso já exista um banco com esse nome.
    conexao.commit() #! 8.1 passo. Confirmar a operação de criação do banco de dados usando conexao.commit(). Isso é necessário para garantir que as alterações sejam salvas no servidor MySQL.
    print("banco word criado com sucesso.")

# criar_banco(cursor) #! 8 oitavo passo. Chamar a função criar_banco() passando o cursor como argumento para criar o banco de dados "word". Isso executará o comando SQL para criar o banco e imprimirá a mensagem de sucesso.
conexao.database = "word" #! 9 nono passo. Selecionar o banco de dados "word" para que as próximas operações sejam realizadas dentro desse banco. Isso é feito atribuindo o nome do banco à propriedade database da conexão.


def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS continentes (
        continente_id INT AUTO_INCREMENT PRIMARY KEY,
        continente_nome VARCHAR(20) NOT NULL,
        populacao BIGINT NOT NULL
    )
    """)
    conexao.commit()
    print("Tabela 'continentes' criada com sucesso!")

# criar_tabela()

def inserir_continente(cursor, conexao, nome, populacao):
    cursor.execute("INSERT INTO continentes (continente_nome, populacao) VALUES (%s, %s)",
    (nome, populacao))
    conexao.commit()
    print(f"Continente '{nome}' inserido com sucesso!")

#inserir_continente(cursor, conexao, "África", 1340598147)
#inserir_continente(cursor, conexao, "América do Norte", 592072212)
#inserir_continente(cursor, conexao, "América do Sul", 430759766)
#inserir_continente(cursor, conexao, "Ásia", 4641054787)
#inserir_continente(cursor, conexao, "Europa", 747636026)
#inserir_continente(cursor, conexao, "Oceania", 43111704)












cursor.close() #! 4 quarto passo. Fechar o cursor após criar o banco de dados, pois ele não é mais necessário para as próximas operações.
conexao.close() #! 5 quinto passo. Fechar a conexão com o banco de dados para liberar recursos e evitar conexões desnecessárias.