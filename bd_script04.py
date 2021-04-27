import sqlite3 as conn

def ExibeDados(dados):
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
    
# abertura de conexao e aquisição
conexao = conn.connect('meu_banco.db')
curso = conexao.cursor()

sql_comando = ''' 
                    insert into cadastro (codigo, nome, idade)
                    values(?,?,?);'''
                   
print("Digite os dados separados por virgulas")
print('Codigo,Nome,Idade')
Ler = input()
while Ler != '':
    D = Ler.split(',')    
    try:
        curso.execute(sql_comando,D)
        conexao.commit()
    except:
        print('{} Dados inválidos'.format(D))
        print('Digite novamente, Exemplo: 0000,Maria,50')
        Ler = input()
    else:
        print('' * 30, '... dadps inseridos com sucesso!')
    finally:
        print('Codigo,Nome,Idade')
    Ler = input()
sql_comando = ''' select * from cadastro'''
curso.execute(sql_comando)

dados = curso.fetchall()

curso.close()
conexao.close()

ExibeDados(dados)


print('\n >>> Fim do relatório <<<')


