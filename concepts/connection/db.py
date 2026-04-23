from dotenv import load_dotenv  
import os
import mysql.connector

load_dotenv()

# Definir a conexão com o banco de dados
def conectar():
    return mysql.connector.connect(
        host= os.getenv("DB_HOST"),
        user= os.getenv("DB_USER"),
        password= os.getenv("DB_PASSWORD"),
    )
