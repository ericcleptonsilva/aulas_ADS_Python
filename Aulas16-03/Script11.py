print("Iterando sobre o arquivo")
with open("text2.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)
    print("fim do arquivo", arquivo.name)
    