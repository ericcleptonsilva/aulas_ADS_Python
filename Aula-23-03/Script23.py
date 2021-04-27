print("Abrindo arquivo")
try:
    open("teste01.pdf", "w")
    print("Arquivo aberto!")
except FileNotFoundError as erro:
    print("Arquico inexistente!")
    print("Descrição do erro:", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição do erro:", erro)
print("fim do programa!")
