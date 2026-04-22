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


# salva (confirma) a operação no banco
# algumas operações precisam disso para serem efetivadas
conexao.commit()


# seleciona o banco que você acabou de criar
# a partir daqui, todas as operações vão acontecer dentro desse banco
conexao.database = "meubanco"


# só um print pra você ver que deu certo
print("Banco pronto!")


# fecha o cursor (boa prática)
cursor.close()


# fecha a conexão com o banco (muito importante)
conexao.close()