with open("date3.txt", "r") as arquivo:
    text = arquivo.read()
    lista_text = text.split()
    print("Contem Simplificada: ", lista_text.count("vida"))
