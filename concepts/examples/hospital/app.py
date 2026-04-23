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

# criar_tabela_pacientes(cursor)

def criar_especidades_pacientes(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS especialidades (
        cidade VARCHAR(50) NOT NULL,
        year INT,
        temperatura FLOAT,
        pacientes_id INT,
        CONSTRAINT check_year CHECK (year >= 1900 AND year <= 2100),
        CONSTRAINT check_temperatura CHECK (temperatura >= 0 AND temperatura <= 50),
        PRIMARY KEY (cidade, year),
        FOREIGN KEY (pacientes_id) REFERENCES pacientes(id)
    )""")
    conexao.commit()
    print("Tabela 'especialidades' criada com sucesso!")

criar_especidades_pacientes(cursor)

conexao.commit()

cursor.close()
conexao.close()