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

# criar_especidades_pacientes(cursor)

def validar_nome(nome):
    if not nome or len(nome) > 100:
        raise ValueError("Nome deve ser preenchido e ter no máximo 100 caracteres.")
    elif not nome.replace(" ", "").isalpha():
        raise ValueError("Nome deve conter apenas letras e espaços.")
    elif nome[0].isspace() or nome[-1].isspace():
        raise ValueError("Nome não deve começar ou terminar com espaço.")
    elif "  " in nome:
        raise ValueError("Nome não deve conter múltiplos espaços consecutivos.")
    elif nome.lower() in ["admin", "root", "null"]:
        print(f"Nome '{nome}' é um nome reservado. Por favor, escolha outro nome.")
        raise ValueError("Nome não pode ser um nome reservado.")
    elif nome == "":
        raise ValueError("Nome não pode ser vazio.")
    



def inserir_paciente(cursor, conexao, nome, idade, email):
    try:
        validar_nome(nome)
        cursor.execute("INSERT INTO pacientes (nome, idade, email) VALUES (%s, %s, %s)",
        (nome, idade, email))
        print(f"Paciente '{nome}' inserido com sucesso!")
        conexao.commit()
    except ValueError as e:
        print(f"Erro ao inserir paciente: {e}")

#inserir_paciente(cursor, conexao, "Maria Silva", 30, "maria.silva@example.com")
#inserir_paciente(cursor, conexao, "João Souza", 45, "joao.souza@example.com")
inserir_paciente(cursor, conexao, "admin", 28, "ana.oliveira@example.com")


conexao.commit()

cursor.close()
conexao.close()