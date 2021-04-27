# split -  elinima espaços
# count -  numero de vezes de uma 
# determinada palavra

with open("date3.txt", "r") as arquivo:
    text = arquivo.read()
    text2 = text.split()
    contador = text2.count("vida")
    print("Total de Ola = ", contador)
    
    # usando o slipt para criar uma lista de palavras, desconhece o espaço
    frase1 = "amora  abacaxi  abacate  banna"
    lista_frase = frase1.split()
    print(lista_frase)
    
    # usando o split para criar uma lista de palavra, separado com virgular
    frase1 = "computador, driver, monitor, mouse"    
    lista_frase = frase1.split(",")
    print(lista_frase)
    
    