import mysql.connector

# Definir a conexão com o banco de dados

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="B34tB0x@",
    )
