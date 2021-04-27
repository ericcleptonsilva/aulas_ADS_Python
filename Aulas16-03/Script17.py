with open("date3.txt", "r") as arquivo:
    text = arquivo.read()
    print("Contagem direta: ",text.count("vida"))
    
contador = 0
list_text = text.split()
for lista in list_text:
    if lista == "vida":
        contador += 1
print("Contagem correta: ", contador)
        