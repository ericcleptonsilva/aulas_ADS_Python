# split -  elinima espaços
# count -  numero de vezes de uma 
# determinada palavra

with open("date3.txt", "r") as arquivo:
    text = arquivo.read()
    contador = text.count("")
    print("Total de Ola = ", contador)
    
    
    
