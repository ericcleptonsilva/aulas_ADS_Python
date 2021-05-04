import sqlite3 as conn
from model import *

#Abertura de conexão
conexao = conn.connect('automoveis.db')
conexao.execute('PRAGMA foreign_keys=on')
cursor = conexao.cursor()

sql_query = ''' insert into veiculo values(:placa, :ano,:cor,:motor,:proprietario,:marca);'''
veiculos01 = Veiculos('AAA0001', 2008, 'prata', 1.0, 123456, 1)
veiculos02 = Veiculos('BBB0002', 2018, 'preto', 2.0, 654321, 2)
veiculos03 = Veiculos('CCC0003', 2010, 'vermelho', 1.4, 1199354, 1)
veiculos04 = Veiculos('DDD0004', 2011, 'azul', 1.1, 123456, 1)

cursor.execute(sql_query, vars(veiculos01))
cursor.execute(sql_query, vars(veiculos02))
cursor.execute(sql_query, vars(veiculos03))
cursor.execute(sql_query, vars(veiculos04))

#efetivar o sql query
conexao.commit()
#fechamento das conexões
cursor.close()
conexao.close()
print("finalizado!")
