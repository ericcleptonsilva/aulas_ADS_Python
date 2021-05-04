import sqlite3 as conn
from sqlite3.dbapi2 import Cursor, DatabaseError
from model import *

try:
    #abertura de conxeão e aquisição de cursor
    conexao = conn.connect('automoveis.db')
    cursor = conexao.cursor()

    #criação de um objeto do tipo pessoa
    pessoa = Pessoas(1199354, 'Clepton', '1984-01-09', True)

    # Definição de parametros com dicionário
    sqlInsert = ''' insert into pessoa (cpf, nome, nascimento, oculos)
                        values (:cpf,:nome,:dataNascimento,:UsaOculos);
                    '''

    cursor.execute(sqlInsert, vars(pessoa))
    print("Exemplo:")
    print(vars(pessoa))
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
