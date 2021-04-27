import csv

arquivo = open("pessoas.csv")
dados = arquivo.read()
arquivo.close()
for regis in dados.splitlines():
    print("Nome: {} - Idade: {}".format(*regis.split(',')))
    
          
          