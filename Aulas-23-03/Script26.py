# operações em diretórios
#   os.mkdir(caminho)
#    os.rmdir(caminho)
import os

try:
    os.mkdir("diretorio")
    print("Diretório criado!")
except PermissionError as erro:
    print("sem permissão para criar diretório")
    print("Descrição do erro:", erro)
except FileExistsError as erro:
    print("Diretório já existe!")
    print("Descrição do erro:", erro)
finally:
    print("Fim do Programa!")
        