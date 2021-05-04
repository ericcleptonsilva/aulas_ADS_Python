import sqlite3 as conn
from sqlite3.dbapi2 import version
from model import *

#Abertura de conexão
conexao = conn.connect('automoveis.db')
cursor = conexao.cursor()
sql_query = ''' SELECT Veiculo.placa, Veiculo.ano, veiculo.cor, Veiculo.motor,
                        Veiculo.proprietario, Marca.nome FROM Veiculo
                        JOIN Marca ON Marca.id = Veiculo.marca;'''

cursor.execute(sql_query)

registro = cursor.fetchall()
for registros in registro:
    veiculos = Veiculos(*registros)
    print(f'Placa:{veiculos.placa} - Marca: {veiculos.marca}')


conexao.commit()

cursor.close()
conexao.close()
print("Dados Localizados")
