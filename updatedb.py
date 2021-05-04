import sqlite3 as conn
from model import *

#Abertura de conexão
conexao = conn.connect('automoveis.db')
conexao.execute('PRAGMA foreign_keys=on')
cursor = conexao.cursor()

#sql_query = ''' update pessoa set oculos = 1;'''
#cursor.execute(sql_query)

#sql_query1 = ''' update pessoa set oculos = ? where cpf = 123456; '''
#cursor.execute(sql_query1, (False,))

sql_query3 = ''' update pessoa set oculos = :UsaOculos where cpf = :cpf; '''
cursor.execute(sql_query3, {'UsaOculos': True, 'cpf': 1199354})

conexao.commit()
cursor.close()
conexao.close()
print("Finalizado!")
