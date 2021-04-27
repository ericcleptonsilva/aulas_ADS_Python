# atributos de um arquivo

arquivo = open("text.txt")

print("\n")
print(f"Nome do arquivo: {arquivo.name}")
print(f"Modo do arquivo: {arquivo.mode}")
print(f"Arquivo esta fechado? {arquivo.closed}")
arquivo.close()
print(f"Arquivo esta fechado? {arquivo.closed}")

print("\n")