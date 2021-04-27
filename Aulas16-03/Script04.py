arquivo = open("text2.txt", "r")

conteudo = arquivo.readline()

print("\n")
print("---------conteudo com readline------------")
print(repr(conteudo))
proximo_conteudo = arquivo.readline()

print("---------proximo conteudo com readline------------")
print(repr(proximo_conteudo))
print("-------------------------------------------")
print(f"Tipo de conteúdo: {type(proximo_conteudo)}")

print("-------------------------------------------")

arquivo.close()
