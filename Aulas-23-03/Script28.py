import os
import errno

try:
    os.rmdir("diretorio")
    print("Diretorio removido")
except OSError as erro:
    print("Código do erro, errno:",erro.errno)
    if erro.errno == errno.ENOTEMPTY:
        print("O ditetório não esta vazio")
    else:
        print("Erro inesperado")
    print("Descrição de erro:", erro)
print("Fim do programa")
