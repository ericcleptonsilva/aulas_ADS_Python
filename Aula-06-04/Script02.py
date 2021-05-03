import csv

arquivo = open("pessoas.csv")

for regis in arquivo:
    #print("Nome: {} - Idade: {}".format(*regis.split(',')))
    print("Nome: {} - Idade: {}".format(*regis.strip().split(',')))
arquivo.close()
