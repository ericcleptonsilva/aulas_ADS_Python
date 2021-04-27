# Contador de linhas
with open("date2.txt", "r") as arquivo:
    print("Total de linhas do arquivo")
    contador = 0
    for linha in arquivo:
        if linha.strip():
            contador +=1
    print("Total de linhas =", contador)
    