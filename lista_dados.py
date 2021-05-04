import sqlite3 as conn
from model import *

#Abertura de conexão
conexao = conn.connect('automoveis.db')
cursor = conexao.cursor()

sql_query = ''' select * from pessoa;'''

cursor.execute(sql_query)
registro = cursor.fetchall()
print('Tipo de retorno pelo fetchal:', type(registro))

for registros in registro:
    print('Tipo: ', type(registro), '- Conteúdo: ', registros)
conexao.commit()

cursor.close()
conexao.close()
print("Dados Localizados")
