import sqlite3 as conn

# abertura de conexao e aquisição
conexao = conn.connect('meu_banco.db')
curso = conexao.cursor()

# exibindo dados da tabela cadastro
sql_comando = ''' select * from cadastro'''
curso.execute(sql_comando)

# retorna todos os registro solicitados pelo select (lista)
dados = curso.fetchall()
curso.close()
conexao.close()
    #print("Codigo:{:3} Nome:{:16}  Idade:{:>3}".format(*lista))
print('\n Conulsta ao Banco de Dados - meu_banco.db\n')
print('Dados da tabela - cadastro:')
print('='*43)
print('{:>12} {:<20} {:>6}'.format('Codigo', 'Nome', 'Idade'))
print('-' *42)
for lista in dados:
    print('{:>12} {:<16} {:>8}'.format(*lista))
print()
print('='*43)
if (len(dados) == 1):
    text = 'registro'
text = 'registros' 
print('Encontrado: {} {}'.format(len(dados), text))
print('\n')
print('Fim do relatório:')

    

