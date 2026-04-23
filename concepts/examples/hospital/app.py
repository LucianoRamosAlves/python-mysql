from db import conectar

conexao = conectar()

cursor = conexao.cursor()

# Banco de dados para um hospital
def criar_banco(cursor): 
    cursor.execute("CREATE DATABASE IF NOT EXISTS hospital")
    print("banco hospital criado com sucesso.")

# seleciona o banco que você acabou de criar
conexao.database = "hospital"

# criar tabela de pacientes
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

# validações para os campos de pacientes
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
        raise ValueError("Nome não pode ser um nome reservado.")
    elif nome == "":
        raise ValueError("Nome não pode ser vazio.")
    
def validar_idade(idade):
    if idade < 0 or idade > 120:
        raise ValueError("Idade deve estar entre 0 e 120 anos.")
    
def validar_email(email):
    if not email or len(email) > 100:
        raise ValueError("Email deve ser preenchido e ter no máximo 100 caracteres.")
    elif "@" not in email or "." not in email:
        raise ValueError("Email deve conter '@' e '.'.")
    elif email[0].isspace() or email[-1].isspace():
        raise ValueError("Email não deve começar ou terminar com espaço.")
    

# campo inserção de pacientes
def inserir_paciente(cursor, conexao, nome, idade, email):
    try:
        validar_nome(nome)
        validar_idade(idade)
        validar_email(email)
        cursor.execute("INSERT INTO pacientes (nome, idade, email) VALUES (%s, %s, %s)",
        (nome, idade, email))
        print(f"Paciente '{nome}' inserido com sucesso!")
        conexao.commit()
    except ValueError as e:
        print(f"Erro ao inserir paciente: {e}")

#inserir_paciente(cursor, conexao, "Maria Silva", 30, "maria.silva@example.com")
#inserir_paciente(cursor, conexao, "João Souza", 45, "joao.souza@example.com")
#inserir_paciente(cursor, conexao, "admin", 28, "ana.oliveira@example.com")


def listar_pacientes(cursor):
    cursor.execute("SELECT * FROM pacientes")
    dados = cursor.fetchall()
    for linha in dados:
        print(linha)

#listar_pacientes(cursor)


# validações para os campos de especialidades
def validar_temperatura(temperatura):
    if temperatura < 0 or temperatura > 50:
        raise ValueError("Temperatura deve estar entre 0 e 50 graus Celsius.")
    
def validar_year(year):
    if year < 1900 or year > 2100:
        raise ValueError("Year deve estar entre 1900 e 2100.")
    
def validar_cidade(cidade):
    if not cidade or len(cidade) > 50:
        raise ValueError("Cidade deve ser preenchida e ter no máximo 50 caracteres.")
    elif not cidade.replace(" ", "").isalpha():
        raise ValueError("Cidade deve conter apenas letras e espaços.")
    elif cidade[0].isspace() or cidade[-1].isspace():
        raise ValueError("Cidade não deve começar ou terminar com espaço.")
    elif "  " in cidade:
        raise ValueError("Cidade não deve conter múltiplos espaços consecutivos.")
    
 
# campo inserção de especialidades
def inserir_especialidade(cursor, conexao, cidade, year, temperatura, pacientes_id):
    try:
        validar_cidade(cidade)
        validar_year(year)
        validar_temperatura(temperatura)
        cursor.execute("INSERT INTO especialidades (cidade, year, temperatura, pacientes_id) VALUES (%s, %s, %s, %s)",
        (cidade, year, temperatura, pacientes_id))
        print(f"Especialidade para paciente ID {pacientes_id} inserida com sucesso!")
        conexao.commit()
    except ValueError as e:
        print(f"Erro ao inserir especialidade: {e}")

#inserir_especialidade(cursor, conexao, "São Paulo", 2023, 25.5, 1)
inserir_especialidade(cursor, conexao, "Rio de Janeiro", 2023, 30.0, 2)

conexao.commit()

cursor.close()
conexao.close()