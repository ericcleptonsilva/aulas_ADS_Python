import sqlite3 as conn
from sqlite3.dbapi2 import Cursor, DatabaseError

try:
    #abertura de conxeão e aquisição de cursor
    conexao = conn.connect('automoveis.db')
    cursor = conexao.cursor()

    # execurta comandos SQL - select, create
    sql_query = ''' create table marca (
                    id integer not null,
                    nome text not null,
                    sigla character2(2) not null,
                    primary key(id)
                
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
