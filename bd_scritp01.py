# importa mysql.connector as conn
# importa psycopg2 as conn
import sqlite3 as conn
# abertura de conexão
conexao = conn.connect('meu_banco.db')
print("Banco de dados criado com sucesso!")



