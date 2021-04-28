arquivo = open("text2.txt")

print("Iterando sobre o arquivo:")
for linha in arquivo:
    print(repr(linha))
    
    

arquivo.close()
