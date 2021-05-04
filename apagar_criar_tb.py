import sqlite3 as conn


#Abertura de conexão
conexao = conn.connect('automoveis.db')
cursor = conexao.cursor()
#executamndo comando alter para apagar uma coluna
#sql_query = ''' drop table veiculo'''
#efetivar o sql query
#cursor.execute(sql_query)

sql_query1 = ''' create table veiculo(
                    placa character(7) not null,
                    ano integer not null,
                    cor text not null,
                    motor real not null,
                    proprietario integer not null,
                    marca integer not null,
                    primary key(placa),
                    foreign key (proprietario) references pessoa(cpf),
                    foreign key (marca) references marca(id)
                    );'''

cursor.execute(sql_query1)

#efetivar o sql query
conexao.commit()

#fechamento das conexões
cursor.close()
conexao.close()

print("finalizado!")
