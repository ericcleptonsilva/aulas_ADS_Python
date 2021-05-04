import sqlite3 as conn
from model import *

try:
    #abertura de conxeão e aquisição de cursor
    conexao = conn.connect('automoveis.db')
    cursor = conexao.cursor()

    #criação de um objeto do import model
    #pessoa = Pessoas(1199354, 'Clepton', '1984-01-09', True)
    #veiculos = Veiculos()

    # Definição de parametros com dicionário
    sqlInsert01 = ''' insert into marca (nome, sigla) values (:nome, :sigla) '''

    '''marca01 = Marca('Fiat', 'F1')
    marca01.id = cursor.lastrowid
    cursor.execute(sqlInsert01, (marca01.nome, marca01.sliga))

    marca02 = Marca('Ford', 'F2')
    marca02.id = cursor.lastrowid
    cursor.execute(sqlInsert01, (marca02.nome, marca02.sliga))
'''
    sqlInsert02 = ''' insert into veiculo (placa, ano, cor, motor, proprietario, marca) 
                                  values (:placa, :ano, :cor, :motor, :proprietario, :marca) '''

    veiculos01 = Veiculos('AAA0001', 2008, 'prata', 1.0, 123456, 1)
    veiculos02 = Veiculos('BBB0002', 2018, 'preto', 2.0, 654321, 0)
    veiculos03 = Veiculos('CCC0003', 2010, 'vermelho', 1.4, 1199354, 1)
    veiculos04 = Veiculos('DDD0004', 2011, 'azul', 1.1, 123456, 1)

    cursor.execute(sqlInsert02, vars(veiculos01))
    cursor.execute(sqlInsert02, vars(veiculos02))
    cursor.execute(sqlInsert02, vars(veiculos03))
    cursor.execute(sqlInsert02, vars(veiculos04))

    # efetivar o sql query
    conexao.commit()

except conn.DatabaseError as err:
    print("Erro no bando de dados!", err)
finally:
    # fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()

print("Programa finalizado!")
