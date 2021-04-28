import random
print("Digite um número:")
n = 5  # input(int())
arquivo = open("Lista_de_Nomes.txt", 'w')
nomesL = list()
i = 0
with open('Atividade-27-04/Nome.txt', 'r') as Nome:
    lista_nome = Nome.readlines()

with open('Atividade-27-04/Sobrenome.txt', 'r') as Sobrenome:
    lista_sobrenome = Sobrenome.readlines()
for i in range(n):
    nome = lista_nome[i]
    sobrenoem = lista_sobrenome[i]
    idade = random.randint(1, 100)
    nome_completo = 'Nome: {} {} Idade: {}\n'.format(
        nome.strip(), sobrenoem.strip(), idade)
    print(nome_completo)
    nomesL.append(nome_completo)
arquivo.writelines(nomesL)

if Nome.closed and Sobrenome.closed:
    print()
    print(f"Arquivo {Nome.name} e {Sobrenome.name}já foi fechado!")
