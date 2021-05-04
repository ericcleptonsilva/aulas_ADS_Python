import sqlite3 as conn
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
    print(f'\nPlaca:{veiculos.placa}\nAno de Fabricação: {veiculos.ano}\nCor: {veiculos.cor}\nMotor:{veiculos.motor}\nMarca: {veiculos.marca}\nProprietário: {veiculos.proprietario}\n')


conexao.commit()

cursor.close()
conexao.close()
print("Dados Localizados")
