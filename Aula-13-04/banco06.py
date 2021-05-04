import sqlite3 as conn
from sqlite3.dbapi2 import Cursor, DatabaseError

try:
    #abertura de conxeão e aquisição de cursor
    conexao = conn.connect('automoveis.db')
    cursor = conexao.cursor()

    # execurta comandos SQL - insert table pessoa
    sqlInsert = ''' insert into pessoa (cpf, nome, nascimento, oculos)
                        values (123456, "Benedito", '2021-12-30', 1)
                    '''

    cursor.execute(sqlInsert)
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
