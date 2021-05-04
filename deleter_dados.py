import sqlite3 as conn
from model import *

#Abertura de conexão
conexao = conn.connect('automoveis.db')
conexao.execute('PRAGMA foreign_keys=on')
cursor = conexao.cursor()

sql_query = ''' delete from veiculo where proprietario = 123456; '''
cursor.execute(sql_query)

sql_query1 = ''' delete from pessoa where cpf = 123456; '''
cursor.execute(sql_query1)

conexao.commit()

cursor.close()
conexao.close()
print("Dados deletado com sucesso!")
