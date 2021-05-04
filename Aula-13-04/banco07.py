import sqlite3 as conn
from sqlite3.dbapi2 import Cursor, DatabaseError
from model import *
try:
    #abertura de conxeão e aquisição de cursor
    conexao = conn.connect('automoveis.db')
    cursor = conexao.cursor()

    #criação de um objeto do tipo pessoa
    pessoa = Pessoas(654321, 'Eric', '1984-01-08', False)

    # Definição de parametros
    sqlInsert = ''' insert into pessoa (cpf, nome, nascimento, oculos)
                        values (?,?,?,?);
                    '''

    cursor.execute(sqlInsert,
                   (pessoa.cpf,
                    pessoa.nome,
                    pessoa.dataNascimento,
                    pessoa.UsaOculos))
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
