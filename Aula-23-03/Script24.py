import os

try:
    os.remove("text02.txt")
    print("Arquivo removido")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição de erro:", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo!")
    print("Descrição de erro:", erro)
except IsADirectoryError as erro:
    print("Remove: serve apenas para arquivos")
    print("Descrição de erro:", erro)
print("Fim do Programa!")
     