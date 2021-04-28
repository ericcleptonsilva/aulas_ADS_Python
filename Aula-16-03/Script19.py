lista = ["arroz", "feijao", "macarrao"]

texto = ", ".join(lista)

with open("text1.txt", "w") as arquivo:
    arquivo.write(texto)
    
texto = " ".join(lista)

with open("text3.txt", "w") as arquivo:
    arquivo.write(texto)
