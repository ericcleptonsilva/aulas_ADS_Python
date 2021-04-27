import csv

with open('pessoas.csv') as arquivo:
    for pessoas in csv.reader(arquivo):
        print('Nome: {} - Idade: {}'.format(*pessoas))
        