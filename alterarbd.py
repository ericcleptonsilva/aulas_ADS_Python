import sqlite3 as conn


#Abertura de conexão
conexao = conn.connect('automoveis.db')
cursor = conexao.cursor()
#executamndo comando alter para adicionar mais uma coluna
sql_query = ''' alter table veiculo add modelo text'''

cursor.execute(sql_query)
#efetivar o sql query
conexao.commit()
#fechamento das conexões
cursor.close()
conexao.close()
print("finalizado!")
