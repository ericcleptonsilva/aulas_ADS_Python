import sqlite3 as conn
from sqlite3.dbapi2 import Cursor

try:

    # abertura de conexao e aquisição
    conexao = conn.connect('meu_banco.db')
    curso = conexao.cursor()
    # execução de comandos para a  criação de tabela
    sql_comando = ''' create table usuarios(
                      id integer not null,
                      nome text not null,
                      senha text not null,
                      primary key(id)
        
        );
    
    '''
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
    
             
