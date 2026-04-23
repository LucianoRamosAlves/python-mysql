from db import conectar

conexao = conectar()

cursor = conexao.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS hospital")
print("banco hospital criado com sucesso.")

conexao.commit()

cursor.close()
conexao.close()