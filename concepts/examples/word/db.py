from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

def conectar():
    return mysql.connector.connect(
        host= os.getenv("DB_HOST"),
        user= os.getenv("DB_USER"),
        password= os.getenv("DB_PASSWORD"),
    )