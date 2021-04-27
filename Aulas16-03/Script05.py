arquivo = open("text2.txt", "r")

conteudo = arquivo.readlines()

print("\n")
print("---------conteudo com readlines------------")
print(repr(conteudo))
print("-------------------------------------------")
print(f"Tipo de conteúdo: {type(conteudo)}")

print("-------------------------------------------")

arquivo.close()