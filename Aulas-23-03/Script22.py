# tratamento de erro
# FileNotFoundError
# try/except ou try/except/finally

print("Abrindo arquivo")
try:
     open("teste.txt", "r")
     print("Arquivo aberto!")
except FileNotFoundError as erro:
     print("Arquico inexistente!")
     print("Descrição do erro:", erro)
print("fim do programa!")


