import os

try:
    os.rmdir("diretorio")
    print("Diretório removido!")
except PermissionError as erro:
    print("sem permissão para remover diretório")
    print("Descrição do erro:", erro)
except FileNotFoundError as erro:
    print("Diretório inexistente!")
    print("Descrição do erro:", erro)
except OSError as erro:
    print("Outro erro")
    print("O diretório esta vazio?")
    print("Descrição do erro:", erro)
finally:
    print("Fim do Programa!")
    