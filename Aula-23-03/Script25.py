import os

try:
    os.rename("teste_abacaxi.txt", "teste03.txt")
    print("Arquivo renomeado")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição de erro:", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo!")
    print("Descrição de erro:", erro)
except IsADirectoryError as erro:
    print("Remove: serve apenas para arquivos")
    print("Descrição de erro:", erro)
except FileExistsError as erro:
    print("Arquivo de destino já existe!")
    print("Descrição de erro:", erro)
print("Fim do Programa!")
     