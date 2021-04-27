import sqlite3 as conn
from sqlite3.dbapi2 import Cursor

try:

    # abertura de conexao e aquisição
    conexao = conn.connect('meu_banco.db')
    curso = conexao.cursor()
    # execução de criação de tabela
    sql_comando = ''' create table cadastro(
                      codigo integer not null,
                      nome text not null,
                      idade integer not null,
                      primary key(codigo)
                      );'''
    curso.execute(sql_comando)
    # inserindo dados na tabela
    sql_comando = ''' 
                    insert into cadastro(codigo, nome, idade)
                    values
                    (019, 'Eric Clepton', 37);'''
    curso.execute(sql_comando)
    sql_comando = ''' 
                    insert into cadastro(codigo, nome, idade)
                    values
                    (017, 'Ricardo da Silva', 38);'''
    curso.execute(sql_comando)
    conexao.commit()

except conn.DatabaseError as err:
    print("Erro de banco de dados", err)
finally:
    #fechamento de conexão
    if conexao:
        curso.close()
        conexao.close()
    print("Finalizado!")
    
    
             