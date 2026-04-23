from db import conectar

conexao = conectar()

cursor = conexao.cursor()

#? Banco de dados para um hospital
def criar_banco(cursor): 
    cursor.execute("CREATE DATABASE IF NOT EXISTS hospital")
    print("banco hospital criado com sucesso.")

# criar_banco(cursor)

conexao.database = "hospital"




def criar_tabela_pacientes(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE
    )""")
    conexao.commit()
    print("Tabela 'pacientes' criada com sucesso!")


criar_tabela_pacientes(cursor)

conexao.commit()

cursor.close()
conexao.close()