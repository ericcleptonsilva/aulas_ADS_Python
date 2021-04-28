# lista conteúdo de diretório
# os.scandir(caminho)

import os

try:
    entrada = os.scandir("diretorio")
    for obj in entrada:         
         print("Nome: ", obj.name)
         print("Caminho:", obj.path)
         print("É uma diretório? ", obj.is_dir())
         print("É uma arquivo? ", obj.is_file())
         if obj.is_file:
            print("Tamanho: ", obj.stat().st_size)
    print("----------------------------------")                
except FileExistsError as erro:
    print("O caminho não existe")
    
except NotADirectoryError as erro:
    print("O caminho não é  de um diretório")
    
    