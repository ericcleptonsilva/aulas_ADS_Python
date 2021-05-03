import sqlite3 as conn
from sqlite3.dbapi2 import Cursor, DatabaseError

try:
    #abertura de conxeão e aquisição de cursor
    conexao = conn.connect('automoveis.db')
    cursor = conexao.cursor()

    # execurta comandos SQL - select, create
    sql_query = ''' create table pessoa (
                    cpf integer not null,
                    nome text not null,
                    nascimento date not null,
                    oculos boolean not null,
                    primary key(cpf)
                
                    );'''
    cursor.execute(sql_query)
    # efetivar o sql)query
    conexao.commit()

except conn.DatabaseError as err:
    print("Erro no bando de dados!", err)
finally:
    # fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
print("Programa finalizado!")