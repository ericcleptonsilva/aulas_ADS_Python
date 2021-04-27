import csv

with open("pessoas.csv") as arquivo:
    for registro in  arquivo:
        print("Nome: {} - Idade: {}".format(*registro.strip().split(',')))
if arquivo.closed:
    print()
    print(f"Arquivo {arquivo.name} já foi fechado!")
    