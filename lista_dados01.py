import sqlite3 as conn
from model import *

#Abertura de conexão
conexao = conn.connect('automoveis.db')
cursor = conexao.cursor()
sql_query = ''' select * from pessoa where oculos = :UsarOculos;'''

cursor.execute(sql_query, {'UsarOculos': True})
registro = cursor.fetchall()
print('Tipo de retorno pelo fetchal:', type(registro))

for registros in registro:
    pessoa = Pessoas(*registros)
    print('CPF:', pessoa.cpf, '\nTipo', type(pessoa.cpf))
    print('Nome:', pessoa.nome, '\nTipo', type(pessoa.nome))
    print('Data Nasc:', pessoa.dataNascimento,
          '\nTipo', type(pessoa.dataNascimento))
conexao.commit()

cursor.close()
conexao.close()
print("Dados Localizados")
