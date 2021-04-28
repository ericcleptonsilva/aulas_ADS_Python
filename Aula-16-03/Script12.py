with open("date2.txt", "r") as arquivo:
    print("Repesentação do final da linha")
    for linha in arquivo:
        print(repr(linha))

with open("date2.txt", "r") as arquivo:
    print("Repesentação do final da linha após o strip")
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
