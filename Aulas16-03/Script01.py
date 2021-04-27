import os

# abrindo o arquivo text.txt
arquivo1 = open("text.txt")  # caminho relativo
# caminho absoluto
arquivo2 = open(
    "d:/ERIC/CURSOS/ESTACIO/ADS/Desenvolvimento Rápido de Aplicação em Python/python/text.txt")

# abrindo o arquivo dados.txt
arquivo3 = open("data/dados.txt")
# caminho absoluto
arquivo4 = open(
    "d:/ERIC/CURSOS/ESTACIO/ADS/Desenvolvimento Rápido de Aplicação em Python/python/data/dados.txt")

print("\n")
print("----------------com o OS os.path.realpath -----------------")

print(f"caminha relativo {os.path.realpath(arquivo2.name)}")
print(f"caminha relativo {os.path.realpath(arquivo3.name)}")

print("------------------------------------------------------------")
print("")
print("\n")
print("----------------com o OS os.path.abspath -----------------")
print(f"caminha absoluto {os.path.abspath(arquivo2.name)}")
print(f"caminha absoluto {os.path.abspath(arquivo4.name)}")
print(f"----------------------------------------------------------")
print("")

print("-----------------Sem a OS-----------------")
print(f"caminha relativo {arquivo1.name}\n")
print(f"caminha absoluto {arquivo2.name}\n")
print(f"caminha relativo {arquivo3.name}\n")
print(f"caminha absoluto {arquivo4.name}\n")
print("------------------------------------------")
print("\n")
